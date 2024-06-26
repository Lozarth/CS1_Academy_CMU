from cmu_graphics import *



app.background = gradient('deepSkyBlue', 'pink', start='top')
Rect(0, 235, 400, 165,
     fill=gradient('darkGreen', 'mediumTurquoise', start='bottom'))

# legs, chest, and tail
Polygon(180, 305, 185, 320, 200, 265, 180, 250, fill='orangeRed', border='black')
Polygon(285, 305, 295, 325, 310, 245, 280, 245, fill='orangeRed', border='black')
Polygon(390, 65, 325, 95, 340, 110, 360, 105, 355, 125, 370, 130,
        fill='floralWhite', border='black')
Polygon(85, 170, 120, 160, 190, 175, 135, 260, fill='floralWhite', border='black')

# Define a polygon to add points to.
### Modify Your Code Here ###
connect = Polygon(
    fill = 'orangeRed',
    border = 'black'
)

# dots
Circle(190, 175, 3)
Label('0, 9, 25', 195, 165, bold=True, align='left')
Circle(120, 160, 3)
Label('1', 120, 170, bold=True)
Circle(85, 170, 3)
Label('2', 75, 170, bold=True)
Circle(85, 110, 3)
Label('3', 95, 110, bold=True)
Circle(70, 40, 3)
Label('4', 80, 40, bold=True)
Circle(120, 75, 3)
Label('5', 130, 75, bold=True)
Circle(140, 80, 3)
Label('6', 150, 80, bold=True)
Circle(195, 50, 3)
Label('7', 205, 50, bold=True)
Circle(175, 105, 3)
Label('8', 185, 105, bold=True)
Circle(135, 260, 3)
Label('10', 125, 260, bold=True)
Circle(170, 340, 3)
Label('11', 180, 340, bold=True)
Circle(190, 260, 3)
Label('12', 200, 255, bold=True)
Circle(220, 270, 3)
Label('13', 220, 280, bold=True)
Circle(250, 260, 3)
Label('14', 260, 260, bold=True)
Circle(280, 340, 3)
Label('15', 290, 340, bold=True)
Circle(300, 260, 3)
Label('16', 315, 260, bold=True)
Circle(320, 225, 3)
Label('17', 330, 225, bold=True)
Circle(300, 180, 3)
Label('18, 24', 310, 180, bold=True, align='left')
Circle(325, 95, 3)
Label('19', 325, 85, bold=True)
Circle(340, 110, 3)
Label('20', 340, 120, bold=True)
Circle(360, 105, 3)
Label('21', 360, 95, bold=True)
Circle(355, 125, 3)
Label('22', 355, 135, bold=True)
Circle(370, 130, 3)
Label('23', 370, 140, bold=True)

# face
Line(110, 130, 140, 150)
Line(155, 125, 153, 150)
Oval(145, 146, 20, 12)
Circle(110, 108, 12, fill='white')
Circle(115, 108, 6)
Circle(155, 108, 12, fill='white')
Circle(160, 108, 6)

def onMousePress(mouseX, mouseY):
    # When the mouse is pressed, add a point to connect to the polygon.
    ### Place Your Code Here ###
    connect.addPoint(mouseX, mouseY)
    pass

cmu_graphics.run()