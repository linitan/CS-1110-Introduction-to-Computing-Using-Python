# play.py
# Lini Tan lt398
# Dec 4
"""Subcontroller module for Breakout

This module contains the subcontroller to manage a single game in the Breakout App. 
Instances of Play represent a single game.  If you want to restart a new game, you are 
expected to make a new instance of Play.

The subcontroller Play manages the paddle, ball, and bricks.  These are model objects.  
Their classes are defined in models.py.

Most of your work on this assignment will be in either this module or models.py.
Whether a helper method belongs in this module or models.py is often a complicated
issue.  If you do not know, ask on Piazza and we will answer."""
from constants import *
from game2d import *
from models import *


# PRIMARY RULE: Play can only access attributes in models.py via getters/setters
# Play is NOT allowed to access anything in breakout.py (Subcontrollers are not
# permitted to access anything in their parent. To see why, take CS 3152)

class Play(object):
    """An instance controls a single game of breakout.
    
    This subcontroller has a reference to the ball, paddle, and bricks. It animates the 
    ball, removing any bricks as necessary.  When the game is won, it stops animating.  
    You should create a NEW instance of Play (in Breakout) if you want to make a new game.
    
    If you want to pause the game, tell this controller to draw, but do not update.  See 
    subcontrollers.py from Lecture 25 for an example.
    
    INSTANCE ATTRIBUTES:
        _paddle [Paddle]: the paddle to play with 
        _bricks [list of Brick]: the list of bricks still remaining 
        _ball   [Ball, or None if waiting for a serve]:  the ball to animate
        _tries  [int >= 0]: the number of tries left 
    
    As you can see, all of these attributes are hidden.  You may find that you want to
    access an attribute in class Breakout. It is okay if you do, but you MAY NOT ACCESS 
    THE ATTRIBUTES DIRECTLY. You must use a getter and/or setter for any attribute that 
    you need to access in Breakout.  Only add the getters and setters that you need for 
    Breakout.
    
    You may change any of the attributes above as you see fit. For example, you may want
    to add new objects on the screen (e.g power-ups).  If you make changes, please list
    the changes with the invariants.
                  
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
        number  [int >= 0]: the number of the score the user got
        score   [GLabel]: display the current score of user
    """
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    def getbricks(self):
        """Return the _brick attribute of current play.
        """
        return self._bricks
    
    def getballtop(self):
        """Return the vertical coordinate of the top edge of _ball attribute of current play.
        """
        return self._ball.top
     
    # INITIALIZER (standard form) TO CREATE PADDLES AND BRICKS
    def __init__(self):
        """Initializer: Creates paddles and bricks.
        
        Create the bricks wall, paddle and ball which is necessary for the game.
        """
        self._bricks = self._createwall()
        self._paddle = Paddle(x=GAME_WIDTH/2.0,y=PADDLE_OFFSET,fillcolor=PADDLECOLOR)
        self._ball = None
        self.number = 0
        self.score = GLabel(text = "score:" + str(self.number),
                           font_name = 'ComicSansBold', x = 50,
                           y = 10, font_size = 15)
        self.mssg = None
                  
    # UPDATE METHODS TO MOVE PADDLE, SERVE AND MOVE THE BALL
    def updatePaddle(self,Input,dt):
        """Animates the paddle.
        
        Parameter dt: The time since the last animation frame.
        Precondition: dt is a float.
        Parameter Input: The input of keyboard to be detected.
        Precondition: Instance of GInput; it is inherited from GameApp.
        
        Citation: the method of how to detect the curr_key and last_key is modified
        from arrows.py. Original author is CS1110 instructor.
        """
        da = 0
        if Input.is_key_down('left'):
            da -= ANIMATION_STEP
        if Input.is_key_down('right'):
            da += ANIMATION_STEP
        # Change the position
        newpos = self._paddle.x + da
        if max(newpos,GAME_WIDTH-PADDLE_WIDTH/2.0) == newpos:
            self._paddle.x = GAME_WIDTH-PADDLE_WIDTH/2.0
        elif min(newpos,PADDLE_WIDTH/2.0) == newpos:
            self._paddle.x = PADDLE_WIDTH/2.0
        else:    
            self._paddle.x = self._paddle.x + da
    
    def updateBall(self):
        """move the ball and handle any physics.
        
        This function firstly update the position of ball in every frame. Then
        it makes the ball bounce away if it hits the wall or brick, paddle. In
        addition, if it hits the brick, the brick will be removed from the brick
        wall.
        """
        self._ball.dropball()
        self._ball.hitwall()
        if self._paddle.collides(self._ball) == True:
            bounceball = Sound('bounce.wav')
            bounceball.play()
            if self._ball.getx()<=self._paddle.getx()-PADDLE_WIDTH/4.0 or self._ball.getx() >= self._paddle.getx()+PADDLE_WIDTH/4.0:
                self._ball.specialbounceball()
            self._ball.bounceball()
        for row in self._bricks:
            for brick in row:
                if brick.collides(self._ball) == True:
                    breakbrick = Sound('plate2.wav')
                    breakbrick.play()
                    self._ball.bounceball()
                    row.remove(brick)
                    self.updatescore()
            if len(row) == 0:
                goodjob = Sound('win.wav')
                goodjob.play()
                self._bricks.remove(row)
    
    # DRAW METHOD TO DRAW THE PADDLES, BALL, AND BRICKS
    def draw(self,view):
        """Draws the paddles, ball and bricks to the application window (view).
        
        Parameter: The view window
        Precondition: view is a GView."""
        for x in self._bricks:
            for y in x:
                y.draw(view)
        self._paddle.draw(view)
        if not self._ball is None:
            self._ball.draw(view)
        if not self.score is None:
            self.score.draw(view)
       
    # HELPER METHODS FOR PHYSICS AND COLLISION DETECTION
    def _createwall(self):
        """Create the brick wall.
        
        Using global constants given in module constants to create a brick wall.
        The colors of the bricks remain constant for two rows and run in the following
        sequence: RED, ORANGE, YELLOW, GREEN, CYAN. If there are more than 10 rows, you
        are to start over with RED, and do the sequence again.
        """
        wall = []
        row = 1
        left = BRICK_SEP_H/2
        y = GAME_HEIGHT-BRICK_Y_OFFSET-BRICK_HEIGHT/2
        fillcolor = BRICK_COLORS1
        while row <= BRICK_ROWS:
            if not row == 1:
                y = y-BRICK_HEIGHT-BRICK_SEP_V
            if row % 10 == 3 or row % 10 == 4:
                fillcolor = BRICK_COLORS2
            elif row % 10 ==5 or row % 10 == 6:
                fillcolor = BRICK_COLORS3
            elif row % 10 == 7 or row % 10 == 8:
                fillcolor = BRICK_COLORS4
            elif row % 10 == 9 or row % 10 == 0:
                fillcolor = BRICK_COLORS5
            wall.append([Brick(left,y,fillcolor)])
            row = row + 1
        for x in range(len(wall)):
            i = 1
            y = wall[x][0].gety()
            fillcolor = wall[x][0].getfillcolor()
            left = wall[x][0].getleft()
            while i < BRICKS_IN_ROW:
                left = left + BRICK_SEP_H + BRICK_WIDTH
                wall[x].append(Brick(left,y,fillcolor))
                i = i + 1
        return wall
    
    # ADD ANY ADDITIONAL METHODS (FULLY SPECIFIED) HERE
    def makeball(self):
        """ make a new ball.
        
        This is the helper function for _counttime() in Breakout.py. It is to
        help it make a new ball at the end of _state:countdown.
        """
        self._ball = Ball()
           
    def updatescore(self):
        """ Update score once the user hit the brick.
        
        The function will increase the number by 2 everytime the user hit a brick.
        """
        self.number = self.number + 2
        self.score = GLabel(text = "score:" + str(self.number),
                           font_name = 'ComicSansBold', x = 50,
                           y = 10, font_size = 15)
        