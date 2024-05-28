from cmu_graphics import *



Rect(0, 0, 400, 400,
     fill=gradient('limeGreen', 'yellow', 'orange', 'red', start='top'),
     opacity=20)

cellPhone = Rect(350, 320, 50, 80, border='dimGrey', borderWidth=3, align='center')
cellPhoneButton = Circle(350, 350, 5, fill='dimGrey')

barLow = Rect(180, 340, 10, 15, fill=None, border='dodgerBlue', align='bottom')
barMid = Rect(200, 340, 10, 30, fill=None, border='dodgerBlue', align='bottom')
barHigh = Rect(220, 340, 10, 45, fill=None, border='dodgerBlue', align='bottom')

def onMouseMove(mouseX, mouseY):
    # Move the cellPhone to the mouse location and cellPhoneButton accordingly.
    ### Place Your Code Here ###
    cellPhone.centerX = mouseX
    cellPhone.centerY = mouseY
    
    cellPhoneButton.centerX = mouseX
    cellPhoneButton.centerY = mouseY + 30
    
    # Based on your mouseY value, fill the reception bars.
    ### Place Your Code Here ###
    if (cellPhone.centerY > 101):
        barHigh.fill = None
    elif (cellPhone.centerY < 101):
        barHigh.fill = 'dodgerBlue'
    
    if (cellPhone.centerY > 201):
        barMid.fill = None
    elif (cellPhone.centerY < 201):
        barMid.fill = 'dodgerBlue'
        
    if (cellPhone.centerY > 301):
        barLow.fill = None
    elif (cellPhone.centerY < 301):
        barLow.fill = 'dodgerBlue'
        
    pass

cmu_graphics.run()