# colp 
[![Build Status](https://travis-ci.com/mvrozanti/colp.svg?token=Hrxne9dbhCC141HWAM1p&branch=colpy)](https://travis-ci.com/mvrozanti/colp)

The color processor 


![](https://i.imgur.com/WIAAZlR.png)

# Constants
- See resource no. 2 (X11 + HTML 4.01 spec)

## Transformative Operations
- lighten/darken
- brightness (without arguments)
- rotate (depends on floating argument (what interval?))
- redder/greener/bluer (with arguments or without arguments, with the latter minimally dislocating the Color in the RGB Color Space)

## Descriptive Operations
- brightness (without arguments)
- angle (without arguments (what interval?))

# Basic Color Operators
|Status|Operator|
|------|--------|
|✓     |  `-`   |
|✓     |  `+`   |
|      |  `*`   |
|      |  `/`   |
|      |  `//`  |
|      |  `!`   |
|      |  `~`   |
|      |  `^`   |
|      |  `**`  |

# Example Usage

```
$ colp 'a=RGB(1,1,1)' # optionally load a color to memory

┌─┐┌─┐┬  ┬─┐
│  │ ││  │─┘
└─┘┘─┘┆─┘┆   the color processor

>>> a = a.brighter() # increment all channels
>>> a
RGB(2, 2, 2)
>>> a = a.redder() # single-channel increment
>>> a
RGB(3, 2, 2)
>>> a = a.rotate(3.) # rotate in HSV space
>>> a
RGB(2, 1, 1)
>>> by_name('red') == a # compare
False
>>> by_name('red') == RGB(255,0,0)
True
>>> -a # invert color
RGB(252, 253, 253)
>>>
```

# Good Resources
- [HSV Color Specification](https://stat.ethz.ch/R-manual/R-devel/library/grDevices/html/hsv.html)
- [X11 + HTML 4.01 spec](https://en.wikipedia.org/wiki/Web_colors)
- [Color Models vs Color Spaces](https://programmingdesignsystems.com/color/color-models-and-color-spaces/index.html)
- [rapidtables.com color converter (including formulas)](https://www.rapidtables.com/convert/color/index.html)
- [colormath-basics](http://www.laurenscorijn.com/articles/colormath-basics)


|Status|Supported Color Models|
|------|---------------|
|✓     |      RGB/RGBA/HEX:    |
|      |<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/RGB_Cube_Show_lowgamma_cutout_a.png/1280px-RGB_Cube_Show_lowgamma_cutout_a.png" alt="drawing" width="400"/>|
|✓     |      HSV=HSB=HSI=HSD: |
|      |<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/HSV_color_solid_cylinder_saturation_gray.png/1280px-HSV_color_solid_cylinder_saturation_gray.png" alt="drawing" width="400"/>|
|[ ]   | HSL:|
|      |<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/HSL_color_solid_cylinder_saturation_gray.png/1280px-HSL_color_solid_cylinder_saturation_gray.png" alt="drawing" width="400"/>|
|[ ]   |  CMY[K]|
|      | <img src="https://i.imgur.com//Bwi2zUi.png" alt="drawing" width="400"/>|
|[ ]   | [CIE]LAB|
|      | <img src="https://upload.wikimedia.org/wikipedia/commons/0/06/CIELAB_color_space_top_view.png" alt="drawing" width="400"/>|
|[ ]   |  YCbCr |
|      | <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/YCbCr-CbCr_Scaled_Y50.png/1024px-YCbCr-CbCr_Scaled_Y50.png" alt="drawing" width="400"/>|
|[ ]   | YIQ|
|      |<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/YIQ_IQ_plane.svg/1024px-YIQ_IQ_plane.svg.png" alt="drawing" width="400"/>|
|[ ]   | YUV|
|      |<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/YUV_UV_plane.svg/1024px-YUV_UV_plane.svg.png" alt="drawing" width="400"/>|

