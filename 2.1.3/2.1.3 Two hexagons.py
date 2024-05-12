def drawTwoHexagons(color):
    # Create two hexagons. Use the function parameter for the fill of the
    # top hexagon and the border of the bottom hexagon!
    ### Place Your Code Here ###
    RegularPolygon(
        200, 100,
        100,
        6,
        
        fill = color
    )
    
    RegularPolygon(
        200, 300,
        100,
        6,
        
        fill = None,
        border = color,
        borderWidth = 8
    )
    
    pass

##### Place your code above this line, code below is for testing purposes #####
# test case:
drawTwoHexagons('green')
