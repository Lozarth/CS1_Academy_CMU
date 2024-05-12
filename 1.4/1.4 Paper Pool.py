# Draw the paper.
### (HINT: For the blue lines, use a very thick line with dashes. You can look at
#          the Scotty Dog sample creative task later in the unit for an example.)
### Place Your Code Here ###

PaperBlue = rgb(230, 230, 245)
PaperGrey = rgb(210, 210, 210)

Rect(
    0, 0,
    400, 400,
    
    fill = gradient('white', PaperBlue, start = 'top')
)

Line(
    200, 0,
    200, 400,
    
    fill = 'lightBlue',
    lineWidth = 400,
    dashes = (1, 19)
)

Line(
    40, 0,
    40, 400,
    
    fill = 'red',
    opacity = 50
)

# Draw the pool and water.
### Place Your Code Here ###

Oval(
    220, 200,
    300, 100,
    
    fill = gradient('white', PaperGrey, start = 'top')
)

Oval(
    220, 220,
    265, 58,
    
    fill = gradient('azure', 'lightBlue', start = 'top')
)

# Draw the four waterfalls.
### Place Your Code Here ###

Line(
    83, 180,
    83, 218,
    
    fill = 'lightBlue'
)

Line(
    128, 160,
    128, 200,
    
    fill = 'lightBlue'
)

Line(
    310, 160,
    310, 200,
    
    fill = 'lightBlue'
)

Line(
    358, 180,
    358, 218,
    
    fill = 'lightBlue'
)

# This draws the stick person.
Circle(98, 143, 8)
Line(95, 150, 88, 165)
Line(88, 165, 92, 168)
Line(95, 150, 96, 163)
Line(96, 163, 100, 166)
Line(95, 150, 102, 168)
Line(102, 168, 108, 175)
Line(108, 175, 108, 185)
Line(102, 168, 112, 175)
Line(112, 175, 112, 185)