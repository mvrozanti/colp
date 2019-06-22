# colp
The color processor

# Supported Color models
- CMY[K]
- RGB/RGBA
- HEX TRIPLET
- HSV=HSB=HSI=HSD
- HSL
- [CIE]LAB
- YCbCr
- YIQ

# Color Components
- Component value access is made by `x[y]` where `x` is the color in the target color model and `y` is the component abbreviation for that model
  - Example: `#ffeedd[R]` returns the number associated with the RED component in the RGB model

# Constants
- See resource no. 2 ()

# Functions
- lighten

# Basic operations
- + sum 
- - 

# Flags
- default output color model

# Extra Resources
- [hsv](https://stat.ethz.ch/R-manual/R-devel/library/grDevices/html/hsv.html)
- [X11 + HTML 4.01 spec](https://en.wikipedia.org/wiki/Web_colors)
