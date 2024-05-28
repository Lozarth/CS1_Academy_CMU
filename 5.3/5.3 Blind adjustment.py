from cmu_graphics import *



app.background = gradient('deepSkyBlue', 'gold', start='top')

# sun
Circle(200, 150, 40, fill=gradient('yellow', 'gold'))

def drawFlower(x, y):
    Line(x, y, x, y + 10, fill='springGreen')
    Star(x, y, 6, 8, fill='yellow')
    Circle(x, y, 2, fill='peru')

# hill
Oval(195, 400, 800, 300, fill=gradient('limeGreen', 'darkGreen', start='top'))
drawFlower(45, 275)
drawFlower(65, 335)
drawFlower(95, 290)
drawFlower(145, 260)
drawFlower(185, 350)
drawFlower(205, 285)
drawFlower(245, 300)
drawFlower(290, 275)
drawFlower(335, 325)
drawFlower(360, 345)

# window
Rect(0, 0, 400, 400, fill=None, border=rgb(120, 62, 75), borderWidth=50)
Rect(40, 40, 320, 320, fill=None, border='silver', borderWidth=10)
Rect(45, 45, 310, 310, fill='white', border='black', borderWidth=1, opacity=30)
Line(40, 40, 50, 50, fill='darkGrey')
Line(40, 360, 50, 350, fill='darkGrey')
Line(360, 40, 350, 50, fill='darkGrey')
Line(360, 360, 350, 350, fill='darkGrey')

blindsShadow = Line(200, 17, 200, 387, fill='tan', lineWidth=370, dashes=(1, 19))
blinds = Line(200, 15, 200, 385, fill='cornSilk', lineWidth=370, dashes=(1, 19))
blinds.dashWidth = 1

Rect(10, 10, 380, 20, fill='wheat')

def onKeyHold(keys):
    # When holding the up or down arrow keys, increase or decrease the blinds
    # dashWidth custom property by one. Make sure it does not go above 19 or
    # below 0.
    ### Place Your Code Here ###
    if ('up' in keys):
        if (blinds.dashWidth < 19):
            blinds.dashWidth += 1
    elif ('down' in keys):
        if (blinds.dashWidth > 0):
            blinds.dashWidth -= 1
    # Set the dashes for both the blinds and the blindsShadow using the dashWidth
    # property.
    ### (HINT: Dashes can be a tuple of the form (dashWidth, gapWidth). In this,
    #          case, the gapWidth should be 20 minus the dashWidth.)
    ### Place Your Code Here ###
    blindsShadow.dashes = (blinds.dashWidth, 20 - blinds.dashWidth)
    blinds.dashes = (blinds.dashWidth, 20 - blinds.dashWidth)
    pass

cmu_graphics.run()