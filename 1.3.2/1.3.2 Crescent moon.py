from cmu_graphics import *



# Colors
NightSky = rgb(30, 30, 30)
CloudGrey = rgb(90, 90, 90)

# Background
Rect(0, 0, 400, 400, fill = NightSky)

# Moon
Circle(200, 175, 100, fill = gradient('lightGrey', 'grey', 'grey', start = 'left'))
Circle(235, 140, 100, fill = NightSky)

# Clouds
Oval(115, 270, 175, 120, opacity = 80, fill = CloudGrey)
Oval(200, 305, 250, 100, opacity = 80, fill = CloudGrey)
Oval(280, 280, 125, 80, opacity = 80, fill = CloudGrey)
Oval(215, 350, 100, 40, opacity = 80, fill = CloudGrey)
cmu_graphics.run()