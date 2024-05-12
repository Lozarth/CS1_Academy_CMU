app.background = 'cornflowerBlue'
app.animalName = None

spikes = Star(200, 335, 130, 30, fill='saddleBrown', roundness=80)

# body
Circle(140, 330, 15, fill='navajoWhite', border='tan', borderWidth=5)
Circle(260, 330, 15, fill='navajoWhite', border='tan', borderWidth=5)
Oval(200, 310, 160, 110, fill='tan', align='top')

# eyes
Circle(175, 360, 7)
Circle(225, 360, 7)

# nose
RegularPolygon(200, 390, 15, 3, rotateAngle=180)

leftEyebrow = Line(155, 345, 170, 345, rotateAngle=-15)
rightEyebrow = Line(245, 345, 230, 345, rotateAngle=15)

def drawAnimal(animal):
    # Change the number of spikes if it is a hedgehog and the fill if it is not.
    ### Place Your Code Here ###
    app.animalName = animal
    
    if (animal == 'hedgehog'):
        spikes.fill = 'saddleBrown'
        spikes.points = 60
    else:
        spikes.fill = gradient('saddleBrown', 'saddleBrown', 'saddleBrown', 'tan')
        spikes.points = 30
    pass

def onMousePress(mouseX, mouseY):
    # Puff the spikes if it is a porcupine.
    # Change the eyebrows to make it disturbed.
    ### Place Your Code Here ###
    leftEyebrow.rotateAngle = 30
    rightEyebrow.rotateAngle = -30
    
    if (app.animalName == 'porcupine'):
        spikes.radius = 250
        spikes.roundness = 40
        
    pass

def onMouseRelease(mouseX, mouseY):
    # Change the puff and eyebrows back to the original state.
    ### Place Your Code Here ###
    leftEyebrow.rotateAngle = -15
    rightEyebrow.rotateAngle = 15
    
    if (app.animalName == 'porcupine'):
        spikes.radius = 130
        spikes.roundness = 80
    pass

##### Place your code above this line, code below is for testing purposes #####
# test case:
drawAnimal('porcupine')
