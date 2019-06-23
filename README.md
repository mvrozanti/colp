# colp
![](https://i.imgur.com/GT5hJhn.png)

The color processor

# Supported Color Models
- [ ] CMY[K]
- [ ] RGB/RGBA
  [ ] - [red|green|blue|r|g|b]
- [ ] HSV=HSB=HSI=HSD
- [ ] HEX TRIPLET/QUADRUPLET
- [ ] HSL
- [ ] [CIE]LAB
- [ ] YCbCr
- [ ] YIQ

# Definitions

A `Color` is the only kind of object there is in `colp`. Intuitively, it is an abstract object. A `Color` can be _transformed_.
Numbers can be expressed as floats and integers because of the difference in color models.

# Color Components
- Component value access is made by `x.y` where `x` is the `Color` in the target Color Model and `y` is the component or component abbreviation for that model

# Constants
- See resource no. 2 (X11 + HTML 4.01 spec)

# Member Functions
A member function call always appears as `Color.function` 

## Transformative Operations
- lighten/darken
- brightness (without arguments)
- rotate (depends on floating argument (what interval?))
- redder/greener/bluer (with arguments or without arguments, with the latter minimally dislocating the Color in the RGB Color Space)

## Descriptive Operations
- brightness (without arguments)
- angle (without arguments (what interval?))

## Custom Functions
```


```

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


# Doubts
- Case-sensitive?
- Comments (`;`|`%`|`#`)
- String delimiter and escaping
- Color Space boundaries

# Real use-cases
```
> rgb(10,20,30).a == 0
True
> rgb(10,20,30).r
10
> rgb(10,20,30,40).a
40
> rgb(10,20,30).red
10
> rgb(10,20,30).r + 1
11
> rgb(10,20,30).r + 1
11
> rotate(rgb(10,20,30), -1.)
rgb(x,y,z)
> hex(rgb(255,0,0))
hex(#ff0000)
> rgb('#ff0000')
rgb(255,0,0)
> rgb(1,0,0) + rgb(0,1,0)
rgb(1,1,0)
> hsv('#ff0000')
hsv(0,100.0,100.0)
> saturate('#ff0000', )
```

### Access Component in Color
- Example: `#c01001.red` returns the number associated with the RED component in the the `Color`'s RGB model

```

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
