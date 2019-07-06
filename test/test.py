#!/usr/bin/env python
import pytest
import sys
sys.path.append('..')
from colp import Color,RGB,HSV,HEX,by_name

all_colors = by_name() # make sure to load before settting Color.MODE below
for c_name,c_var in all_colors.items():
    globals()[c_name] = c_var

# def hook(hookfunc, oldfunc):
#     def foo(*args, **kwargs):
#         hookfunc(*args, **kwargs)
#         return oldfunc(*args, **kwargs)
#     return foo

# def test_hook():
#     print('\n')
#     print('test_hook')
#     def hookfunc(args):
#         print('!')
#     for clazz in [RGB,HSV,HEX]:
#         for method_name in dir(clazz):
#             if callable(getattr(clazz, method_name)):
#                 setattr(clazz, method_name, hook(hookfunc, getattr(clazz, method_name)))
#     RGB(0,0,0).to(HSV)


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
    assert rgb_red.to(HEX).to(RGB) is not None
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
    assert is_named_blue and -sub == by_name('yellow') 

def test_rotate():
    print('\n')
    print('rotate')
    hsv_red = HSV(0,100,100)
    named_colors = by_name() 
    for i in range(0,360,60):
        rotated = hsv_red.rotate(angle=i)
        found = False
        for k,v in named_colors.items():
            if v == rotated:
                found = True
                print(k,v)
        is_rotated_named = rotated in list(named_colors.values())
        assert is_rotated_named

def test_web_safe():
    ws_hex_red = HEX('#f00')
    assert ws_hex_red == by_name('red')

def test__er_suffix_and_brightness():
    print('\n')
    print('brightness')
    darkest_red   = RGB(0,0,0).redder()
    darkest_green = RGB(0,0,0).greener()
    darkest_blue  = RGB(0,0,0).bluer()
    lightest_blue = RGB(254,255,255);
    print(darkest_red)
    print(darkest_green)
    print(darkest_blue)
    assert -darkest_red == lightest_blue
    assert darkest_red.brightness() == darkest_green.brightness() == darkest_blue.brightness() == 1/255

def test_access_channel():
    assert RGB(25,0,0)[0] == 25

def test_delta_brightness():
    print('\n')
    print('brightness')
    darkest_red = RGB(1,0,0)
    print(darkest_red.brighter(39))
    assert cyan.darker().brighter().brightness(normalise=False) == 254

def test_truediv_and_mul():
    print('\n')
    print('/ and *')
    red = RGB(255,0,0)
    faded_red = red / 3
    assert faded_red == RGB(85,0,0)
    assert faded_red * 3 == red
    hsv_red = red.to(HSV)
    assert hsv_red / 3 == faded_red

def test_and_or():
    print('\n')
    print('& and |')
    red = RGB(255,0,0)
    some_red = red & 3

def test_monochrome_check():
    darkest_gray = RGB(1,1,1)
    darkest_gray.is_monochrome()

def test_comparisons():
    assert RGB(255,0,127) >  RGB(200,200,200)
    assert RGB(1,2,3)     <  RGB(4,2,0)
    assert RGB(3,3,3)     <= RGB(3,2,0)
    assert RGB(3,6,3)     >= RGB(3,2,0)
    assert HSV(3,6,3)     >= RGB(3,2,0)
    assert purple         <  129
    assert purple.to(HSV) <  129

def test_float_inversion():
    print('\n')
    print('float inversion')

    a = RGB(1,100,1).to(HSV)
    assert isinstance(~a, HSV)

    z = RGB(0,15,255)
    z = ~z # test zero-containing channel
    assert str(z)

def test_floor_div():
    some_green = RGB(3,99,3)
    assert some_green // 3 == RGB(1,33,1)
    assert RGB(33,188,33) // some_green == RGB(11, 1, 11)

def test_truth():
    assert not black
    darkest_red   = RGB(0,0,1)
    darkest_green = RGB(0,1,0)
    darkest_blue  = RGB(1,0,0)
    assert HSV(0,0,0) == black == 0
    assert darkest_red and darkest_green and darkest_blue

def test_xor_and_getitem():
    some_red = RGB(128,64,32)
    some_other_red = some_red ^ 65
    assert some_other_red[1] == 1
    some_blue = RGB(64,32,128)
    abomination = some_red ^ some_blue
    abomination == RGB(192, 96, 160)

def test_iall():
    print('\n')
    print('iall')
    a = RGB(1,2,3)
    a *= 2
    a += 2
    a -= 2
    a /= 2
    a ^= 2
    a &= 2
    a |= 3
    a **= 9
    a %= 9
    a <<= 9
    a >>= 9

def test_interpolate():
    print('\n')
    print('interpolate')
    inclusive_between = blue.interpolate(red, 10)
    assert inclusive_between[0] == blue
    assert inclusive_between[-1] == red
    # assert inclusive_between[5][0] == inclusive_between[5][2] 
    print(inclusive_between)
    assert len(inclusive_between) == 10
    matrix = blue.interpolate((red,green), 10)
    for row in matrix:
        assert isinstance(row, list)

def test_is_major():
    assert RGB(120,119,100).is_red()
    assert RGB(119,120,100).is_green()
    assert RGB(119,120,130).is_blue()

def test_is_named_constant():
    Color.USE_CONSTANT_SPEC = None
    assert repr(gainsboro) == 'RGB(220, 220, 220)'
    assert repr(red) == "HEX('#ff0000')"
    Color.USE_CONSTANT_SPEC = 'hTmL'
    assert repr(gainsboro) == 'RGB(220, 220, 220)'
    assert repr(red) == "red"
    Color.USE_CONSTANT_SPEC = 'x11'
    assert repr(gainsboro) == 'gainsboro'
    assert repr(red) == "red"
    
# https://stackoverflow.com/questions/16444726/binary-representation-of-float-in-python-bits-not-hex
if __name__ == '__main__': 

    if False: # optionally run tests with visualizer
        import tkinter as tk 
        Color.visualizer = tk.Tk()

    for ptm in list(globals().keys()):
        if 'test' == ptm[:4]:
            eval(ptm + '()')
