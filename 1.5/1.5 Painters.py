### Place Your Code Here ###

# Background
Rect(
    0, 0,
    400, 400,
    
    fill = 'whiteSmoke'
)
Oval(
    70, 210,
    200, 150,
    
    fill = 'mediumPurple'
)
Oval(
    120, 150,
    150, 190,
    
    fill = 'mediumPurple'
)
Oval(
    330, 210,
    150, 110,
    
    fill = 'mediumPurple'
)
Oval(
    230, 160,
    150, 150,
    
    fill = 'mediumPurple'
)
Rect(
    0, 200,
    400, 200,
    
    fill = 'mediumPurple'
)

# Ladder
Line(
    320, 400,
    300, 95,
    
    fill = 'black',
    lineWidth = 2
)
Line(
    360, 400,
    340, 95,
    
    fill = 'black',
    lineWidth = 2
)
Line(
    340, 400,
    320, 95,
    
    fill = 'black',
    lineWidth = 40,
    dashes = (2, 15)
)

# Rolling Brush
#Brush 1
Line(
    180, 150,
    150, 120,
    
    fill = 'white',
    lineWidth = 4
)
Line(
    150, 120,
    145, 100,
    
    fill = 'white',
    lineWidth = 2
)
Line(
    150, 120,
    130, 115,
    
    fill = 'white',
    lineWidth = 2
)
Line(
    125, 115,
    145, 95,
    
    fill = 'white',
    lineWidth = 8
)
#Brush2
Line(
    145, 260,
    145, 220,
    
    fill = 'white',
    lineWidth = 4
)
Line(
    145, 220,
    160, 210,
    
    fill = 'white',
    lineWidth = 2
)
Line(
    145, 220,
    130, 210,
    
    fill = 'white',
    lineWidth = 2
)
Line(
    130, 205,
    160, 205,
    
    fill = 'white',
    lineWidth = 8
)

# Paint Bucket
Circle(
    50, 370,
    15,
    
    fill = None,
    border = 'black'
)
Rect(
    35, 370,
    30, 30,
    
    fill = 'black'
)
Line(
    40, 370,
    60, 370,
    
    fill = 'darkViolet',
    lineWidth = 4
)

# Person 1
#Head
Circle(
    105, 245,
    20,
    
    fill = 'black'
)
#Left Arm
Polygon(
    90, 275,
    90, 300,
    70, 330,
    
    fill = 'black'
)
#Right Arm
Polygon(
    145, 255,
    125, 300,
    115, 285,
    
    fill = 'black'
)
#Left Leg
Line(
    80, 400,
    90, 320,
    
    fill = 'black'
)
#Right Leg
Line(
    125, 400,
    120, 320,
    
    fill = 'black'
)
#Torso
Oval(
    105, 300,
    40, 80,
    
    fill = 'black'
)
Rect(
    85, 300,
    40, 40,
    
    fill = 'black'
)

# Person 2
#Head
Circle(
    220, 130,
    20,
    
    fill = 'black'
)
#Torso
Circle(
    240, 160,
    20,
    
    fill = 'black'
)
Line(
    280, 220,
    240, 160,
    
    fill = 'black',
    lineWidth = 40
)
#Left Arm
Polygon(
    230, 175,
    225, 160,
    175, 145,
    
    fill = 'black'
)
#Right Arm
Polygon(
    250, 145,
    305, 155,
    260, 160,
    
    fill = 'black'
)
#Left Leg
Line(
    275, 280,
    270, 225,
    
    fill = 'black',
    lineWidth = 2
)
#Right Leg
Line(
    325, 265,
    285, 210,
    
    fill = 'black',
    lineWidth = 2
)