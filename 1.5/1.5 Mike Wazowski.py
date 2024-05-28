from cmu_graphics import *



### Place Your Code Here ###

# Background
Rect(
    0, 0,
    400, 400,
    
    fill = 'crimson'
)
#Lines
Line(
    0, 200,
    400, 200,
    
    fill = 'darkRed',
    opacity = 20,
    lineWidth = 400,
    dashes = (5, 75)
)

# Horns
Polygon(
    135, 90,
    150, 105,
    130, 125,
    
    fill = gradient('whiteSmoke', 'khaki', start = 'top')
)
Polygon(
    265, 90,
    270, 125,
    250, 105,
    
    fill = gradient('whiteSmoke', 'khaki', start = 'top')
)

# Arms
#Left Finger
Line(
    110, 300,
    120, 310,
    
    fill = gradient('mediumSeaGreen', 'greenYellow', start = 'left'),
    lineWidth = 8
)
#Left Arm
Line(
    112, 240,
    105, 265,

    fill = gradient('mediumSeaGreen', 'greenYellow', start = 'left'),
    lineWidth = 8
)
Line(
    106, 260,
    110, 310,
    
    fill = gradient('mediumSeaGreen', 'greenYellow', start = 'left'),
    lineWidth = 8
)
#Hand
Oval(
    110, 310,
    15, 25,
    
    fill = gradient('mediumSeaGreen', 'greenYellow', start = 'left')
)
#Right Finger
Line(
    290, 300,
    280, 310,
    
    fill = gradient('mediumSeaGreen', 'greenYellow', start = 'left'),
    lineWidth = 8
)
#Right Arm
Line(
    293, 225,
    290, 310,
    
    fill = gradient('mediumSeaGreen', 'greenYellow', start = 'left'),
    lineWidth = 8
)
#Hand
Oval(
    290, 310,
    15, 25,
    
    fill = gradient('mediumSeaGreen', 'greenYellow', start = 'left'),
)

# Legs
#Left Leg
Line(
    170, 300,
    170, 360,
    
    fill = gradient('mediumSeaGreen', 'greenYellow', start = 'left'),
    lineWidth = 15
)
#Right Leg
Line(
    230, 300,
    230, 360,
    
    fill = gradient('mediumSeaGreen', 'greenYellow', start = 'left'),
    lineWidth = 15
)

# Oval for leg curves
Oval(
    200, 333,
    55, 110,
    
    fill = 'crimson'
)


#Left Foot
Oval(
    170, 360,
    30, 20,
    
    fill = gradient('mediumSeaGreen', 'greenYellow', start = 'left')
)
#Right Foot
Oval(
    230, 360,
    30, 20,
    
    fill = gradient('mediumSeaGreen', 'greenYellow', start = 'left'),
)

# Body
Oval(
    200, 200,
    200, 220,
    
    fill = gradient('greenYellow', 'greenYellow', 'mediumSeaGreen')
)

# Mouth
Circle(
    245, 233,
    10,
    
    fill = 'darkGreen'
)
Circle(
    245, 235,
    10,
    
    fill = 'greenYellow'
)
Circle(
    155, 233,
    10,
    
    fill = 'darkGreen'
)
Circle(
    155, 235,
    10,
    
    fill = 'greenYellow'
)
Oval(
    200, 232,
    100, 50,
    
    fill = 'darkGreen'
)
Oval(
    200, 230,
    100, 50,
    
    fill = 'greenYellow'
)

# Eye
#Sclera
Circle( 
    200, 160,
    50,
    
    fill = 'white'
)
#Iris
Circle(
    200, 160,
    25,
    
    fill = gradient('mediumSeaGreen', 'seaGreen')
)
Star(
    200, 160,
    25,
    25,
    
    fill = gradient('springGreen', 'mediumSeaGreen'),
    roundness = 50
)
#Pupil
Circle(
    200, 160,
    15,
    
    fill = 'black'
)
#Reflections
Circle(
    180, 150,
    2,
    
    fill = 'white'
)
Circle(
    190, 150,
    5,
    
    fill = 'white'
)

cmu_graphics.run()