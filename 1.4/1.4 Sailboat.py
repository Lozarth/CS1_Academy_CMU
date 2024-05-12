# background
Rect(0, 0, 400, 400, fill='wheat')

# Draw the picture shadow.
### (HINT: This should be a RegularPolygon, like the sky.)
### Place Your Code Here ###
RegularPolygon(
    210, 210,
    180,
    7,
    
    fill = 'tan'
)

# Draw the sky and sun.
### Place Your Code Here ###
RegularPolygon(
    200, 200,
    180,
    7,
    
    fill = 'powderBlue'
)

Circle(
    270, 200,
    65,
    
    fill = 'orangeRed',
    opacity = 70
)

Circle(
    270, 200,
    55,
    
    fill = gradient('orange', 'orangeRed')
)


# Draw the boat hull, left sail, and right sail.
### Place Your Code Here ###

Polygon(
    60, 205,
    190, 205,
    160, 240,
    90, 240,
    
    fill = 'dimGray'
)

Polygon(
    125, 135,
    125, 205,
    60, 205,
    
    fill = 'forestGreen'
)

Polygon(
    130, 145,
    190, 205,
    130, 205,
    
    fill = 'limeGreen'
)

# Draw the sea.
### Place Your Code Here ###
Polygon(
    25, 240,
    375, 240,
    280, 365,
    120, 365,
    
    fill = 'cadetBlue'
)
