from cmu_graphics import *



app.background = gradient('gray', 'black')
# Walls

dirtyRoom = Group(
    RegularPolygon(
        200, 200, 
        200, 6, 
        fill= rgb(168, 154, 128),
        border = 'black', 
        borderWidth = 5
    ),
    Line(200, 0, 200, 200, lineWidth = 5),
    Line(29, 300, 200, 200, lineWidth = 5),
    Line(369, 300, 200, 200, lineWidth = 5),

    # Floor
    Polygon(
        200, 200, 
        370, 300, 
        200, 400, 
        29, 300,
    
        fill = rgb(161, 161, 161),
        border = 'black',
        borderWidth = 5
    ),
    
    Polygon(
        93, 333,
        107, 342,
        112, 325,
        130, 320,
        128, 304,
        106, 311,
        100, 325,
    ), 
    Oval(348, 298, 23, 6, fill='sienna'),
    Line(247, 33, 247, 229, fill='maroon', lineWidth=4),
    Oval(238, 238, 35, 25, fill='maroon'),

)


normalRoom = Group(
    RegularPolygon(
        200, 200, 
        200, 6, 
        fill= 'oldLace',
        border = 'black', 
        borderWidth = 5
    ),
    Line(200, 0, 200, 200, lineWidth = 5),
    Line(29, 300, 200, 200, lineWidth = 5),
    Line(369, 300, 200, 200, lineWidth = 5),

    # Floor
    Polygon(
        200, 205, 
        354, 300, 
        200, 390, 
        35, 300,
    
        fill = 'white'
    )
)

# Window
brokenWindow = Group(
    Polygon(
        170, 80,
        170, 150,
        62, 203,
        60, 137,
    
        fill = 'dimGray',
        border = 'black',
        borderWidth = 5
    ),
    
    # Tree
    Polygon(
        136, 161,
        143, 145,
        142, 128,
        143, 119,
        145, 129,
        153, 139,
        149, 155,
        
        
        fill = 'saddleBrown'
    ),
    Polygon(
        143, 136,
        136, 141,
        129, 143,
        136, 148,
        143, 142,
        
        fill = 'saddleBrown'
    ),
    
    Line(
        117, 107,
        117, 171,
    ),
    Line(
        165, 123,
        64, 170,
    ),
    
    # Cracks
    Polygon(
        96, 132,
        106, 132,
        112, 122,
        115, 135,
        102, 147,
        101, 138,
    ),
    Polygon(
        81, 167,
        87, 167,
        90, 170,
        86, 175
    ), Star(65, 200, 20, 6, fill='saddlebrown', roundness=15)
)

normalWindow = Group(
    Polygon(
        170, 80,
        170, 150,
        62, 203,
        60, 137,
    
        fill = 'skyBlue',
        border = 'black',
        borderWidth = 5
    ),
    
    # Tree
    Polygon(
        136, 161,
        143, 145,
        142, 128,
        143, 119,
        145, 129,
        153, 139,
        149, 155,
        
        
        fill = 'saddleBrown'
    ),
    Polygon(
        143, 136,
        136, 141,
        129, 143,
        136, 148,
        143, 142,
        
        fill = 'saddleBrown'
    ),
    # Leaves
    Star(
        129, 143,
        12,
        6,
        
        fill = 'forestGreen',
        rotateAngle = 25
    ),
    Star(
        143, 119,
        14,
        6,
        
        fill = 'forestGreen',
        rotateAngle = -15
    ),
    Line(
        117, 107,
        117, 171,
    ),
    Line(
        165, 123,
        64, 170,
    ),
    
    # Trees (green leaves instead of dead)
)

# Door
brokenDoor = Group(
    Polygon(
        290, 130,
        340, 158,
        340, 282,
        290, 253,
    
        fill = gradient('saddlebrown', 'black', start='top'),
        border = 'black',
        borderWidth = 5
    ),

    # Crack
    Polygon(
        340, 190,
        322, 200,
        315, 194,
        310, 206,
        326, 214,
        340, 200
    ),
    
    # Knob
    Circle(
        327, 225,
        4, 
    
        fill = gradient('gainsboro', 'darkGray')
    )
)

normalDoor = Group(
    Polygon(
        290, 130,
        340, 158,
        340, 282,
        290, 253,
    
        fill = gradient('saddleBrown', 'brown'),
        border = 'black',
        borderWidth = 5
    ),
    
    # Knob
    Circle(
        327, 225,
        4, 
    
        fill = gradient('gainsboro', 'darkGray')
    )
)



# Bed
dirtyBed = Group(
    Polygon(
        119, 248,
        154, 273,
        242, 224,
        200, 200, 
    
        fill = 'olive', border = 'black', borderWidth = 3
    ),
    Polygon(
        201, 208,
        206, 215,
        219, 219,
        208, 222,
        205, 230,
        198, 220, 
        187, 219,
        197, 213, 
        
        fill=gradient('saddlebrown', 'white', start='top')
    )
)
        
normalBed = Group(
    Polygon(
        119, 248,
        154, 273,
        242, 224,
        200, 200, 
    
        fill='royalBlue', border='black', borderWidth=3
    ),
    

    Line(170, 80, 60, 137, fill = 'maroon'),
    
    Polygon(
        201, 208,
        206, 215,
        219, 219,
        208, 222,
        205, 230,
        198, 220, 
        187, 219,
        197, 213,
        
        fill=gradient('skyBlue', 'white', start='top')
    )
)

#Health Symbol
normalSign = Polygon(
    306, 83,
    324, 90,
    320, 108,
    336, 114,
    333, 127,
    318, 123,
    317, 137,
    303, 131,
    303, 118,
    293, 112,
    294, 97,
    305, 102,
    
    fill = 'maroon',
    border = 'black',
    borderWidth = 3
)

# DRAW STUPID GLUTTONOUS PEEP
def drawStupidPeep(x, y, color, color2, eyeColor):
    # Shadow
    peepGroup = Group(
        Oval(
            x - 1, y,
            20, 25,
        
            fill = 'black'
        ),
        # Body
        Oval(
            x, y,
            20, 25,
        
            fill = gradient(color, color2)
        ),
    
        # Shadow
        Oval(
            x - 1, y - 10,
            20, 15,
        
            fill = 'black'
        ),
        # Ears
        Oval(
            x - 7, y - 16,
            10, 20,
        
            rotateAngle = -15,
            fill = 'black'
        ),
        Oval(
            x - 6, y - 15,
            10, 20,
        
            rotateAngle = -15,
            fill = gradient(color, color2)
        ),
        Oval(
            x + 5, y - 15,
            10, 20,
        
            rotateAngle = 15,
            fill = gradient(color, color2)
        ),
        # Head
        Oval(
            x, y - 10,
            20, 15,
        
            fill = gradient(color, color2)
        ),
        # Eyes
        Circle(
            x - 5, y - 11,
            2,
            
            fill = eyeColor
        ),
        Circle(
            x + 5, y - 11,
            2,
            
            fill = eyeColor
        ),
        # Mouth
        Circle(
            x, y - 8,
            2,
            
            fill = 'black'
        )
    )
    
    # hack to not make the emoPeeps and normalPeeps Group error
    return peepGroup

emoPeeps = Group(
    drawStupidPeep(84, 292, rgb(69, 69, 69), 'black', 'red'),
    drawStupidPeep(180, 313, rgb(69, 69, 69), 'black', 'red'),
    drawStupidPeep(201, 358, rgb(69, 69, 69), 'black', 'red'),
    drawStupidPeep(235, 277, rgb(69, 69, 69), 'black', 'red'),
    drawStupidPeep(263, 328, rgb(69, 69, 69), 'black', 'red')
)

normalPeeps = Group(
    drawStupidPeep(84, 292, 'red', 'maroon', 'black'),
    drawStupidPeep(180, 313, 'blue', 'navy', 'black'),
    drawStupidPeep(201, 358, 'lime', 'green', 'black'),
    drawStupidPeep(235, 277, 'fuchsia', 'purple', 'black'),
    drawStupidPeep(263, 328, 'orangeRed', rgb(148, 48, 10), 'black')
)


normalWindow.visible = False
normalDoor.visible = False
normalRoom.visible = False
normalBed.visible = False
normalPeeps.visible = False

# Mouse Events
def onMousePress(mouseX, mouseY):
    brokenWindow.visible = False
    brokenDoor.visible = False
    dirtyBed.visible = False
    dirtyRoom.visible = False
    emoPeeps.visible = False
    
    
    normalWindow.visible = True
    normalDoor.visible = True
    normalBed.visible = True
    normalRoom.visible = True
    normalPeeps.visible = True
    normalSign.fill='red'
    app.background = gradient('white', 'lightGray')
    
def onMouseRelease(mouseX, mouseY):
    brokenWindow.visible = True
    brokenDoor.visible = True
    dirtyBed.visible =  True
    dirtyRoom.visible = True
    emoPeeps.visible = True
    
    normalWindow.visible = False
    normalDoor.visible = False
    normalBed.visible = False
    normalRoom.visible = False
    normalSign.fill='darkRed'
    normalPeeps.visible = False
    app.background = gradient('gray', 'black')
cmu_graphics.run()