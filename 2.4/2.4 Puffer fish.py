from cmu_graphics import *



# background
app.background = 'skyBlue'

# spikes
spikes = Star(200, 200, 170, 20, fill='brown', roundness=30, visible=False)

# fins
Polygon(190, 103, 200, 60, 210, 103, fill='brown')
Oval(132, 184, 60, 20, fill='brown', rotateAngle=20)
Oval(132, 204, 60, 20, fill='brown', rotateAngle=-20)
Oval(268, 184, 60, 20, fill='brown', rotateAngle=-20)
Oval(268, 204, 60, 20, fill='brown', rotateAngle=20)

fish = Oval(200, 200, 120, 200, fill='orange')

# eyes and mouth
Circle(155, 150, 22, fill='white')
Circle(155, 150, 10)
Circle(245, 150, 22, fill='white')
Circle(245, 150, 10)
Oval(200, 250, 70, 30, fill='brown', border='white', borderWidth=10)

def onMousePress(x, y):
    # Change the width and the fill of the fish to make it puff up.
    # Display its dangerous spikes!
    ### Place Your Code Here ###
    fish.width = 200
    fish.height = 200
    fish.fill = 'saddleBrown'
    
    spikes.visible = True
    pass

def onMouseRelease(x, y):
    # Change the width and the fill of the fish to make it go back to normal.
    # Make the spikes go away too.
    ### Place Your Code Here ###
    fish.width = 120
    fish.height = 200
    fish.fill = 'orange'
    
    spikes.visible = False
    pass

cmu_graphics.run()