from cmu_graphics import *



from cmu_graphics import *

import math
import time

app.background = rgb(106, 168, 79)

groundTiles = Group(
    Rect(0, 0, 50, 50, fill = rgb(56, 118, 29)),
    Rect(100, 0, 50, 50, fill = rgb(56, 118, 29)),
    Rect(200, 0, 50, 50, fill = rgb(56, 118, 29)),
    Rect(300, 0, 50, 50, fill = rgb(56, 118, 29)),
    Rect(50, 50, 50, 50, fill = rgb(56, 118, 29)),
    Rect(150, 50, 50, 50, fill = rgb(56, 118, 29)),
    Rect(250, 50, 50, 50, fill = rgb(56, 118, 29)),
    Rect(350, 50, 50, 50, fill = rgb(56, 118, 29)),
    Rect(0, 100, 50, 50, fill = rgb(56, 118, 29)),
    Rect(100, 100, 50, 50, fill = rgb(56, 118, 29)),
    Rect(200, 100, 50, 50, fill = rgb(56, 118, 29)),
    Rect(300, 100, 50, 50, fill = rgb(56, 118, 29)),
    Rect(50, 150, 50, 50, fill = rgb(56, 118, 29)),
    Rect(150, 150, 50, 50, fill = rgb(56, 118, 29)),
    Rect(250, 150, 50, 50, fill = rgb(56, 118, 29)),
    Rect(350, 150, 50, 50, fill = rgb(56, 118, 29)),
    Rect(0, 200, 50, 50, fill = rgb(56, 118, 29)),
    Rect(100, 200, 50, 50, fill = rgb(56, 118, 29)),
    Rect(200, 200, 50, 50, fill = rgb(56, 118, 29)),
    Rect(300, 200, 50, 50, fill = rgb(56, 118, 29)),
    Rect(50, 250, 50, 50, fill = rgb(56, 118, 29)),
    Rect(150, 250, 50, 50, fill = rgb(56, 118, 29)),
    Rect(250, 250, 50, 50, fill = rgb(56, 118, 29)),
    Rect(350, 250, 50, 50, fill = rgb(56, 118, 29)),
    Rect(0, 300, 50, 50, fill = rgb(56, 118, 29)),
    Rect(100, 300, 50, 50, fill = rgb(56, 118, 29)),
    Rect(200, 300, 50, 50, fill = rgb(56, 118, 29)),
    Rect(300, 300, 50, 50, fill = rgb(56, 118, 29)),
    Rect(50, 350, 50, 50, fill = rgb(56, 118, 29)),
    Rect(150, 350, 50, 50, fill = rgb(56, 118, 29)),
    Rect(250, 350, 50, 50, fill = rgb(56, 118, 29)),
    Rect(350, 350, 50, 50, fill = rgb(56, 118, 29))
)

map = Group(
    Rect(0, 0, 25, 25)
)

redTank = Group(
    # Body
    Rect(100, 100, 30, 50, fill = 'red'),
    # Treads
    Line(105, 100, 105, 150, fill = 'fireBrick', lineWidth = 5),
    Line(125, 100, 125, 150, fill = 'fireBrick', lineWidth = 5),
    # Turret
    Circle(115, 125, 10, fill = 'maroon'),
    Line(115, 125, 115, 155, fill = 'maroon', lineWidth = 7)
)
redTank.barrel = redTank.children[4]
redTank.healthBar = Group(
    Rect(redTank.centerX - 20, redTank.centerY - 50, 40, 10),
    Rect(redTank.centerX - 18, redTank.centerY - 48, 36, 6, fill = 'red')
)
# Probably the worst code I've ever written
redTank.healthBar.healthMeter = redTank.healthBar.children[1]


blueTank = Group(
    # Body
    Rect(100, 100, 30, 50, fill = 'blue'),
    # Treads
    Line(105, 100, 105, 150, fill = 'royalBlue', lineWidth = 5),
    Line(125, 100, 125, 150, fill = 'royalBlue', lineWidth = 5),
    # Turret
    Circle(115, 125, 10, fill = 'darkBlue'),
    Line(115, 125, 115, 155, fill = 'darkBlue', lineWidth = 7)
)
blueTank.barrel = blueTank.children[4]
blueTank.healthBar = Group(
    Rect(redTank.centerX - 20, redTank.centerY - 50, 40, 10),
    Rect(redTank.centerX - 18, redTank.centerY - 48, 36, 6, fill = 'cyan')
)
# Probably the worst code I've ever written
blueTank.healthBar.healthMeter = blueTank.healthBar.children[1]

# Set tank positions
redTank.centerX = 75
redTank.centerY = 120

blueTank.centerX = 325
blueTank.centerY = 120

# Variables
app.activeProjectiles = []
app.maxProjectileBounces = 4

redTank.health = 100
blueTank.health = 100

redTank.movementSpeed = 1
blueTank.movementSpeed = 1

redTank.rotationSpeed = 2
blueTank.rotationSpeed = 2

# Functions
# https://www.desmos.com/calculator/wqoaibbppt
def getMove(rotateAngle, multiplyAmount):
    moveAngle = math.radians(rotateAngle)
    
    moveX = (math.sin(moveAngle) * multiplyAmount)
    moveY = (-math.cos(moveAngle) * multiplyAmount)
    
    return (moveX, moveY)

def createProjectile(tank):
    projectile = Circle(tank.barrel.x2 , tank.barrel.y2, 3, fill = 'black', visible = False)
    projectile.rotateAngle = tank.rotateAngle
    projectile.owner = tank
    
    moveX, moveY = getMove(projectile.rotateAngle, -4)
    projectile.moveX = moveX
    projectile.moveY = moveY
    
    projectile.bounces = 0
    
    projectile.toFront()
    projectile.visible = True

    app.activeProjectiles.append(projectile)

def checkOutside(shape):
    if (shape.left > 400):
        return True
    if (shape.right < 0):
        return True
    if (shape.bottom < 0):
        return True
    if (shape.top > 400):
        return True
        
    return False
    
def checkWhoWins():
    if (redTank.health <= 0):
        # Red loses
        Label('Blue wins!', 200, 200)
        app.stop()
    if (blueTank.health <= 0):
        # Blue loses
        Label('Red wins!', 200, 200)
        app.stop()

def moveShape(shape, moveAmount, rotationAmount, collisionShapes, borderCollision):
    oldX = shape.centerX
    oldY = shape.centerY
    oldRotation = shape.rotateAngle
    
    moveX, moveY = getMove(oldRotation, moveAmount)

    shape.centerX += moveX
    shape.centerY += moveY
    
    shape.rotateAngle += rotationAmount
    
    # Return the main shape to its original position if hitting any of the collision shapes
    if (collisionShapes):
        for cShape in collisionShapes:
            if (shape.hitsShape(cShape)):
                shape.centerX = oldX
                shape.centerY = oldY
                
                shape.rotateAngle = oldRotation
                
    if (borderCollision):
        if (shape.top < 0):
            shape.top = 0
        if (shape.left < 0):
            shape.left = 0
        if (shape.right > 400):
            shape.right = 400
        if (shape.bottom > 400):
            shape.bottom = 400
            
def moveHealthBars():
    redTank.healthBar.centerX = redTank.centerX
    redTank.healthBar.centerY = redTank.centerY - 45
    
    blueTank.healthBar.centerX = blueTank.centerX
    blueTank.healthBar.centerY = blueTank.centerY - 45
    
    # Move the healthbar under the tank if its above the map
    if (redTank.healthBar.top < 0):
        redTank.healthBar.centerY = redTank.centerY + 45
    if (blueTank.healthBar.top < 0):
        blueTank.healthBar.centerY = blueTank.centerY + 45
        
def manageActiveProjectiles():
    for activeProjectile in app.activeProjectiles:
        # Blue tank hits the red tank
        if ((activeProjectile.hitsShape(redTank)) and (activeProjectile.owner != redTank)):
            redTank.health -= 25
            
            # I would do 9 but width cannot be 0 so this is good enough
            redTank.healthBar.healthMeter.width -= 8.9
            
            app.activeProjectiles.remove(activeProjectile)
            activeProjectile.visible = False
            
            checkWhoWins()
            
            continue
        
        # Red tank hits the blue tank
        if ((activeProjectile.hitsShape(blueTank)) and (activeProjectile.owner != blueTank)):
            blueTank.health -= 25
            
            # I would do 9 but width cannot be 0 so this is good enough
            blueTank.healthBar.healthMeter.width -= 8.9
            
            app.activeProjectiles.remove(activeProjectile)
            activeProjectile.visible = False
            
            checkWhoWins()
            
            continue
        
        if (activeProjectile.bounces < app.maxProjectileBounces):
            if ((activeProjectile.left <= 0) or (activeProjectile.right >= 400)):
                activeProjectile.moveX *= -1
                activeProjectile.bounces += 1
            if ((activeProjectile.top <= 0) or (activeProjectile.bottom >= 400)):
                activeProjectile.moveY *= -1
                activeProjectile.bounces += 1
        elif (activeProjectile.bounces == app.maxProjectileBounces):
            # Wait for the projectile to leave the map to smoothly remove
            if ((activeProjectile.right < 0) or (activeProjectile.left > 400) or (activeProjectile.top > 400) or (activeProjectile.bottom < 0)):
                app.activeProjectiles.remove(activeProjectile)
            
                activeProjectile.visible = False
            
                continue
        
        activeProjectile.centerX += activeProjectile.moveX
        activeProjectile.centerY += activeProjectile.moveY

# Events
def onKeyPress(key):
    # Make key letters lowercase to ignore shift
    key = key.lower()
    
    if (key == 'f'):
        createProjectile(redTank)
        
    if (key == 'enter'):
        createProjectile(blueTank)

def onKeyHold(keysUnsanitized):
    # Make all key letters lowercase to ignore shift
    keys = [key.lower() for key in keysUnsanitized]
    
    # Red Tank
    if ('w' in keys):
        moveShape(
            redTank, 
            moveAmount = -redTank.movementSpeed, 
            rotationAmount = 0, 
            collisionShapes = [
                blueTank
            ],
            borderCollision = True
        )
    if ('s' in keys):
        moveShape(
            redTank, 
            moveAmount = redTank.movementSpeed, 
            rotationAmount = 0, 
            collisionShapes = [
                blueTank
            ],
            borderCollision = True
        )
    if ('a' in keys):
        moveShape(
            redTank,
            moveAmount = 0,
            rotationAmount = redTank.rotationSpeed,
            collisionShapes = [
                blueTank
            ],
            borderCollision = True
        )
    if ('d' in keys):
        moveShape(
            redTank,
            moveAmount = 0,
            rotationAmount = -redTank.rotationSpeed,
            collisionShapes = [
                blueTank
            ],
            borderCollision = True
        )
    
    # Blue Tank
    if ('up' in keys):
        moveShape(
            blueTank,
            moveAmount = -blueTank.movementSpeed,
            rotationAmount = 0,
            collisionShapes = [
                redTank
            ],
            borderCollision = True
        )
    if ('down' in keys):
        moveShape(
            blueTank, 
            moveAmount = blueTank.movementSpeed, 
            rotationAmount = 0,
            collisionShapes = [
                redTank
            ],
            borderCollision = True
        )
    if ('left' in keys):
        moveShape(
            blueTank, 
            moveAmount = 0, 
            rotationAmount = blueTank.rotationSpeed,
            collisionShapes = [
                redTank
            ],
            borderCollision = True
        )
    if ('right' in keys):
        moveShape(
            blueTank,
            moveAmount = 0,
            rotationAmount = -blueTank.rotationSpeed,
            collisionShapes = [
                redTank
            ],
            borderCollision = True
        )
    
def onStep():
    moveHealthBars()
    
    manageActiveProjectiles()
        
app.stepsPerSecond = 60

print('Red Tank Controls:')
print('W - Move forward')
print('A - Rotate clockwise')
print('S - Move backward')
print('D - Rotate counter-clockwise')
print('F - Fire weapon')
print('\n')
print('Blue Tank Controls:')
print('Up    - Move forward')
print('Left  - Rotate clockwise')
print('Down  - Move backward')
print('Right - Rotate counter-clockwise')
print('Enter - Fire weapon')

cmu_graphics.run()