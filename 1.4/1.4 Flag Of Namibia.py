# background
Rect(0, 0, 400, 400, fill='whiteSmoke')

Label('Namibia', 200, 50, size = 30)

Rect(
    5, 100, 
    390, 
    265,
    
    fill = 'white'
)

# Draw the flag of Namibia.
### (HINT: The sun is drawn using one star and one circle with a border.)
### Place Your Code Here ###

PrussianBlue = rgb(0, 60, 125)
CrimsonRed = rgb(210, 15, 50)
PigmentGreen = rgb(0, 150, 65)
Gold = rgb(255, 215, 0)

Polygon(
    5, 100, 
    315, 100, 
    5, 310,
    
    fill = PrussianBlue
)

Star(
    84, 174,
    40,
    12,
    
    fill = Gold
)

Circle(
    84, 174,
    25,
    
    fill = Gold,
    border = PrussianBlue,
    borderWidth = 5
)

Polygon(
    335, 100,
    395, 100,
    395, 140,
    65, 365,
    5, 365,
    5, 325,
    
    fill = CrimsonRed
)

Polygon(
    395, 155,
    395, 365,
    85, 365,
    
    fill = PigmentGreen
)
