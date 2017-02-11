# models.py
# Lini Tan lt398
# Dec 4
"""Models module for Breakout

This module contains the model classes for the Breakout game. That is anything that you
interact with on the screen is model: the paddle, the ball, and any of the bricks.

Technically, just because something is a model does not mean there has to be a special 
class for it.  Unless you need something special, both paddle and individual bricks could
just be instances of GRectangle.  However, we do need something special: collision 
detection.  That is why we have custom classes.

You are free to add new models to this module.  You may wish to do this when you add
new features to your game.  If you are unsure about whether to make a new class or 
not, please ask on Piazza."""
import random # To randomly generate the ball velocity
from constants import *
from game2d import *


# PRIMARY RULE: Models are not allowed to access anything except the module constants.py.
# If you need extra information from Play, then it should be a parameter in your method, 
# and Play should pass it as a argument when it calls the method.


class Paddle(GRectangle):
    """An instance is the game paddle.
    
    This class contains a method to detect collision with the ball, as well as move it
    left and right.  You may wish to add more features to this class.
    
    The attributes of this class are those inherited from GRectangle.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    def getx(self):
        """Return the horizontal coordinate of the object center.
        """
        return self.x
    
    def gety(self):
        """Return the vertical coordinate of the object center.
        """
        return self.y
    
    # INITIALIZER TO CREATE A NEW PADDLE
    def __init__(self,x,y,fillcolor):
        """Initializer: Creates a new paddle.
        
        Create a new paddle whose position, linecolor, fillcolor, height and width
        fit the requirement of constants.
        """
        GRectangle.__init__(self,x=x,y=y,linecolor = fillcolor,fillcolor=fillcolor,
                            height = PADDLE_HEIGHT,width = PADDLE_WIDTH)
    
    # METHODS TO MOVE THE PADDLE AND CHECK FOR COLLISIONS
    def collides(self,ball):
        """Returns: True if the ball collides with this paddle
        
        Parameter ball: The ball to check
        Precondition: ball is of class Ball.
        """
        if ball.getvy()<0:
            if self.contains(ball.getx()-BALL_DIAMETER/2.0,ball.gety()+BALL_DIAMETER/2.0) == True:
                return True
            elif self.contains(ball.getx()-BALL_DIAMETER/2.0,ball.gety()-BALL_DIAMETER/2.0) == True:
                return True
            elif self.contains(ball.getx()+BALL_DIAMETER/2.0,ball.gety()+BALL_DIAMETER/2.0) == True:
                return True
            elif self.contains(ball.getx()+BALL_DIAMETER/2.0,ball.gety()-BALL_DIAMETER/2.0) == True:
                return True
        return False   
    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY


class Brick(GImage):
    """An instance is the game paddle.
    
    This class contains a method to detect collision with the ball.  You may wish to 
    add more features to this class.
    
    The attributes of this class are those inherited from GRectangle.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    def getleft(self):
        """Return the left edge of this shape.
        """
        return self.left
    
    def gety(self):
        """Return the vertical coordinate of the object center.
        """
        return self.y
    
    def getfillcolor(self):
        """Return the fill color of that object.
        """
        return self.fillcolor
    
    # INITIALIZER TO CREATE A BRICK
    def __init__(self,left,y,fillcolor):
        """Initializer: Creates a new brick.
        
        Create a new paddle whose position, linecolor, fillcolor, height and width
        fit the requirement of constants. It contains a picture source which would
        be presented in the brick.
        """
        GImage.__init__(self,left=left,y=y,linecolor=fillcolor,fillcolor=fillcolor,
                            height = BRICK_HEIGHT,width=BRICK_WIDTH,source='final.png')
        
    # METHOD TO CHECK FOR COLLISION
    def collides(self,ball):
        """Returns: True if the ball collides with this brick
        
        Parameter ball: The ball to check
        Precondition: ball is of class Ball.
        """
        if self.contains(ball.getx()-BALL_DIAMETER/2.0,ball.gety()+BALL_DIAMETER/2.0) == True:
            return True
        elif self.contains(ball.getx()-BALL_DIAMETER/2.0,ball.gety()-BALL_DIAMETER/2.0) == True:
            return True
        elif self.contains(ball.getx()+BALL_DIAMETER/2.0,ball.gety()+BALL_DIAMETER/2.0) == True:
            return True
        elif self.contains(ball.getx()+BALL_DIAMETER/2.0,ball.gety()-BALL_DIAMETER/2.0) == True:
            return True
        else:
            return False
    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY


class Ball(GImage):
    """Instance is a game ball.
    
    We extend GEllipse because a ball must have additional attributes for velocity.
    This class adds this attributes and manages them.
    
    INSTANCE ATTRIBUTES:
        _vx [int or float]: Velocity in x direction 
        _vy [int or float]: Velocity in y direction 
    
    The class Play will need to look at these attributes, so you will need
    getters for them.  However, it is possible to write this assignment with no
    setters for the velocities.
    
    How? The only time the ball can change velocities is if it hits an obstacle
    (paddle or brick) or if it hits a wall.  Why not just write methods for these
    instead of using setters?  This cuts down on the amount of code in Gameplay.
    
    NOTE: The ball does not have to be a GEllipse. It could be an instance
    of GImage (why?). This change is allowed, but you must modify the class
    header up above.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    def getvx(self):
        """Return the velocity in x direction.
        """
        return self._vx
    
    def getvy(self):
        """Return the velocity in y direction.
        """        
        return self._vy
    
    def getx(self):
        """Return the horizontal coordinate of this shape.
        """        
        return self.x
    
    def gety(self):
        """Return the vertical coordinate of the object center.
        """        
        return self.y
    
    # INITIALIZER TO SET RANDOM VELOCITY
    def __init__(self):
        """Initializer: To initialize a ball with random velocity.
        
        The x, y, width, height, source attributes are all inherented form GImage.
        _vy is a specific negative number and _vx is a random number.
        """
        GImage.__init__(self,x=GAME_WIDTH/2.0,y=GAME_HEIGHT/2.0,width=BALL_DIAMETER,height=BALL_DIAMETER,
                                  source = 'beach-ball.png')
        self._vx = random.uniform(1.0,5.0) 
        self._vx = self._vx * random.choice([-1, 1])
        self._vy = -5.0
        
    # METHODS TO MOVE AND/OR BOUNCE THE BALL
    def dropball(self):
        """Move the ball down step by step.
        
        Each time the new method is called, it should move the ball one step.
        Simply add the ball's velocity attributes to the ball's corresponding
        position coordinates.
        """
        self.x = self.x + self._vx
        self.y = self.y + self._vy
        
    def hitwall(self):
        """bounce the ball if it hit the wall
        
        As the ball moves, it should change direction if it hits a wall. For instance,
        If the ball is going up, check if any part of the ball has a y-coordinate
        greater than or equal to GAME_HEIGHT. In that case the ball has reached
        the top and its direction has to be changed so that it goes down. You do
        this by setting _vy attribute to -_vy. 
        """
        if self.contains(self.x,GAME_HEIGHT) == True:
            self._vy = -self._vy
        elif self.contains(0,self.y) == True:
            self._vx = -self._vx
        elif self.contains(GAME_WIDTH,self.y) == True:
            self._vx = -self._vx
           
    def bounceball(self):
        """bounce the ball.
        
        This is a helper function to set _vy attribute to -_vy.  
        """
        self._vy = -self._vy
            
    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY
    def specialbounceball(self):
        """bounce the ball.
        
        This is a helper function to set _vx attribute to -_vx.  
        """
        self._vx = -self._vx        

# IF YOU NEED ADDITIONAL MODEL CLASSES, THEY GO HERE