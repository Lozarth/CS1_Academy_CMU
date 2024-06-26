from cmu_graphics import *



app.background = gradient('black', 'midnightBlue', 'blue', start='left-top')

# background
Polygon(0, 0, 400, 220, 400, 400, 220, 400, fill='white', opacity=30)

# halo and the star
halo = Circle(0, 0, 30, fill=gradient('white', 'gold'), opacity=50)
halo.isGrowing = True

star = Star(0, 0, 1, 5, fill=gradient('lightYellow', 'gold'))

def onKeyHold(keys):
    # Check if the halo is growing and add or subtract accordingly from its size.
    ### Place Your Code Here ###
    if (halo.isGrowing):
        halo.radius += 1
    elif (not halo.isGrowing):
        halo.radius -= 1

    # If the radius is bigger than 50 or smaller than 20, change halo.isGrowing.
    ### Place Your Code Here ###
    if (halo.radius > 50):
        halo.isGrowing = False
    elif (halo.radius < 20):
        halo.isGrowing = True

    # If right is held, increase the centerX, centerY, and rotateAngle by 5
    # and the radius by 1. Also, wrap around from right-bottom corner to left-top
    # corner and reset the radius of the star to 1.
    ### Place Your Code Here ###
    if ('right' in keys):
        star.centerX += 5
        star.centerY += 5
        star.rotateAngle += 5
        star.radius += 1
        
        if ((star.centerX == 400) and (star.centerY == 400)):
            star.centerX = 0
            star.centerY = 0
            star.radius = 1

    halo.centerX = star.centerX
    halo.centerY = star.centerY

cmu_graphics.run()