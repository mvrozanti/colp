#!/usr/bin/env python
from abc import ABC, abstractmethod
import copy
import colorsys

class Color(ABC):

    def __radd__(self, o):
        return self.__add__(o);

    def __rsub__(self, o):
        return self.__sub__(o);

    @abstractmethod
    def get_dimensions(self):
        pass

    def normalised(self):
        pass

    @abstractmethod
    def to(self, colorspace):
        import inspect
        if inspect.isclass(colorspace) and issubclass(colorspace, Color):
            clone = copy.copy(self)
            clone.__class__ = colorspace
        else:
            raise('Invalid colorspace')

    def rotate(self, col, angle=1.):
        if not isinstance(col, HSV):
            col = col.to(HSV)
        col.rotate(angle)


class RGB(Color):

    def __init__(self, r, g, b, a=0):
        self.r = r;
        self.g = g;
        self.b = b;
        self.a = a;
        
    def get_dimensions(self):
        return [self.r,self.g,self.b] + ([self.a] if self.a else [])

    def to(self, colorspace, normalise=False):
        if not colorspace or isinstance(self, colorspace):
            return self
        if colorspace is HSV:
            hsv_dimensions = colorsys.rgb_to_hsv(*self.get_dimensions())
            return HSV(*hsv_dimensions)

    def __add__(self, o): 
        if isinstance(o, Color):
            o = o.to(RGB)
            rr = o.r + self.r
            rg = o.g + self.g
            rb = o.b + self.b
            sum = RGB(rr,rg,rb)
            return sum
        else:
            try:
                return RGB(max(self.r + o, 0), max(self.g + o, 0), max(self.b + o, 0)) 
            except:
                raise('Invalid addition')

    def __eq__(self, o):
        return self.r == o.r and self.g == o.g and self.b == o.b
         
    def __sub__(self, o): 
        if isinstance(o, Color):
            pass
        try:
            return RGB(max(self.r - o, 0), max(self.g - o, 0), max(self.b - o, 0)) 
        except:
            raise('Invalid subtraction')

    def __repr__(self):
        if self.a:
            return 'rgb(%d,%d,%d,%d)' % (self.r,self.g,self.b,self.a)
        else:
            return 'rgb(%d,%d,%d)' % (self.r,self.g,self.b)

class HEX(RGB):

    def __init__(self, str_repr):
        if str_repr[0] == '#': str_repr = str_repr[1:]
        self.r = int(str_repr[0:2], 16)
        self.g = int(str_repr[2:4], 16)
        self.b = int(str_repr[4:6], 16)
        if len(str_repr) > 6: self.a = int(str_repr, 16)
        else: self.a = 0

    def __str__(self):
        if self.a:
            return 'hex(#%02x%02x%02x%02x)' % (self.r,self.g,self.b,self.a)
        else:
            return 'hex(#%02x%02x%02x)' % (self.r,self.g,self.b)

class HSV(Color):

    def __init__(self, h, s, v, radians=False):
        self.h = h
        assert 0 <= h < 360
        self.s = s
        self.v = v
        self.radians = radians

    def __radd__(self, o):
        return self.__add__(o)

    def __add__(self, o):
        if isinstance(o, RGB):
            return o + self 
        
    def get_dimensions(self):
        return [self.h,self.s,self.v]

    def to(self, colorspace):
        if not colorspace or isinstance(self, colorspace): return self
        if colorspace == RGB:
            C = self.v * self.s
            X = C * (1 - abs((self.h/60) % 2 - 1))
            m = self.v - C
            if     0 <= self.h <  60:
                _RGB = (C,X,0)
            elif  60 <= self.h < 120:
                _RGB = (X,C,0)
            elif 120 <= self.h < 180:
                _RGB = (0,C,X)
            elif 180 <= self.h < 240:
                _RGB = (0,X,C)
            elif 240 <= self.h < 300:
                _RGB = (X,0,C)
            elif 300 <= self.h < 360:
                _RGB = (C,0,X)
            rgb = RGB((_RGB[0]+m), (_RGB[1]+m)*255, (_RGB[2]+m)*255)
            assert 0 <= rgb.r <= 255
            assert 0 <= rgb.g <= 255
            assert 0 <= rgb.b <= 255
            return rgb
        super().to(colorspace)

    def __repr__(self):
        return 'hsv(%f,%f,%d)' % (self.h,self.s,self.v)
