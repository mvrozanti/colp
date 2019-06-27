#!/usr/bin/env python
from abc import ABC, abstractmethod
import copy
import colorsys

def detect_normalised(normalised):
    return all([type(n) == float and 0 <= n <= 1 for n in normalised])

class Color(ABC):

    def __radd__(self, o):
        return self.__add__(o);

    def __rsub__(self, o):
        return self.__sub__(o);

    @abstractmethod
    def get_dimensions(self, normalised=False):
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

    def __eq__(self, other):
        if type(other) == type(self):
            return self.get_dimensions() == other.get_dimensions()

    def __repr__(self):
        return self.__class__.__name__  + str(tuple(self.get_dimensions()))

class RGB(Color):

    def __init__(self, r, g, b, a=0):
        self.r = r;
        self.g = g;
        self.b = b;
        self.a = a;
        if not detect_normalised([r,g,b]):
            self.r /= 255;
            self.g /= 255;
            self.b /= 255;
        if not detect_normalised([a]):
            self.a /= 255;

    def get_dimensions(self, normalise=False):
        if normalise:
            return [self.r,self.g,self.b] + ([self.a] if self.a else [])
        else:
            return [int(255*self.r),int(255*self.g),int(255*self.b)] + \
                    ([int(255*self.a)] if self.a else [])

    def to(self, colorspace, normalise=False):
        if not colorspace or isinstance(self, colorspace):
            return self
        if colorspace is HSV:
            hsv_dimensions = colorsys.rgb_to_hsv(*self.get_dimensions(normalise=True))
            return HSV(*hsv_dimensions)

    def __add__(self, o): 
        if isinstance(o, Color):
            o = o.to(RGB)
            rr = o.r + self.r
            rg = o.g + self.g
            rb = o.b + self.b
            return RGB(rr,rg,rb) 
        if isinstance(o, (int, float)):
            return RGB(max(self.r + o, 0), \
                    max(self.g + o, 0), \
                    max(self.b + o, 0))
        raise('Invalid addition')
         
    def __sub__(self, o): 
        if isinstance(o, Color):
            pass
        try:
            return RGB(max(self.r - o, 0), max(self.g - o, 0), max(self.b - o, 0)) 
        except:
            raise('Invalid subtraction')

class HEX(RGB):

    def __init__(self, str_repr):
        if str_repr[0] == '#': str_repr = str_repr[1:]
        self.r = int(str_repr[0:2], 16) / 255
        self.g = int(str_repr[2:4], 16) / 255
        self.b = int(str_repr[4:6], 16) / 255
        self.a = int(str_repr[6:8], 16) / 255 if len(str_repr) > 6 else 0

    def __repr__(self):
        return 'HEX(#%02x%02x%02x)' % (self.get_dimensions())

class HSV(Color):

    def __init__(self, h, s, v, radians=False):
        self.h = h
        self.s = s
        self.v = v
        if not detect_normalised([h,s,v]):
            self.h /= 360
            self.s /= 100
            self.v /= 100
        self.radians = radians

    def __radd__(self, o):
        return self.__add__(o)

    def __add__(self, o):
        if isinstance(o, RGB):
            return o + self 
        
    def get_dimensions(self, normalise=False):
        if normalise:
            return [self.h,self.s,self.v]
        else:
            return [int(self.h*360), int(self.s*100), int(self.v*100)]

    def to(self, colorspace):
        if not colorspace or isinstance(self, colorspace): return self
        if colorspace == RGB:
            h,s,v = self.get_dimensions(normalise=True)
            h *= 360
            C = v * s
            X = C * (1 - abs((h/60) % 2 - 1))
            m = v - C
            if     0 <= h <  60:
                _RGB = (C,X,0)
            elif  60 <= h < 120:
                _RGB = (X,C,0)
            elif 120 <= h < 180:
                _RGB = (0,C,X)
            elif 180 <= h < 240:
                _RGB = (0,X,C)
            elif 240 <= h < 300:
                _RGB = (X,0,C)
            elif 300 <= h < 360:
                _RGB = (C,0,X)
            rgb = RGB((_RGB[0]+m), (_RGB[1]+m)*255, (_RGB[2]+m)*255)
            assert 0 <= rgb.r <= 255
            assert 0 <= rgb.g <= 255
            assert 0 <= rgb.b <= 255
            return rgb
        super().to(colorspace)
