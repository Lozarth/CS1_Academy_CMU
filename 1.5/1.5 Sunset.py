from cmu_graphics import *



### Place Your Code Here ###

# Sky
Rect(
    0, 0,
    400, 200,
    
    fill = gradient('lightSkyBlue', 'pink', 'coral', start = 'top')
)
#Sun
Circle(
    200, 200,
    70,
    
    fill = 'orange',
    opacity = 50
)
Circle(
    200, 200,
    50,
    
    fill = 'gold'
)

# Sea
Rect(
    0, 200,
    400, 60,
    
    fill = 'dodgerBlue'
)
Rect(
    0, 260,
    400, 40,
    
    fill = 'deepSkyBlue'
)
Rect(
    0, 300,
    400, 100,
    
    fill = 'turquoise'
)
#Foam
Polygon(
    0, 280,
    300, 335,
    400, 320,
    400, 400,
    0, 400,
    
    fill = 'white'
)
#Reflections
Oval(
    200, 204,
    120, 5,
    
    fill = 'gold',
    opacity = 80
)
Oval(
    165, 210,
    80, 5,
    
    fill = 'gold',
    opacity = 70
)
Oval(
    255, 210,
    70, 5,
    
    fill = 'gold',
    opacity = 70
)
Oval(
    230, 217,
    95, 5,
    
    fill = 'gold',
    opacity = 70
)
Oval(
    190, 223,
    60, 5,
    
    fill = 'gold',
    opacity = 60
)
Oval(
    155, 232,
    60, 5,
    
    fill = 'gold',
    opacity = 40
)
Oval(
    235, 232,
    60, 5,
    
    fill = 'gold',
    opacity = 40
)

# Beach
Polygon(
    0, 290,
    300, 360,
    400, 330,
    400, 400,
    0, 400,
    
    fill = 'wheat'
)
#Palm Tree
Polygon(
    50, 175,
    60, 175,
    50, 275,
    55, 360,
    30, 360,
    35, 280,
    
    fill = 'sienna'
)
Star(
    55, 175,
    60,
    9,
    
    fill = 'limeGreen',
    roundness = 50
)
#Coconut
Circle(
    20, 185,
    7,
    
    fill = 'maroon'
)
Star(
    55, 175,
    50,
    8,
    
    fill = 'green',
    roundness = 50
)
#Coconut
Circle(
    40, 180,
    7,
    
    fill = 'maroon'
)
#Coconut
Circle(
    40, 200,
    7,
    
    fill = 'maroon'
)

Polygon(
    0, 335,
    400, 390,
    400, 400,
    0, 400,
    
    fill = 'burlyWood'
)

cmu_graphics.run()