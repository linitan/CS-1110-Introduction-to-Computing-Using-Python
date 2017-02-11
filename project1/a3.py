# a3.py
# Lini Tan (lt398)
# October 3
""" Functions for Assignment A3"""

import colormodel
import math

def complement_rgb(rgb):
    """Returns: the complement of color rgb.
    
    Parameter rgb: the color to complement
    Precondition: rgb is an RGB object"""
    return colormodel.RGB(255-rgb.red, 255-rgb.green, 255-rgb.blue)


def round(number, places):
    """Returns: the number rounded to the given number of decimal places.
    
    The value returned is a float.
    
    This function is more stable than the built-in round.  The built-in round
    has weird behavior where round(100.55,1) is 100.5 while round(100.45,1) is
    also 100.5.  We want to ensure that anything ending in a 5 is rounded UP.
    
    It is possible to write this function without the second precondition on
    places. If you want to do that, we leave that as an optional challenge.
    
    Parameter number: the number to round to the given decimal place
    Precondition: number is an int or float
    number is greater than or equal to 0.
    
    Parameter places: the decimal place to round to
    Precondition: places is an int; 0 <= places <= 3"""
    # To get the desired output, do the following
    #   1. Shift the number "to the left" so that the position to round to is left of 
    #      the decimal place.  For example, if you are rounding 100.556 to the first 
    #      decimal place, the number becomes 1005.56.  If you are rounding to the second 
    #      decimal place, it becomes 10055.6.  If you are rounding 100.556 to the nearest 
    #      integer, it remains 100.556.
    #   2. Add 0.5 to this number
    #   3. Convert the number to an int, cutting it off to the right of the decimal.
    #   4. Shift the number back "to the right" the same amount that you did to the left.
    #      Suppose that in step 1 you converted 100.556 to 1005.56.  In this case, 
    #      divide the number by 10 to put it back.
    if places == 1:
        number = number * 10
    elif places == 2:
        number = number * 100
    elif places == 3:
        number = number * 1000
    number = number + 0.5
    number = int(number)
    number = float(number)
    if places == 1:
        number = number / 10
    elif places == 2:
        number = number / 100
    elif places == 3:
        number = number / 1000
    return number


def str5(value):
    """ Returns: value as a string, but expand or round to be exactly 5 characters.
    
    The decimal point counts as one of the five characters.
   
    Examples:
        str5(1.3546)  is  '1.355'.
        str5(21.9954) is  '22.00'.
        str5(21.994)  is  '21.99'.
        str5(130.59)  is  '130.6'.
        str5(130.54)  is  '130.5'.
        str5(1)       is  '1.000'.
    
    Parameter value: the number to conver to a 5 character string.
    Precondition: value is a number (int or float), 0 <= value <= 360."""
    # Note:Obviously, you want to use the function round() that you just defined. 
    # However, remember that the rounding takes place at a different place depending 
    # on how big value is. Look at the examples in the specification.
    value = float(value)
    value = str(value)
    decimal = value.find('.')
    if (decimal == 1):
        value = float(value)
        value = round(value,3)
    elif (decimal == 2):
        value = float(value)
        value = round(value,2)
    elif (decimal == 3):
        value = float(value)
        value = round(value,1)
    value= str(value)
    value_long = len(value)
    if value_long == 4:
        value = value + '0'
    elif value_long ==3:
        value = value + '00'
    return value  


def str5_cmyk(cmyk):
    """Returns: String representation of cmyk in the form "(C, M, Y, K)".
    
    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)
    
    Example: if str(cmyk) is 
    
          '(0.0,31.3725490196,31.3725490196,0.0)'
    
    then str5_cmyk(cmyk) is '(0.000, 31.37, 31.37, 0.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter cmtk: the color to convert to a string
    Precondition: cmyk is an CMYK object."""
    cmyk_C = str5(cmyk.cyan)
    cmyk_M = str5(cmyk.magenta)
    cmyk_Y = str5(cmyk.yellow)
    cmyk_K = str5(cmyk.black)
    return '(' + cmyk_C + ', ' + cmyk_M + ', ' + cmyk_Y + ', ' + cmyk_K + ')' 


def str5_hsv(hsv):
    """Returns: String representation of hsv in the form "(H, S, V)".
    
    In the output, each of H, S, and V should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsv)
    
    Example: if str(hsv) is 
    
          '(0.0,0.313725490196,1.0)'
    
    then str5_hsv(hsv) is '(0.000, 0.314, 1.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter hsv: the color to convert to a string
    Precondition: hsv is an HSV object."""
    hsv_H = str5(hsv.hue)
    hsv_S = str5(hsv.saturation)
    hsv_V = str5(hsv.value)
    return '(' + hsv_H + ', ' + hsv_S + ', ' + hsv_V + ')'


def rgb_to_cmyk(rgb):
    """Returns: color rgb in space CMYK, with the most black possible.
    
    Formulae from en.wikipedia.org/wiki/CMYK_color_model.
    
    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object"""
    # The RGB numbers are in the range 0..255.
    # Change the RGB numbers to the range 0..1 by dividing them by 255.0.
    R = rgb.red
    G = rgb.green
    B = rgb.blue
    R = R / 255.0
    G = G / 255.0
    B = B / 255.0
    c = 1 - R
    m = 1 - G
    y = 1 - B
    if (c == m == y == 1):
        K = 1
        C = M = Y = 0
    else:
        K = min(c, m, y)
        C = (c - K)/(1 - K)
        M = (m - K)/(1 - K)
        Y = (y - K)/(1 - K)        
    K = K * 100
    C = C * 100
    M = M * 100
    Y = Y * 100
    return colormodel.CMYK(C,M,Y,K)


def cmyk_to_rgb(cmyk):
    """Returns : color CMYK in space RGB.

    Formulae from en.wikipedia.org/wiki/CMYK_color_model.
   
    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object."""
    # The CMYK numbers are in the range 0.0..100.0.  Deal with them in the 
    # same way as the RGB numbers in rgb_to_cmyk()
    C = cmyk.cyan
    M = cmyk.magenta
    Y = cmyk.yellow
    K = cmyk.black
    C = C / 100.0
    M = M / 100.0
    Y = Y / 100.0
    K = K / 100.0
    R = (1 - C) * (1 - K)
    G = (1 - M) * (1 - K)
    B = (1 - Y) * (1 - K)
    R = R * 255
    G = G * 255
    B = B * 255
    R = round(R,0)
    G = round(G,0)
    B = round(B,0)
    R = int(R)
    G = int(G)
    B = int(B)
    return colormodel.RGB(R,G,B) 


def rgb_to_hsv(rgb):
    """Return: color rgb in HSV color space.

    Formulae from wikipedia.org/wiki/HSV_color_space.
   
    Parameter rgb: the color to convert to a HSV object
    Precondition: rgb is an RGB object"""
    # The RGB numbers are in the range 0..255.
    # Change them to range 0..1 by dividing them by 255.0.
    R = rgb.red
    G = rgb.green
    B = rgb.blue
    R = R / 255.0
    G = G / 255.0
    B = B / 255.0
    MAX = max(R,G,B)
    MIN = min(R,G,B)
    if (MAX == MIN):
        H = 0
    elif (MAX == R and G >= B):
        H = 60.0 * (G - B) / (MAX - MIN)
    elif (MAX == R and G < B):
        H = 60.0 * (G - B) / (MAX - MIN) + 360.0
    elif MAX == G:
        H = 60.0 * (B - R) / (MAX - MIN) + 120.0
    elif MAX == B:
        H = 60.0 * (R - G) / (MAX - MIN) + 240.0
    if MAX == 0:
        S = 0
    else:
        S = 1 - MIN / MAX
    V = MAX
    return colormodel.HSV(H,S,V) 


def hsv_to_rgb(hsv):
    """Returns: color in RGB color space.
    
    Formulae from http://en.wikipedia.org/wiki/HSV_color_space.
    
    Parameter hsv: the color to convert to a RGB object
    Precondition: hsv is an HSV object."""
    H = hsv.hue
    S = hsv.saturation
    V = hsv.value
    H1 = math.floor(H / 60.0)
    f = H / 60.0 - H1
    p = V * (1 - S)
    q = V * (1 - f * S)
    t = V * (1 - (1-f) * S)
    if H1 == 0:
        R = V
        G = t
        B = p
    elif H1 == 1:
        R = q
        B = p
        G = V
    elif H1 == 2:
        R = p
        G = V
        B = t
    elif H1 == 3:
        R = p
        G = q
        B = V
    elif H1 == 4:
        R = t
        G = p
        B = V
    elif H1 == 5:
        R = V
        G = p
        B = q
    R = R * 255
    G = G * 255
    B = B * 255
    R = round(R,0)
    G = round(G,0)
    B = round(B,0)
    R = int(R)
    G = int(G)
    B = int(B)
    return colormodel.RGB(R,G,B) 
        
