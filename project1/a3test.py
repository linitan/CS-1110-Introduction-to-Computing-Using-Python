# a3test.py
# Lini Tan (lt398)
# October 3
""" Unit Test for Assignment A3"""

import colormodel
import cornelltest
import a3


def test_complement():
    """Test function complement"""
    cornelltest.assert_equals(colormodel.RGB(255-250, 255-0, 255-71),
                              a3.complement_rgb(colormodel.RGB(250, 0, 71)))


def test_round():
    """Test function round (a3 version)"""
    cornelltest.assert_equals(130.6,   a3.round(130.59,1))
    cornelltest.assert_equals(130.5,   a3.round(130.54,1))
    cornelltest.assert_equals(100.0,   a3.round(100,1))
    cornelltest.assert_equals(100.6,   a3.round(100.55,1))
    cornelltest.assert_equals(99.57,   a3.round(99.566,2))
    cornelltest.assert_equals(99.99,   a3.round(99.99,2))
    cornelltest.assert_equals(100.0,   a3.round(99.995,2))
    cornelltest.assert_equals(22.00,   a3.round(21.99575,2))
    cornelltest.assert_equals(21.99,   a3.round(21.994,2))
    cornelltest.assert_equals(10.01,   a3.round(10.013567,2))
    cornelltest.assert_equals(10.0,    a3.round(10.000000005,2))
    cornelltest.assert_equals(10.0,    a3.round(9.9999,3))
    cornelltest.assert_equals(9.999,   a3.round(9.9993,3))
    cornelltest.assert_equals(1.355,   a3.round(1.3546,3))
    cornelltest.assert_equals(1.354,   a3.round(1.3544,3))
    cornelltest.assert_equals(0.046,   a3.round(.0456,3))
    cornelltest.assert_equals(0.045,   a3.round(.0453,3))
    cornelltest.assert_equals(0.006,   a3.round(.0056,3))
    cornelltest.assert_equals(0.001,   a3.round(.0013,3))
    cornelltest.assert_equals(0.0,     a3.round(.0004,3))
    cornelltest.assert_equals(0.001,   a3.round(.0009999,3))
    cornelltest.assert_equals(2.0,     a3.round(2,1))
    cornelltest.assert_equals(3.00,    a3.round(3,2))
    cornelltest.assert_equals(4.000,   a3.round(4,3))


def test_str5():
    """Test function str5"""
    cornelltest.assert_equals('130.6',  a3.str5(130.59))
    cornelltest.assert_equals('130.5',  a3.str5(130.54))
    cornelltest.assert_equals('100.0',  a3.str5(100))
    cornelltest.assert_equals('100.6',  a3.str5(100.55))
    cornelltest.assert_equals('99.57',  a3.str5(99.566))
    cornelltest.assert_equals('99.99',  a3.str5(99.99))
    cornelltest.assert_equals('100.0',  a3.str5(99.995))
    cornelltest.assert_equals('22.00',  a3.str5(21.99575))
    cornelltest.assert_equals('21.99',  a3.str5(21.994))
    cornelltest.assert_equals('10.01',  a3.str5(10.013567))
    cornelltest.assert_equals('10.00',  a3.str5(10.000000005))
    cornelltest.assert_equals('10.00',  a3.str5(9.9999))
    cornelltest.assert_equals('9.999',  a3.str5(9.9993))
    cornelltest.assert_equals('1.355',  a3.str5(1.3546))
    cornelltest.assert_equals('1.354',  a3.str5(1.3544))
    cornelltest.assert_equals('0.046',  a3.str5(.0456))
    cornelltest.assert_equals('0.045',  a3.str5(.0453))
    cornelltest.assert_equals('0.006',  a3.str5(.0056))
    cornelltest.assert_equals('0.001',  a3.str5(.0013))
    cornelltest.assert_equals('0.000',  a3.str5(.0004))
    cornelltest.assert_equals('0.001',  a3.str5(.0009999))
    cornelltest.assert_equals('1.000',  a3.str5(1))
    cornelltest.assert_equals('0.000',  a3.str5(0))
    cornelltest.assert_equals('360.0',  a3.str5(360))
    cornelltest.assert_equals('78.00',  a3.str5(78))


def test_str5_color():
    """Test the str5 functions for cmyk and hsv."""
    cornelltest.assert_equals('(98.45, 25.36, 72.80, 1.000)',
                              a3.str5_cmyk(colormodel.CMYK(98.448, 25.362, 72.8, 1.0)));
    cornelltest.assert_equals('(76.86, 0.000, 9.429, 100.0)',
                              a3.str5_cmyk(colormodel.CMYK(76.858, 0.000, 9.42885, 100.0)));
    
    # Tests for round5_hsv (add two)
    cornelltest.assert_equals('(12.00, 0.468, 0.325)',
                              a3.str5_hsv(colormodel.HSV(12,0.46792,0.32456)));
    cornelltest.assert_equals('(225.3, 0.151, 0.786)',
                              a3.str5_hsv(colormodel.HSV(225.298,0.1512256,0.78610)));


def test_rgb_to_cmyk():
    """Test rgb_to_cmyk"""
    rgb = colormodel.RGB(255, 255, 255);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('0.000', a3.str5(cmyk.cyan))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.magenta))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.yellow))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.black))
    
    rgb = colormodel.RGB(0, 0, 0);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('0.000', a3.str5(cmyk.cyan))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.magenta))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.yellow))
    cornelltest.assert_equals('100.0', a3.str5(cmyk.black))
        
    rgb = colormodel.RGB(217, 43, 164);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('0.000', a3.str5(cmyk.cyan))
    cornelltest.assert_equals('80.18', a3.str5(cmyk.magenta))
    cornelltest.assert_equals('24.42', a3.str5(cmyk.yellow))
    cornelltest.assert_equals('14.90', a3.str5(cmyk.black))
    
    rgb = colormodel.RGB(0, 165, 39);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('100.0', a3.str5(cmyk.cyan))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.magenta))
    cornelltest.assert_equals('76.36', a3.str5(cmyk.yellow))
    cornelltest.assert_equals('35.29', a3.str5(cmyk.black))
    
    rgb = colormodel.RGB(23, 66, 188);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('87.77', a3.str5(cmyk.cyan))
    cornelltest.assert_equals('64.89', a3.str5(cmyk.magenta))
    cornelltest.assert_equals('0.000', a3.str5(cmyk.yellow))
    cornelltest.assert_equals('26.27', a3.str5(cmyk.black))


def test_cmyk_to_rgb():
    """Test translation function cmyk_to_rgb"""
    cmyk = colormodel.CMYK(88.44, 76.99, 5.528, 21.96);
    rgb = a3.cmyk_to_rgb(cmyk);
    cornelltest.assert_equals('23.00', a3.str5(rgb.red))
    cornelltest.assert_equals('46.00', a3.str5(rgb.green))
    cornelltest.assert_equals('188.0', a3.str5(rgb.blue))
    
    cmyk = colormodel.CMYK(46.98, 55.10, 100.0, 2.122);
    rgb = a3.cmyk_to_rgb(cmyk);
    cornelltest.assert_equals('132.0', a3.str5(rgb.red))
    cornelltest.assert_equals('112.0', a3.str5(rgb.green))
    cornelltest.assert_equals('0.000', a3.str5(rgb.blue))
 
    cmyk = colormodel.CMYK(0.000, 100.0, 100.0, 0.000);
    rgb = a3.cmyk_to_rgb(cmyk);
    cornelltest.assert_equals('255.0', a3.str5(rgb.red))
    cornelltest.assert_equals('0.000', a3.str5(rgb.green))
    cornelltest.assert_equals('0.000', a3.str5(rgb.blue))


def test_rgb_to_hsv():
    """Test translation function rgb_to_hsv"""
    #Test case 1: MAX = MIN
    rgb = colormodel.RGB(255, 255, 255);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('0.000', a3.str5(hsv.hue))
    cornelltest.assert_equals('0.000', a3.str5(hsv.saturation))
    cornelltest.assert_equals('1.000', a3.str5(hsv.value))
    
    #Test case 2: MAX = R and G > B
    rgb = colormodel.RGB(188, 56, 9);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('15.75', a3.str5(hsv.hue))
    cornelltest.assert_equals('0.952', a3.str5(hsv.saturation))
    cornelltest.assert_equals('0.737', a3.str5(hsv.value))
    
    #Test case 3: MAX = R and G = B
    rgb = colormodel.RGB(62, 7, 7);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('0.000', a3.str5(hsv.hue))
    cornelltest.assert_equals('0.887', a3.str5(hsv.saturation))
    cornelltest.assert_equals('0.243', a3.str5(hsv.value))
    
    #Test case 4: MAX = R and G < B
    rgb = colormodel.RGB(245, 66, 99);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('348.9', a3.str5(hsv.hue))
    cornelltest.assert_equals('0.731', a3.str5(hsv.saturation))
    cornelltest.assert_equals('0.961', a3.str5(hsv.value))
    
    #Test case 5: MAX = G
    rgb = colormodel.RGB(24, 178, 88);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('144.9', a3.str5(hsv.hue))
    cornelltest.assert_equals('0.865', a3.str5(hsv.saturation))
    cornelltest.assert_equals('0.698', a3.str5(hsv.value))
    
    #Test case 6: MAX = B
    rgb = colormodel.RGB(6, 2, 8);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('280.0', a3.str5(hsv.hue))
    cornelltest.assert_equals('0.750', a3.str5(hsv.saturation))
    cornelltest.assert_equals('0.031', a3.str5(hsv.value))  


def test_hsv_to_rgb():
    """Test translation function hsv_to_rgb"""
    #Test case 1: H1 = 0
    hsv = colormodel.HSV(0.000, 1.000, 0.765);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals('195.0', a3.str5(rgb.red))
    cornelltest.assert_equals('0.000', a3.str5(rgb.green))
    cornelltest.assert_equals('0.000', a3.str5(rgb.blue))    

    #Test case 2: H1 = 1
    hsv = colormodel.HSV(77.23, 0.652, 0.148);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals('31.00', a3.str5(rgb.red))
    cornelltest.assert_equals('38.00', a3.str5(rgb.green))
    cornelltest.assert_equals('13.00', a3.str5(rgb.blue))
    
    #Test case 3: H1 = 2
    hsv = colormodel.HSV(178, 0.999, 0.001);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals('0.000', a3.str5(rgb.red))
    cornelltest.assert_equals('0.000', a3.str5(rgb.green))
    cornelltest.assert_equals('0.000', a3.str5(rgb.blue))
    
    #Test case 4: H1 = 3
    hsv = colormodel.HSV(222.8, 1.000, 0.521);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals('0.000', a3.str5(rgb.red))
    cornelltest.assert_equals('38.00', a3.str5(rgb.green))
    cornelltest.assert_equals('133.0', a3.str5(rgb.blue))
    
    #Test case 5: H1 = 4
    hsv = colormodel.HSV(240.1, 0.366, 0.771);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals('125.0', a3.str5(rgb.red))
    cornelltest.assert_equals('125.0', a3.str5(rgb.green))
    cornelltest.assert_equals('197.0', a3.str5(rgb.blue))
    
    #Test case 6: H1 = 5
    hsv = colormodel.HSV(359.9, 0.295, 0.402);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals('103.0', a3.str5(rgb.red))
    cornelltest.assert_equals('72.00', a3.str5(rgb.green))
    cornelltest.assert_equals('72.00', a3.str5(rgb.blue))
 
 
# Script Code
# THIS PREVENTS THE TESTS RUNNING ON IMPORT
if __name__ == "__main__":
    test_complement()
    test_round()
    test_str5()
    test_str5_color()
    test_rgb_to_cmyk()
    test_cmyk_to_rgb()
    test_rgb_to_hsv()
    test_hsv_to_rgb()
    print "Module a3 is working correctly"
