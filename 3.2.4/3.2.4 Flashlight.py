from cmu_graphics import *



# background
Rect(0, 0, 400, 400)

def turnOnFlashlight(intensity):
    # Check how large intensity is.
    # Draw triangles of different colors to represent light.
    ### Place Your Code Here ###
    if (intensity >= 29):
        Polygon(
            20, 0,
            380, 0,
            200, 230,
            
            fill = rgb(170, 170, 170)
        )
        
    if (intensity >= 31):
        Polygon(
            50, 0,
            350, 0,
            200, 230,
            
            fill = rgb(220, 220, 220)
        )
        
    if (intensity >= 60):
        Polygon(
            80, 0,
            320, 0,
            200, 230,
            
            fill = rgb(240, 240, 240)
        )
    
    if (intensity >= 90):
        Polygon(
            120, 0,
            280, 0,
            200, 230,
            
            fill = 'white'
        )

    # flashlight
    Rect(195, 230, 10, 60, fill=rgb(68, 68, 68))
    RegularPolygon(200, 225, 15, 3, fill=rgb(68, 68, 68), rotateAngle=180)
    Oval(200, 218, 24, 5, fill='white')

##### Place your code above this line, code below is for testing purposes #####
# test case:
turnOnFlashlight(0)

cmu_graphics.run()