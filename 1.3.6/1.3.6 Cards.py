# Draws the background and blank cards.
Rect(0, 0, 400, 400, fill=gradient('darkGreen', 'forestGreen', start='top'))
Rect(90, 50, 180, 280, fill=rgb(245, 245, 245))
Rect(130, 70, 180, 280, fill='white')

# Draw the suit and numbers on top of the cards.
### Place Your Code Here ###

# Diamonds
Star(110, 100, 15, 4, roundness=65, fill = 'crimson')
Star(150, 120, 15, 4, roundness=65, fill = 'crimson')
Star(220, 210, 25, 4, roundness=65, fill = 'crimson')
Star(280, 320, 15, 4, roundness=65, fill = 'crimson')

# Letters
Label('2', 110, 70, size = 30, font = 'monospace', fill = 'crimson', bold = True)
Label('A', 150, 90, size = 30, font = 'monospace', fill = 'crimson', bold = True)
Label('A', 280, 290, size = 30, font = 'monospace', fill = 'crimson', bold = True)