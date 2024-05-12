# background
Rect(0, 0, 400, 300, fill=gradient('powderBlue', 'gold', start='top'))
Rect(0, 150, 400, 300, fill=gradient('lightBlue', 'darkCyan', start='left-top'))
Oval(140, 220, 500, 40, fill=gradient('white', 'lightBlue'), opacity=20)
Polygon(0, 20, 200, 100, 340, 220, 0, 220,
        fill=gradient('teal', 'midnightBlue', start='top'))

# Draw the ripples in the water around the rocks.
### Place Your Code Here ###

Oval(
    100, 340, # x, y
    420, 60,  # size
    
    fill = gradient('white', 'lightBlue', start = 'center'),
    opacity = 80
)

Oval(
    260, 260, # x, y
    240, 40,  # size
    
    fill = gradient('white', 'lightBlue', start = 'center'),
    opacity = 40
)

# Draw the rocks in the water.
### Place Your Code Here ###

Polygon(
    240, 180, # p1
    360, 220, # p2
    340, 260, # p3
    160, 260, # p4
    
    fill = gradient('teal', 'darkSlateBlue', start = 'top')
)

Polygon(
    0, 220,   # p1
    140, 200, # p2
    280, 340, # p3
    0, 340,   # p4
    
    fill = gradient('darkCyan', 'darkSlateBlue', start = 'top')
)

# Draw the house and the rock in front of the house.
### Place Your Code Here ###

# Roof
Polygon(
    80, 100,   # p1
    140, 100,  # p2
    160, 120,  # p3
    100, 120,  # p4

    fill = gradient('salmon', 'indianRed', start = 'top')
)

# Left Wall
Polygon(
    80, 100,  # p1
    100, 120, # p2
    100, 160, # p3
    80, 160,   # p4
    
    fill = gradient('lightGrey', 'darkGrey', start = 'top')
)

# Front Wall
Polygon(
    100, 120, # p1
    160, 120, # p2
    160, 160, # p3
    100, 160, # p4
    
    fill = gradient('gainsboro', 'silver', start = 'top')
)

# Rock
Polygon(
    80, 140,  # p1
    120, 140, # p2
    180, 160, # p3
    60, 160,  # p4
    
    fill = gradient('darkCyan', 'midnightBlue', start = 'top')
)


# Draws the fog over the scene.
Rect(0, 0, 400, 400, fill='grey', opacity=20)
