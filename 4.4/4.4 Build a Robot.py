from cmu_graphics import *



app.background = 'gainsboro'

# background room
Rect(40, 40, 320, 400, fill=gradient('gray', 'gainsboro'), border='dimGray')
Line(0, 0, 40, 40, fill='dimGray')
Line(400, 0, 360, 40, fill='dimGray')

# button panel
Rect(0, 310, 400, 100, fill='slateGray', border='black', borderWidth=5)
blueButton = Circle(
    80, 360, 
    20, 
    fill = 'dodgerBlue', 
    border = 'black', 
    borderWidth = 3,
)
def blueButtonClick():
    leftEye.fill = 'dodgerBlue'
    rightEye.fill = 'dodgerBlue'
blueButton.clickFunc = blueButtonClick

goldButton = Circle(
    160, 360, 
    20, 
    fill = 'gold', 
    border = 'black', 
    borderWidth = 3
)
def goldButtonClick():
    leftEye.fill = 'gold'
    rightEye.fill = 'gold'
goldButton.clickFunc = goldButtonClick

ovalButton = Rect(
    250, 360, 
    70, 
    30, 
    align = 'center',
    fill = gradient('salmon', 'indianRed', start = 'top-left')
)
def ovalButtonClick():
    rectMouth.visible = False
    ovalMouth.visible = True
ovalButton.clickFunc = ovalButtonClick

rectButton = Rect(
    350, 
    360, 
    70, 
    30, 
    align = 'center',
    fill = gradient('salmon', 'indianRed', start='top-left')
)
def rectButtonClick():
    ovalMouth.visible = False
    rectMouth.visible = True
rectButton.clickFunc = rectButtonClick

Oval(250, 360, 40, 20, fill=None, border='black')
Rect(350, 360, 35, 15, fill=None, border='black', align='center')

# robot
Rect(80, 140, 240, 60, fill='midnightBlue')
Rect(165, 80, 70, 230, fill='midnightBlue')
Rect(100, 100, 200, 150, fill='cadetBlue', border='navy', borderWidth=4)
Line(200, 250, 200, 310, lineWidth=80, dashes=(5, 5))

leftEye = Circle(160, 160, 20, fill=None, border='dimGray')
rightEye = Circle(240, 160, 20, fill=None, border='dimGray')
ovalMouth = Oval(200, 210, 80, 40, fill='gray', border='midnightBlue',
                 visible=False)
rectMouth = Rect(200, 210, 70, 30, fill='gray', border='midnightBlue',
                 visible=False, align='center')

buttons = [
    blueButton,
    goldButton,
    ovalButton,
    rectButton
]

def onMousePress(mouseX, mouseY):
    # Check if the user pressed any of the four buttons on the control panel.
    # If so, update the robot accordingly.
    ### Place Your Code Here ###
    ### (HINT: We've defined some global variables for you on lines 10-14 and
    #          25-29.)
    for button in buttons:
        if (button.hits(mouseX, mouseY)):
            button.clickFunc()
    pass

cmu_graphics.run()