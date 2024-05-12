# Colors
Trinidad = rgb(201, 70, 38)
TrinidadLight = rgb(237, 111, 80)

Gray1 = rgb(67, 67, 67)

# Console
Polygon(
    57, 125, 
    343, 125,
    369, 285,
    32, 285,
    
    fill = Gray1,
    border = 'black',
    borderWidth = 1
)

Polygon(
    64, 125, 
    334, 125,
    360, 285,
    40, 285
)

Polygon(
    45, 253,
    355, 253,
    360, 285,
    40, 285,
    
    fill = gradient(TrinidadLight, Trinidad, start = 'top'),
    border = 'black',
    borderWidth = 1
)

# Logo
Line(
    176, # x1
    165, # y1
    176,
    141,
    
    fill = 'white',
    lineWidth = 2
)

Polygon(
    172, 141,
    173, 141,
    173, 153,
    170, 160,
    166, 164,
    159, 167,
    159, 164,
    165, 161,
    169, 157,
    171, 150,
    
    fill = 'white'
)

Polygon(
    179, 141,
    180, 141,
    182, 150,
    180, 153,
    183, 157,
    182, 160,
    187, 161,
    186, 164,
    193, 164,
    193, 167,
    
    fill = 'white'
)



Label(
    'ATARI',
    174, 172,
    
    fill = 'white',
    font = 'arial',
    bold = True
)

# Gradient Trim
Polygon(
    64, 125,
    334, 125,
    336, 141,
    62, 141,
    
    fill = gradient('gray', 'black', start = 'top'),
    border = 'black',
    borderWidth = 1
)

# Buttons

# Power Button
Circle(
    95, 152,
    12,
    
    fill = gradient('red', 'darkRed'),
    
    border = rgb(166, 28, 0),
    borderWidth = 1
)

Label(
    'POWER',
    95, 134,
    
    fill = 'white',
    size = 7,
)

# Reset Button
Circle(
    132, 152,
    12,
    
    fill = gradient('orange', 'darkOrange'),
    
    border = rgb(180, 95, 6),
    borderWidth = 1
)

Label(
    'RESET',
    132, 134,
    
    fill = 'white',
    size = 7
)

# Difficulty Buttons
Circle(
    220, 152,
    12,
    
    fill = gradient('orange', 'darkOrange'),
    
    border = rgb(180, 95, 6),
    borderWidth = 1
)

Label(
    'LEFT',
    220, 172,
    
    fill = 'white',
    size = 5
)

Circle(
    257, 152,
    12,
    
    fill = gradient('orange', 'darkOrange'),
    
    border = rgb(180, 95, 6),
    borderWidth = 1
)

Label(
    'RIGHT',
    257, 172,
    
    fill = 'white',
    size = 5
)

Label(
    'DIFFICULTY',
    238, 134,
    
    fill = 'white',
    size = 7
)


# Select Button
Circle(
    307, 152,
    12,
    
    fill = gradient('orange', 'darkOrange'),
    
    border = rgb(180, 95, 6),
    borderWidth = 1
)

Label(
    'SELECT',
    307, 134,
    
    fill = 'white',
    size = 7
)