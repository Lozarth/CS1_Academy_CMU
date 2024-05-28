from cmu_graphics import *



app.background = gradient('lightSkyBlue', 'orange', start='top')

# sun and lake
Circle(250, 335, 50, fill='gold')
Rect(0, 300, 400, 100, fill='dodgerBlue')

# boat and fishing rod
Polygon(0, 270, 0, 350, 50, 350, 85, 315, 100, 270, fill='sienna')
Line(0, 240, 140, 160)

# fishing line, fish body, and fish tail
fishingLine = Line(140, 160, 140, 340, lineWidth=1)

fishBody = Oval(340, 340, 50, 30, fill='salmon')
fishTail = Polygon(350, 340, 380, 350, 380, 330, fill='salmon')

print(fishBody.centerX)
print(fishBody.centerY)

def pullUpFish():
    fishingLine.x2 = 140
    fishingLine.y2 = 225

    fishBody.rotateAngle = 90
    fishBody.centerX = 140
    fishBody.centerY = 250
    fishTail.rotateAngle = 90
    fishTail.centerX = 140
    fishTail.top = 255

def onKeyPress(key):
    # Release the fish if the correct key is pressed.
    ### Place Your Code Here ###
    fishBody.centerX = 340
    fishBody.centerY = 340
    fishTail.centerX = 365
    fishTail.centerY = 340
    pass

def onMouseDrag(mouseX, mouseY):
    distance = (fishBody.centerX - mouseX)
    
    # If fish is very close to boat, pull it up.
    ### (HINT: Use a helper function.)
    ### Place Your Code Here ###
    print(fishBody.centerX)
    if (fishBody.centerX < 175):
        pullUpFish()
        return

    # If the mouse is behind the fish, only move the line.
    ### Place Your Code Here ###
    if (distance < 0):
        print('behind')
        fishingLine.x2 = mouseX
        fishingLine.y2 = mouseY

    # If the mouse is too far from the fish, only move the line.
    ### (HINT: They are too far when horizontal distance between them is more
    #          than 80.)
    ### Place Your Code Here ###
    
    distance = (fishBody.centerX - mouseX)
    
    if (distance > 80):
        print('too far')
        fishingLine.x2 = mouseX
        fishingLine.y2 = mouseY

    # If the mouse is close enough to the fish and below the water, the line
    # should hook the fish.
    ### (HINT: If the line 'hooks' the fish, both the line and the fish
    #          should move.)
    ### Place Your Code Here ###
    if (distance < 80 and distance > 0 and mouseY > 300):
        print('hooked')
        fishingLine.x2 = mouseX
        fishingLine.y2 = mouseY
        
        fishBody.centerX = fishingLine.x2 + 25
        fishBody.centerY = fishingLine.y2
        
        fishTail.centerX = fishingLine.x2 + 50
        fishTail.centerY = fishingLine.y2
    
    pass

cmu_graphics.run()