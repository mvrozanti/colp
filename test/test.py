#!/usr/bin/env python
import unittest
import sys
sys.path.append('..')
from src.colordef import RGB,HSV,HEX

def test_color_conversion():
    rgb = RGB(255,0,255)
    assert rgb 
    hsv = rgb.to(HSV)
    assert hsv is not None
    print('aaa')
