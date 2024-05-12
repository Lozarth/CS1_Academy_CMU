# sign
Rect(0, 0, 400, 400, fill='whiteSmoke')
Rect(20, 50, 360, 100, fill='gold', border='black')
Rect(20, 150, 360, 220, fill=rgb(40, 40, 40))
Label('Departures', 200, 87, size=36)
Label('TIME', 50, 135, size=14)
Label('DESTINATION', 200, 135, size=14)
Label('GATE', 340, 135, size=14)
Rect(33, 65, 45, 45, fill='white', border='black')
Polygon(44, 80, 50, 89, 43, 91, 37, 85, 41, 94, 73, 86, 75, 84, 70, 83, 57, 85)

# departed flights
Label('02:00', 50, 180, fill='dimGray', size=20, bold=True)
Label('Chicago', 200, 180, fill='dimGray', size=20, bold=True)
Label('C12', 355, 180, fill='dimGray', size=20, bold=True)
Label('03:00', 50, 230, fill='dimGray', size=20, bold=True)
Label('Toronto', 200, 230, fill='dimGray', size=20, bold=True)
Label('B97', 355, 230, fill='dimGray', size=20, bold=True)
Label('03:30', 50, 280, fill='dimGray', size=20, bold=True)
Label('Reykjavik', 200, 280, fill='dimGray', size=20, bold=True)
Label('A82', 355, 280, fill='dimGray', size=20, bold=True)

def updateDepartingFlights(time, destination, gate):
    # Update the flight information below.
    ### Fix Your Code Here ###
    Label(time, 50, 330, fill='whiteSmoke', size=20, bold=True)
    Label(destination, 200, 330, fill='whiteSmoke', size=20, bold=True)
    Label(gate, 355, 330, fill='whiteSmoke', size=20, bold=True)

##### Place your code above this line, code below is for testing purposes #####
# test case:
updateDepartingFlights('04:00', 'Madrid', 'D82')
