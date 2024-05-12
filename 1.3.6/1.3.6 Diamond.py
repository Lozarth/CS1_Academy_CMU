# Draws the background.
Rect(0, 0, 400, 400)

# Draw the diamond.
### (HINT: You will need two regular polygons and one star. The star should
#          be drawn second.)
### Place Your Code Here ###

RegularPolygon(200, 200, 150, 8, fill = gradient('aliceBlue', 'lightBlue', 'steelBlue'))

Star(200, 200, 150, 8, roundness = 10, fill = gradient('aliceBlue', 'aliceBlue', 'lightBlue'))

RegularPolygon(200, 200, 100, 8, fill = 'aliceBlue')