#!/usr/bin/env python
import unittest
import sys
sys.path.append('..')
from src.colordef import RGB,HSV,HEX

def test_inter_color_sum():
    print('\n')
    rgb_blue = RGB(0,  0,255)
    rgb_red  = RGB(255,0,  0)
    hsv_red = rgb_red.to(HSV)
    hsv_blue = rgb_blue.to(HSV)
    print(hsv_red)
    print('+')
    print(rgb_blue)
    print('_'*15)
    sum1 = hsv_red + rgb_blue
    assert 0 <= max(sum1.get_dimensions()) <= 255

    sum2 = rgb_red + hsv_blue
    assert sum1 == sum2

def test_color_sum():
    print('\n')
    rgb_blue = RGB(0,  0,255)
    rgb_red  = RGB(255,0,  0)
    print(rgb_blue)
    print('+')
    print(rgb_red)
    print('_'*15)
    sum = rgb_red + rgb_blue
    print(sum)
    assert sum == RGB(255,0,255)

def test_color_conversion():
    print('\n')
    rgb_red  = RGB(255,0,0)
    rgb_blue = RGB(0,0,255)
    hsv_red = rgb_red.to(HSV)
    assert hsv_red.get_dimensions() == [0.0,1.0,255]
    hsv_red = HSV(0,1,255)
    assert hsv_red.get_dimensions() == [0.0,1.0,255]
    assert hsv_red.to(RGB) == rgb_red
    sum = rgb_red + hsv_red

if __name__ == '__main__':
    for ptm in list(globals().keys()):
        if 'test' == ptm[:4]:
            eval(ptm + '()')
