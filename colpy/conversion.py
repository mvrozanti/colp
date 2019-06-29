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
    def get_dimensions(self, normalise=False):
        pass

    @abstractmethod
    def to(self, colorspace):
        import inspect
        if inspect.isclass(colorspace) and issubclass(colorspace, Color):
            clone = copy.copy(self)
            clone.__class__ = colorspace
        else:
            raise('Invalid colorspace')

    def brightness(self, normalised=True):
        if normalised:
            return sum(self.get_dimensions()) / len(self.get_dimensions())

    def darkness(self, normalised=True):
        if normalised:
            return 1 - self.brightness()

    def brighter(self):
        o = copy.copy(self)
        return o + 1

    def darker(self):
        o = copy.copy(self)
        return o - 1

    def _inc_channel(self, chan_ix, factor=1):
        o = copy.copy(self).to(RGB)
        channels = o.get_dimensions()
        channels[chan_ix] += factor
        channels[chan_ix] %= 255
        return RGB(*channels).to(self.__class__) 

    def redder(self, factor=1):
        return self._inc_channel(0, factor=factor)

    def greener(self, factor=1):
        return self._inc_channel(1, factor=factor)

    def bluer(self, factor=1):
        return self._inc_channel(2, factor=factor)

    def rotate(self, angle=1.):
        o = self
        original_class = o.__class__
        if not isinstance(o, HSV):
            o = self.to(HSV)
        rotated_hsv = o.rotate(angle)
        return rotated_hsv.to(original_class)

    def __neg__(self):
        o = copy.copy(self).to(RGB)
        channels = o.get_dimensions()
        for i in len(channels):
            channels[i] = 255 - channels[i]
        return RGB(*channels).to(self.__class__)

    def __eq__(self, other):
        if other is None: return False
        if isinstance(other, self.__class__) or isinstance(self, other.__class__):
            return self.get_dimensions() == other.get_dimensions()
        else:
            return other.to(self.__class__) == self

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

    def __hash__(self):
        r,g,b = self.get_dimensions()
        rgb = r
        rgb = (rgb << 8) + g
        rgb = (rgb << 8) + b
        return rgb

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
        if colorspace is HEX:
            return HEX('#%02x%02x%02x' % tuple(self.get_dimensions()))

    def __neg__(self):
        o = copy.copy(self)
        o.r = 1.0 - o.r
        o.g = 1.0 - o.g
        o.b = 1.0 - o.b
        return o

    def __add__(self, o, normalise=False): 
        if isinstance(o, Color):
            o = o.to(RGB)
            rr = o.r + self.r
            rg = o.g + self.g
            rb = o.b + self.b
            return RGB(rr,rg,rb) 
        if isinstance(o, float) and normalise:
            if 0 <= o <= 1:
                return RGB(max(self.r + o, 0), \
                        max(self.g + o, 0), \
                        max(self.b + o, 0))
        elif isinstance(o, int) and not normalise:
            rgb = self.get_dimensions(normalise=False)
            for i in range(len(rgb)):
                rgb[i] += o
            return RGB(*rgb)
        raise('Invalid addition')
         
    def __sub__(self, o): 
        if isinstance(o, Color):
            o = copy.copy(o)
            if isinstance(o, HSV):
                o = o.to(RGB)
            o.r = -o.r
            o.g = -o.g
            o.b = -o.b
            o.a = -o.a
            return self.__add__(o)
        elif isinstance(o, (int,float)):
            return self.__add__(-o)

class HEX(RGB):

    def __init__(self, str_repr):
        if str_repr[0] == '#': str_repr = str_repr[1:]
        ws = int(len(str_repr) == 3) + 1 # web-safe factor
        self.r = int(str_repr[0//ws:2//ws] * ws, 16) / 255
        self.g = int(str_repr[2//ws:4//ws] * ws, 16) / 255
        self.b = int(str_repr[4//ws:6//ws] * ws, 16) / 255
        self.a = int(str_repr[6//ws:8//ws] * ws, 16) / 255 if len(str_repr) > 6 else 0

    def __repr__(self):
        return 'HEX(#%02x%02x%02x)' % tuple(self.get_dimensions(normalise=False))

class HSV(Color):

    def __init__(self, h, s, v, radians=False):
        self.h = h
        self.s = s
        self.v = v
        if not detect_normalised([h,s,v]):
            self.h %= 360
            self.h /= 360
            self.s /= 100
            self.v /= 100
        self.radians = radians

    def __radd__(self, o):
        return self.__add__(o)

    def __add__(self, o):
        if isinstance(o, RGB):
            return o + self 

    def __hash__(self):
        return self.to(RGB).__hash__()

    def __eq__(self, o):
        if isinstance(o, RGB):
            return self.to(RGB) == o

    def rotate(self, angle=1., radians=False):
        h,s,v = self.get_dimensions(normalise=False)
        return HSV(h+angle, s, v)
        
    def get_dimensions(self, normalise=False):
        if normalise:
            return [self.h,self.s,self.v]
        else:
            return [int(self.h*360), int(self.s*100), int(self.v*100)]

    def to(self, colorspace):
        if not colorspace or isinstance(self, colorspace): return self
        if issubclass(colorspace, RGB):
            h,s,v = self.get_dimensions(normalise=True)
            rgb = RGB(*colorsys.hsv_to_rgb(h,s,v*255))
            if colorspace == HEX: return rgb.to(HEX)
            else: return rgb
            # import code
            # code.interact(local=globals().update(locals()) or globals())
            # h *= 360
            # C = v * s
            # X = C * (1 - abs((h/60) % 2 - 1))
            # m = v - C
            # if     0 <= h <  60:
            #     _RGB = (C,X,0)
            # elif  60 <= h < 120:
            #     _RGB = (X,C,0)
            # elif 120 <= h < 180:
            #     _RGB = (0,C,X)
            # elif 180 <= h < 240:
            #     _RGB = (0,X,C)
            # elif 240 <= h < 300:
            #     _RGB = (X,0,C)
            # elif 300 <= h < 360:
            #     _RGB = (C,0,X)
            # rgb = RGB((_RGB[0]+m), (_RGB[1]+m)*255, (_RGB[2]+m)*255)
            # return rgb.to(HEX) if colorspace == HEX else rgb
        super().to(colorspace)

def by_name(name=None):
    html_spec = {      
            'white'                             : HEX('#FFFFFF'),
            'silver'                            : HEX('#C0C0C0'),
            'gray'                              : HEX('#808080'),
            'black'                             : HEX('#000000'),
            'red'                               : HEX('#FF0000'),
            'maroon'                            : HEX('#800000'),
            'yellow'                            : HEX('#FFFF00'),
            'olive'                             : HEX('#808000'),
            'lime'                              : HEX('#00FF00'),
            'green'                             : HEX('#008000'),
            'aqua'                              : HEX('#00FFFF'),
            'teal'                              : HEX('#008080'),
            'blue'                              : HEX('#0000FF'),
            'navy'                              : HEX('#000080'),
            'fuchsia'                           : HEX('#FF00FF'),
            'magenta'                           : HEX('#FF00FF'),
            'purple'                            : HEX('#800080'),
            }
    x11_spec = {
            # Pink colors
            'pink'                              : RGB(255, 192, 203),
            'lightpink'                         : RGB(255, 182, 193),
            'hotpink'                           : RGB(255, 105, 180),
            'deeppink'                          : RGB(255,  20, 147),
            'palevioletred'                     : RGB(219, 112, 147),
            'mediumvioletred'                   : RGB(199,  21, 133),
            # red colors
            'lightsalmon'                       : RGB(255, 160, 122),
            'salmon'                            : RGB(250, 128, 114),
            'darksalmon'                        : RGB(233, 150, 122),
            'lightcoral'                        : RGB(240, 128, 128),
            'indianred'                         : RGB(205,  92,  92),
            'crimson'                           : RGB(220,  20,  60),
            'firebrick'                         : RGB(178,  34,  34),
            'darkred'                           : RGB(139,   0,   0),
            'red'                               : RGB(255,   0,   0),
            # orange colors
            'orangered'                         : RGB(255,  69,   0),
            'tomato'                            : RGB(255,  99,  71),
            'coral'                             : RGB(255, 127,  80),
            'darkorange'                        : RGB(255, 140,   0),
            'orange'                            : RGB(255, 165,   0),
            # yellow colors                                    
            'yellow'                            : RGB(255, 255,   0),
            'lightyellow'                       : RGB(255, 255, 224),
            'lemonchiffon'                      : RGB(255, 250, 205),
            'lightgoldenrodyellow'              : RGB(250, 250, 210),
            'papayawhip'                        : RGB(255, 239, 213),
            'moccasin'                          : RGB(255, 228, 181),
            'peachpuff'                         : RGB(255, 218, 185),
            'palegoldenrod'                     : RGB(238, 232, 170),
            'khaki'                             : RGB(240, 230, 140),
            'darkkhaki'                         : RGB(189, 183, 107),
            'gold'                              : RGB(255, 215,   0),
            # brown colors                                      
            'cornsilk'                          : RGB(255, 248, 220),
            'blanchedalmond'                    : RGB(255, 235, 205),
            'bisque'                            : RGB(255, 228, 196),
            'navajowhite'                       : RGB(255, 222, 173),
            'wheat'                             : RGB(245, 222, 179),
            'burlywood'                         : RGB(222, 184, 135),
            'tan'                               : RGB(210, 180, 140),
            'rosybrown'                         : RGB(188, 143, 143),
            'sandybrown'                        : RGB(244, 164,  96),
            'goldenrod'                         : RGB(218, 165,  32),
            'darkgoldenrod'                     : RGB(184, 134,  11),
            'peru'                              : RGB(205, 133,  63),
            'chocolate'                         : RGB(210, 105,  30),
            'saddlebrown'                       : RGB(139,  69,  19),
            'sienna'                            : RGB(160,  82,  45),
            'brown'                             : RGB(165,  42,  42),
            'maroon'                            : RGB(128,   0,   0),
            # green colors                                      
            'darkolivegreen'                    : RGB(85 , 107,  47),
            'olive'                             : RGB(128, 128,   0),
            'olivedrab'                         : RGB(107, 142,  35),
            'yellowgreen'                       : RGB(154, 205,  50),
            'limegreen'                         : RGB(50 , 205,  50),
            'lime'                              : RGB(0  , 255,   0),
            'lawngreen'                         : RGB(124, 252,   0),
            'chartreuse'                        : RGB(127, 255,   0),
            'greenyellow'                       : RGB(173, 255,  47),
            'springgreen'                       : RGB(0  , 255, 127),
            'mediumspringgreen'                 : RGB(0  , 250, 154),
            'lightgreen'                        : RGB(144, 238, 144),
            'palegreen'                         : RGB(152, 251, 152),
            'darkseagreen'                      : RGB(143, 188, 143),
            'mediumaquamarine'                  : RGB(102, 205, 170),
            'mediumseagreen'                    : RGB(60 , 179, 113),
            'seagreen'                          : RGB(46 , 139,  87),
            'forestgreen'                       : RGB(34 , 139,  34),
            'green'                             : RGB(0  , 128,   0),
            'darkgreen'                         : RGB(0  , 100,   0),
            # cyan colors
            'aqua'                              : RGB(0  , 255, 255),
            'cyan'                              : RGB(0  , 255, 255),
            'lightcyan'                         : RGB(224, 255, 255),
            'paleturquoise'                     : RGB(175, 238, 238),
            'aquamarine'                        : RGB(127, 255, 212),
            'turquoise'                         : RGB(64 , 224, 208),
            'mediumturquoise'                   : RGB(72 , 209, 204),
            'darkturquoise'                     : RGB(0  , 206, 209),
            'lightseagreen'                     : RGB(32 , 178, 170),
            'cadetblue'                         : RGB(95 , 158, 160),
            'darkcyan'                          : RGB(0  , 139, 139),
            'teal'                              : RGB(0  , 128, 128),
            # blue colors
            'lightsteelblue'                    : RGB(176, 196, 222),
            'powderblue'                        : RGB(176, 224, 230),
            'lightblue'                         : RGB(173, 216, 230),
            'skyblue'                           : RGB(135, 206, 235),
            'lightskyblue'                      : RGB(135, 206, 250),
            'deepskyblue'                       : RGB(0  , 191, 255),
            'dodgerblue'                        : RGB(30 , 144, 255),
            'cornflowerblue'                    : RGB(100, 149, 237),
            'steelblue'                         : RGB(70 , 130, 180),
            'royalblue'                         : RGB(65 , 105, 225),
            'blue'                              : RGB(0  , 0  , 255),
            'mediumblue'                        : RGB(0  , 0  , 205),
            'darkblue'                          : RGB(0  , 0  , 139),
            'navy'                              : RGB(0  , 0  , 128),
            'midnightblue'                      : RGB(25 , 25 , 112),
            # purple, violet, and magenta colors
            'lavender'                          : RGB(230, 230, 250),
            'thistle'                           : RGB(216, 191, 216),
            'plum'                              : RGB(221, 160, 221),
            'violet'                            : RGB(238, 130, 238),
            'orchid'                            : RGB(218, 112, 214),
            'fuchsia'                           : RGB(255,   0, 255),
            'magenta'                           : RGB(255,   0, 255),
            'mediumorchid'                      : RGB(186,  85, 211),
            'mediumpurple'                      : RGB(147, 112, 219),
            'blueviolet'                        : RGB(138,  43, 226),
            'darkviolet'                        : RGB(148,   0, 211),
            'darkorchid'                        : RGB(153,  50, 204),
            'darkmagenta'                       : RGB(139,   0, 139),
            'purple'                            : RGB(128,   0, 128),
            'indigo'                            : RGB(75 ,   0, 130),
            'darkslateblue'                     : RGB(72 ,  61, 139),
            'slateblue'                         : RGB(106,  90, 205),
            'mediumslateblue'                   : RGB(123, 104, 238),
            # white colors
            'white'                             : RGB(255, 255, 255),
            'snow'                              : RGB(255, 250, 250),
            'honeydew'                          : RGB(240, 255, 240),
            'mintcream'                         : RGB(245, 255, 250),
            'azure'                             : RGB(240, 255, 255),
            'aliceblue'                         : RGB(240, 248, 255),
            'ghostwhite'                        : RGB(248, 248, 255),
            'whitesmoke'                        : RGB(245, 245, 245),
            'seashell'                          : RGB(255, 245, 238),
            'beige'                             : RGB(245, 245, 220),
            'oldlace'                           : RGB(253, 245, 230),
            'floralwhite'                       : RGB(255, 250, 240),
            'ivory'                             : RGB(255, 255, 240),
            'antiquewhite'                      : RGB(250, 235, 215),
            'linen'                             : RGB(250, 240, 230),
            'lavenderblush'                     : RGB(255, 240, 245),
            'mistyrose'                         : RGB(255, 228, 225),
            # gray and black colors
            'gainsboro'                         : RGB(220, 220, 220),
            'lightgray'                         : RGB(211, 211, 211),
            'silver'                            : RGB(192, 192, 192),
            'darkgray'                          : RGB(169, 169, 169),
            'gray'                              : RGB(128, 128, 128),
            'dimgray'                           : RGB(105, 105, 105),
            'lightslategray'                    : RGB(119, 136, 153),
            'slategray'                         : RGB(112, 128, 144),
            'darkslategray'                     : RGB(47 , 79 , 79 ),
            'black'                             : RGB(0  , 0  , 0  ),
            }
    le_dict = dict(x11_spec, **html_spec)
    if name: return le_dict[name.lower()]
    else: return le_dict
