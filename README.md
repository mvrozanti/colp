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

### Image input/output

# Conversion
Any one `Color` can be represented in any Color Model.

```
> rotate(rgb(10,20,30))
rgb(x,y,z)
> hex(rgb(255,0,0))
hex(#ff0000)
> rgb('#ff0000')
rgb(255,0,0)
> hsv('#ff0000')
hsv(0,100.0,100.0)
```

# Basic Color Operators
`-`,`+`,`*`,`//`,`/`,`!`,`~`,`^`,'|',`**`

# Doubts
- Case-sensitive?
- Comments (`;`|`%`|`#`)
- String delimiter and escaping
- Color Space boundaries

# Real use-cases
```
> rgb(10,20,30).a == 0 # comparisons
True
> rgb(10,20,30).r # accessing components
10
> rgb(10,20,30).r + 1 # simple integer operations
11
> rotate(rgb(10,20,30), -1.) # a built-in function
rgb(x,y,z)
> hex(rgb(255,0,0)) # conversions
hex('#ff0000')
> hsv(hex('#ff0000'))
hsv(0,100.0,100.0)
> rgb(hex('#ff0000')) 
rgb(255,0,0)
> rgb(1,0,0) + rgb(0,1,0) # sum colors
rgb(1,1,0)
> saturate(rgb(3,2,1), 1) # another built-in
rgb(4,3,2)
```

# Flags
- default output color model? 
- Modes
  - interpret
  - transform

# Good Resources
- [HSV Color Specification](https://stat.ethz.ch/R-manual/R-devel/library/grDevices/html/hsv.html)
- [X11 + HTML 4.01 spec](https://en.wikipedia.org/wiki/Web_colors)
- [Color Models vs Color Spaces](https://programmingdesignsystems.com/color/color-models-and-color-spaces/index.html)
- [rapidtables.com color converter (including formulas)](https://www.rapidtables.com/convert/color/index.html)
- [colormath-basics](http://www.laurenscorijn.com/articles/colormath-basics)

# Supported Color Models
- [X] RGB/RGBA/HEX
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/RGB_Cube_Show_lowgamma_cutout_a.png/1280px-RGB_Cube_Show_lowgamma_cutout_a.png" alt="drawing" width="400"/>

- [X] HSV=HSB=HSI=HSD
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/HSV_color_solid_cylinder_saturation_gray.png/1280px-HSV_color_solid_cylinder_saturation_gray.png" alt="drawing" width="400"/>

- [ ] HSL
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/HSL_color_solid_cylinder_saturation_gray.png/1280px-HSL_color_solid_cylinder_saturation_gray.png" alt="drawing" width="400"/>

- [ ] CMY[K]
<img src="https://i.imgur.com//Bwi2zUi.png" alt="drawing" width="400"/>

- [ ] [CIE]LAB
<img src="https://upload.wikimedia.org/wikipedia/commons/0/06/CIELAB_color_space_top_view.png" alt="drawing" width="400"/>

- [ ] YCbCr
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/YCbCr-CbCr_Scaled_Y50.png/1024px-YCbCr-CbCr_Scaled_Y50.png" alt="drawing" width="400"/>

- [ ] YIQ
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/YIQ_IQ_plane.svg/1024px-YIQ_IQ_plane.svg.png" alt="drawing" width="400"/>

- [ ] YUV
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/YUV_UV_plane.svg/1024px-YUV_UV_plane.svg.png" alt="drawing" width="400"/>

