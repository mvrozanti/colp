#!/usr/bin/env python
import unittest
import sys
sys.path.append('..')
from src.colordef import Color,RGB,HSV,HEX,by_name

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
    assert hsv_red.get_dimensions(normalise=True)  == [0.0,1.0,1.0]
    assert hsv_red.get_dimensions(normalise=False) == [0,100,100]
    hsv_red = HSV(0,100,100)
    assert hsv_red.get_dimensions(normalise=True) == [0.0,1.0,1.0]
    assert hsv_red.to(RGB) == rgb_red
    sum = rgb_red + hsv_red

def test_negation_subtraction():
    print('\n')
    hsv_red = HSV(0,100,100)
    rgb_red = RGB(255,0,  0)
    rgb_black = hsv_red - rgb_red
    assert not any(rgb_black.get_dimensions())

    rgb_magenta = RGB(255,0,255)
    print(rgb_magenta)
    print('-')
    print(hsv_red)
    print('_'*15)
    sub = rgb_magenta - hsv_red
    print(sub)
    is_named_blue = sub == by_name('blue') 
    assert is_named_blue
    assert -sub == by_name('yellow') 

def test_rotate():
    print('\n')
    print('rotate')
    hsv_red = HSV(0,100,100)
    named_colors = by_name() 
    for i in range(0,360,60):
        rotated = hsv_red.rotate(angle=i)
        is_rotated_named = rotated in list(named_colors.values())
        assert is_rotated_named

def test_web_safe():
    ws_hex_red = HEX('#f00')
    assert ws_hex_red == HEX('#ff0000')

# if __name__ == '__main__': # run tests
#     for ptm in list(globals().keys()):
#         if 'test' == ptm[:4]:
#             eval(ptm + '()')
