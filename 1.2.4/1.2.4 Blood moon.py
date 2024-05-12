# Use gradients to draw the two rectangles.
### (HINT: The gradients use both rgb and named colors!)
### Place Your Code Here ###

brownRed = rgb(60, 20, 20)
reddishBrown = rgb(150, 50, 0)
deepBlue = rgb(20, 20, 100)


Rect(0, 0, 400, 300, fill = gradient('orangeRed', brownRed, 'black'))

Rect(0, 300, 400, 100, fill = gradient(reddishBrown, deepBlue))