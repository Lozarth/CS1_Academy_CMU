# Draws the background.
Rect(0, 0, 400, 250, fill=gradient('royalBlue', 'lightSkyBlue', start='top'))
Rect(0, 250, 400, 150, fill=gradient('navajoWhite', 'burlyWood'))

# Shadow
Oval(200, 300, 100, 20, fill = 'black', opacity = 20)

# Cactus
Oval(200, 235, 130, 140, fill = 'seaGreen', border = 'khaki', dashes = (4, 3))
Oval(200, 235, 100, 140, fill = rgb(55, 165, 90), border = 'khaki', dashes = (4, 3))
Oval(200, 235, 50, 140, fill = 'mediumSeaGreen', border = 'khaki', dashes = (4, 3))

Line(200, 165, 200, 305, fill = 'khaki', dashes = (4, 3))