# colp 
[![Build Status](https://travis-ci.com/mvrozanti/colp.svg?token=Hrxne9dbhCC141HWAM1p&branch=master)](https://travis-ci.com/mvrozanti/colp)
[![PyPI](https://img.shields.io/pypi/v/colp.svg)](https://pypi.org/project/colp/)


The color processor 


![](https://i.imgur.com/WIAAZlR.png)


### Objective

This tool is inspired on various processing tools such as awk, sed and imagemagick. There is no processing library for single color operations, be it interactively or not. 
`colp` attempts to solve that. It supports a number of color models (specified later in this README). The goal is to have the ability to script and automate any algorithmic color transformation.

### Installation

`pip install colp`

### Example Usage

#### Interactively operate on colors

```
$ colp 'a=RGB(1,1,1)' # optionally load a color to memory

┌─┐┌─┐┬  ┬─┐
│  │ ││  │─┘
└─┘┘─┘┆─┘┆   the color processor

> a = a.redder()                  # single channel increment
> a
RGB(2, 1, 1)
> a = a + 1                       # all channels increment
> a
RGB(3, 2, 2)
> lightgoldenrodyellow            # X11/HTML constants
RGB(250, 250, 210)
> -a                              # inversion 
RGB(252, 253, 253)
> red.rotate(180) == -red == cyan # rotate hue in HSV space
True
> skyblue ; skyblue.brighter()    # brighter in HSV space
RGB(135, 206, 235)
RGB(136, 208, 237)

> a_set_of_colors = [RGB(25,25,112), HSV(186,23,90), plum, orchid, fuchsia, HEX('#800080')]
> a_set_of_colors.sort()
> a_set_of_colors
[RGB(25, 25, 112), HEX('#800080'), RGB(218, 112, 214), RGB(221, 160, 221), HSV(186, 23, 90), HEX('#ff00ff')]
>
> cursor = RGB(0,0,0)             # define your own custom functions
> def pop_and_turn(x):
>       if x: 
>             x = x.redder() * 255
>       return x.rotate(30)
> 
> for i in range(10):
>       cursor = pop_and_turn(cursor)
>       print(cursor)
>
RGB(255, 0, 127)
RGB(255, 0, 0)
RGB(255, 127, 0)
RGB(255, 255, 0)
RGB(127, 255, 0)
RGB(0, 255, 0)
RGB(0, 255, 127)
RGB(0, 255, 255)
RGB(0, 127, 255)
RGB(0, 0, 255)

```

#### Or pipe commands in

```
$ echo "HEX('#ff0000').rotate(15.).to(RGB)" | colp

RGB(255, 63, 0)

```

#### Usage from Python script

```
from colp import *
print(RGB(1,2,3).to(HEX))

```

outputs:

```
HEX('#010203')
```

### Formal Parameters

```
usage: colp [-h] [-n] [-v VISUALIZER] [-s] [-S] [-l SCRIPT_FILE]
            [VAR [VAR ...]]

Color Processor

positional arguments:
  VAR                   arbitrary python code execution

optional arguments:
  -h, --help            show this help message and exit
  -n, --no-banner       don't show banner on interactive mode
  -v VISUALIZER, --visualizer VISUALIZER
                        visualize current color processed
  -s, --simple-mode     css-compliant output
  -S, --scripting-mode  colp script output
  -l SCRIPT_FILE, --load-script SCRIPT_FILE
                        load script from file or stdin
```

### Basic Color Operators
|    |    |    |     |
|----|----|----|-----|
|`-` |`+` |`*` |`/`  |
|`//`|`~` |`^` |`|`  |
|`&` |`**`|`%` |`>>` | 
|`<<`|`<` |`>` |`<=` |
|`>=`|`==`|`is`|`not`|

### Named Constants
- [HTML 4.01 specification](https://en.wikipedia.org/wiki/Web_colors#HTML_color_names)
- [X11 color names](https://en.wikipedia.org/wiki/Web_colors#)

### Good Resources
- [HSV Color Specification](https://stat.ethz.ch/R-manual/R-devel/library/grDevices/html/hsv.html)
- [Color Models vs Color Spaces](https://programmingdesignsystems.com/color/color-models-and-color-spaces/index.html)
- [rapidtables.com color converter (including formulas)](https://www.rapidtables.com/convert/color/index.html)
- [colormath-basics](http://www.laurenscorijn.com/articles/colormath-basics)


### Supported Color Models

|                      |                      |
|----------------------|----------------------|
|  ✓  RGB/RGBA/HEX:    | ✓ HSV=HSB=HSI=HSD:   |
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/RGB_Cube_Show_lowgamma_cutout_a.png/1280px-RGB_Cube_Show_lowgamma_cutout_a.png" alt="drawing" width="300"/>|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/HSV_color_solid_cylinder_saturation_gray.png/1280px-HSV_color_solid_cylinder_saturation_gray.png" alt="drawing" width="300"/>|
| HSL:                 | CMY[K]               |
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/HSL_color_solid_cylinder_saturation_gray.png/1280px-HSL_color_solid_cylinder_saturation_gray.png" alt="drawing" width="300"/>|<img src="https://i.imgur.com//Bwi2zUi.png" alt="drawing" width="300"/>|
| [CIE]LAB             | YCbCr                |
| <img src="https://upload.wikimedia.org/wikipedia/commons/0/06/CIELAB_color_space_top_view.png" alt="drawing" width="300"/>|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/YCbCr-CbCr_Scaled_Y50.png/1024px-YCbCr-CbCr_Scaled_Y50.png" alt="drawing" width="300"/>|
| YIQ                  | YUV                  |
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/YIQ_IQ_plane.svg/1024px-YIQ_IQ_plane.svg.png" alt="drawing" width="300"/>|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/YUV_UV_plane.svg/1024px-YUV_UV_plane.svg.png" alt="drawing" width="300"/>|

### Contributing

- There's definitely some room for automating CSS-file editing.
