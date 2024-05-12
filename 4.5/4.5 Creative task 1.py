# I am NOT a satanist!!! This is all fantastical and it fits the theme.

import math
import random

app.background = 'black'

boardGrids = Group(
    # Bottom Row
    Rect(320, 320, 50, 50, fill = 'darkRed', border = 'black', borderWidth = 1),
    Rect(290, 320, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1),
    Rect(260, 320, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1),
    Rect(230, 320, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1),
    Rect(200, 320, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1),
    Rect(170, 320, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1),
    Rect(140, 320, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1),
    Rect(110, 320, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1),
    Rect(80, 320, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1),
    
    # Left Row
    Rect(30, 320, 50, 50, fill = 'darkRed', border = 'black', borderWidth = 1),
    Rect(40, 280, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1, rotateAngle = 90),
    Rect(40, 250, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1, rotateAngle = 90),
    Rect(40, 220, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1, rotateAngle = 90),
    Rect(40, 190, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1, rotateAngle = 90),
    Rect(40, 160, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1, rotateAngle = 90),
    Rect(40, 130, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1, rotateAngle = 90),
    Rect(40, 100, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1, rotateAngle = 90),
    Rect(40, 70, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1, rotateAngle = 90),
    
    # Top Row
    Rect(30, 30, 50, 50, fill = 'darkRed', border = 'black', borderWidth = 1),
    Rect(80, 30, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1),
    Rect(110, 30, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1),
    Rect(140, 30, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1),
    Rect(170, 30, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1),
    Rect(200, 30, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1),
    Rect(230, 30, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1),
    Rect(260, 30, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1),
    Rect(290, 30, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1),
    Rect(320, 30, 50, 50, fill = 'darkRed', border = 'black', borderWidth = 1),
    
    # Right Row
    Rect(330, 70, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1, rotateAngle = 90),
    Rect(330, 100, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1, rotateAngle = 90),
    Rect(330, 130, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1, rotateAngle = 90),
    Rect(330, 160, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1, rotateAngle = 90),
    Rect(330, 190, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1, rotateAngle = 90),
    Rect(330, 220, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1, rotateAngle = 90),
    Rect(330, 250, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1, rotateAngle = 90),
    Rect(330, 280, 30, 50, fill = 'darkRed', border = 'black', borderWidth = 1, rotateAngle = 90)
)

# Pentagram
Pentagram = Group(
    # Outer Circle
    Circle(200, 200, 110, fill = None, border = 'white', borderWidth = 3),
    # Flipped Star
    Star(200, 200, 110, 5, fill = None, border = 'white', borderWidth = 3, rotateAngle = -180),
    # CenterPentagon
    RegularPolygon(200, 200, 42, 5, fill = None, border = 'white', borderWidth = 3, rotateAngle = 0)
)


Label('Monopolium', 200, 200, fill = 'red', font = 'grenze', size = 35, border = 'black', borderWidth = 1)

# Roll Result
rollSumLabel = Label('', 200, 125, fill = 'red', font = 'symbols', size = 25)

# Go
Label('Go', 345, 345, fill = 'black', font = 'grenze', size = 25)
Label('5', 345, 360, fill = 'black', font = ' grenze', size = 15)

# Hell Avenue
Label('Hell', 305, 335, fill = 'black', font = 'grenze', size = 10)
Label('Avenue', 305, 345, fill = 'black', font = 'grenze', size = 10)
Label('6', 305, 360, fill = 'black', font = 'grenze', size = 15)

# Diabolic Chest
Label('Diabolic', 275, 335, fill = 'black', font = 'grenze', size = 9)
Label('Chest', 275, 345, fill = 'black', font = 'grenze', size = 10)
Label('7', 275, 360, fill = 'black', font = 'grenze', size = 15)

# Baltic Avenue
Label('Inferno', 245, 335, fill = 'black', font = 'grenze', size = 9)
Label('Lane', 245, 345, fill = 'black', font = 'grenze', size = 10)
Label('8', 245, 360, fill = 'black', font = 'grenze', size = 15)

# Soul Tax
Label('Soul', 215, 335, fill = 'black', font = 'grenze', size = 10)
Label('Tax', 215, 345, fill = 'black', font = 'grenze', size = 10)
Label('9',215, 360, fill = 'black', font = 'grenze', size = 15)

# Railroad of the Damnned
Label('Railroad', 185, 328, fill = 'black', font = 'grenze', size = 9)
Label('of the', 185, 338, fill = 'black', font = 'grenze', size = 10)
Label('Damned', 185, 348, fill = 'black', font = 'grenze', size = 9)
Label('10', 185, 360, fill = 'black', font = 'grenze', size = 15)

# Hades Passage
Label('Hades', 155, 335, fill = 'black', font = 'grenze', size = 10)
Label('Passage', 155, 345, fill = 'black', font = 'grenze', size = 9)
Label('11', 155, 360, fill = 'black', font = 'grenze', size = 15)

# Chance
Label('Chance', 125, 340, fill = 'black', font = 'grenze', size = 10)
Label('12', 125, 360, fill = 'black', font = 'grenze', size = 15)

# Brimstone Avenue
Label('Brimstone', 95, 335, fill = 'black', font = 'grenze', size = 7)
Label('Avenue', 95, 345, fill = 'black', font = 'grenze', size = 10)
Label('13', 95, 360, fill = 'black', font = 'grenze', size = 15)

# Hell (Jail)
Label('HELL', 63, 340, fill = 'red', font = 'grenze', size = 15)

Label('Just', 42, 338, fill = 'black', font = 'grenze', size = 10, rotateAngle = 90)
Label('Visiting', 62, 360, fill = 'black', font = 'grenze', size = 10)
Label('15', 40, 360, fill = 'black', font = 'grenze', size = 13)

# Reincarnation
Label('Reincarnat', 55, 50, fill = 'white', font = 'grenze', size = 10)
Label('ion', 55, 57, fill = 'white', font = 'grenze', size = 10)

# Go to hell
Label('Go to', 345, 45, fill = 'black', font = 'grenze', size = 15)
Label('HELL', 345, 60, fill = 'red', font = 'grenze', size = 15, bold = True)

# First Die
die1 = Group(
    Rect(150, 260, 30, 30, fill = 'white', border = 'black'),
    # One Face
    Circle(165, 275, 3, fill = 'black'),
    # Two Face
    Group(
        Circle(160, 270, 3, fill = 'black'),
        Circle(170, 280, 3, fill = 'black')
    ),
    # Three Face
    Group(
        Circle(158, 268, 3, fill = 'black'),
        Circle(165, 275, 3, fill = 'black'),
        Circle(172, 282, 3, fill = 'black')
    ),
    # Four Face
    Group(
        Circle(158, 268, 3, fill = 'black'),
        Circle(172, 268, 3, fill = 'black'),
        Circle(158, 282, 3, fill = 'black'),
        Circle(172, 282, 3, fill = 'black')
    ),
    # Five Face
    Group(
        Circle(158, 268, 3, fill = 'black'),
        Circle(172, 268, 3, fill = 'black'),
        Circle(165, 275, 3, fill = 'black'),
        Circle(158, 282, 3, fill = 'black'),
        Circle(172, 282, 3, fill = 'black')
    ),
    # Six Face
    Group(
        Circle(158, 268, 3, fill = 'black'),
        Circle(172, 268, 3, fill = 'black'),
        Circle(158, 275, 3, fill = 'black'),
        Circle(158, 282, 3, fill = 'black'),
        Circle(172, 275, 3, fill = 'black'),
        Circle(172, 282, 3, fill = 'black')
    )
)

# Second Die
die2 = Group(
    Rect(225, 260, 30, 30, fill = 'white', border = 'black'),
    # One Face
    Circle(240, 275, 3, fill = 'black'),
    # Two Face
    Group(
        Circle(235, 270, 3, fill = 'black'),
        Circle(245, 280, 3, fill = 'black')
    ),
    # Three Face
    Group(
        Circle(233, 268, 3, fill = 'black'),
        Circle(240, 275, 3, fill = 'black'),
        Circle(247, 282, 3, fill = 'black')
    ),
    # Four Face
    Group(
        Circle(233, 269, 3, fill = 'black'),
        Circle(247, 268, 3, fill = 'black'),
        Circle(233, 282, 3, fill = 'black'),
        Circle(247, 282, 3, fill = 'black')
    ),
    # Five Face
    Group(
        Circle(233, 268, 3, fill = 'black'),
        Circle(247, 268, 3, fill = 'black'),
        Circle(240, 275, 3, fill = 'black'),
        Circle(233, 282, 3, fill = 'black'),
        Circle(247, 282, 3, fill = 'black')
    ),
    # Six Face
    Group(
        Circle(233, 268, 3, fill = 'black'),
        Circle(247, 268, 3, fill = 'black'),
        Circle(233, 275, 3, fill = 'black'),
        Circle(233, 282, 3, fill = 'black'),
        Circle(247, 275, 3, fill = 'black'),
        Circle(247, 282, 3, fill = 'black')
    )
)

# Skull Piece
skullPiece = Group(
    Rect(340, 350, 10, 6, fill = rgb(163, 138, 89)),
    Oval(345, 345, 15, 18, fill = rgb(163, 138, 89)),
    Oval(341, 350, 6, 4, fill = 'black'),
    Oval(349, 350, 6, 4, fill = 'black'),
    Circle(341, 350, 1, fill = 'red'),
    Circle(349, 350, 1, fill = 'red'),
    Oval(345, 353, 4, 2, fill = 'black')
) 
skullPiece.rotateAngle = 90

# Variables
app.mouseDragging = False
app.rollingDice = False
app.rollSum = 0
app.currentGridNum = 0
app.currentGrid = boardGrids.children[app.currentGridNum]

skullPiece.centerX = app.currentGrid.centerX
skullPiece.centerY = app.currentGrid.centerY

# Sounds
# e-z.host my goat 🤑🤑
app.diceSounds = [
    Sound('https://r2.e-z.host/598c2c5a-e417-4d11-9f6c-6e31f5a4c5bc/7o6twkq9.wav'),
    Sound('https://r2.e-z.host/598c2c5a-e417-4d11-9f6c-6e31f5a4c5bc/lavtyjew.wav')
]

app.pieceSounds = [
    Sound('https://r2.e-z.host/598c2c5a-e417-4d11-9f6c-6e31f5a4c5bc/6wamcepv.wav'),
    Sound('https://r2.e-z.host/598c2c5a-e417-4d11-9f6c-6e31f5a4c5bc/vbeq5z74.wav'),
    Sound('https://r2.e-z.host/598c2c5a-e417-4d11-9f6c-6e31f5a4c5bc/kkiw1zd6.wav'),
    Sound('https://r2.e-z.host/598c2c5a-e417-4d11-9f6c-6e31f5a4c5bc/8lt01h75.wav'),
    Sound('https://r2.e-z.host/598c2c5a-e417-4d11-9f6c-6e31f5a4c5bc/zten86sg.wav')
]

def playRandomSound(soundList):
    randomSound = random.choice(soundList)
    randomSound.play()

# Functions
def rollDice():
    app.rollingDice = True
    
    playRandomSound(app.diceSounds)
    
    random1 = random.choice([1, 2, 3, 4, 5, 6])
    random2 = random.choice([1, 2, 3, 4, 5, 6])
    
    changeDieFace(die1, random1)
    changeDieFace(die2, random2)
        
    app.rollSum = random1 + random2
    rollSumLabel.value = app.rollSum
    
    sleep(.5)
    
    moveSkullPiece(app.rollSum)
        
    app.rollingDice = False

def moveSkullPiece(moveNum):
    alreadyMoved = 0
    
    while (alreadyMoved < moveNum):
        nextGridNum = app.currentGridNum + 1
        
        if (nextGridNum < 36):
            nextGrid = boardGrids.children[nextGridNum]
        elif (nextGridNum == 36):
            nextGridNum = 0
            nextGrid = boardGrids.children[nextGridNum]
        
        skullPiece.centerX = nextGrid.centerX
        skullPiece.centerY = nextGrid.centerY
        
        alreadyMoved += 1
        
        playRandomSound(app.pieceSounds)
        
        # Rotate skull piece based on where the piece is on the board
        if (skullPiece.centerX == 55 and skullPiece.centerY > 80):
            skullPiece.rotateAngle = 180
        elif (skullPiece.centerX >= 55 and skullPiece.centerY == 55):
            skullPiece.rotateAngle = 270
        elif (skullPiece.centerX == 345 and skullPiece.centerY >= 55):
            skullPiece.rotateAngle = 0
        elif(skullPiece.centerX <= 345 and skullPiece.centerY == 345):
            skullPiece.rotateAngle = 90
        
        app.currentGridNum = nextGridNum
        app.currentGrid = nextGrid
        
        sleep(0.5)

def changeDieFace(die, faceNumber):
    # Terrible unreadable code because for some reason I cannot change the visibility of a face group
    # without it breaking my code, so I will just make the fill of the black dots None.
    for index, child in enumerate(die.children):
        if (faceNumber == index):
            child.fill = 'black'
        elif (faceNumber != index and index != 0):
            child.fill = None
            
changeDieFace(die1, 1)
changeDieFace(die2, 1)

# Events
def onMouseMove(mouseX, mouseY):
    if (not app.rollingDice):
        # Move Dice
        die1.centerX = mouseX - 20
        die1.centerY = mouseY
    
        die2.centerX = mouseX + 20
        die2.centerY = mouseY
    
def onMouseDrag(mouseX, mouseY):
    app.mouseDragging = True
    
def onMouseRelease(mouseX, mouseY):
    die1.centerX = mouseX - 20
    die1.centerY = mouseY
    
    die2.centerX = mouseX + 20
    die2.centerY = mouseY
    
    if (app.mouseDragging):
        rollDice()
    
    app.mouseDragging = False

print('You have been sent to a limbo realm where you have to play Monopoly to either be reincarnated or sent to hell...')
print('"Keep rollin\', rollin\', rollin\', rollin\'" -Fred Durst')