# Hurdle 1 - https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

def turn_right() :
    turn_left()
    turn_left()
    turn_left()
    
def moveAndTurnRight() :
    move()
    turn_right()
    
def moveAndTurnLeft() :
    move()
    turn_left()
    
def path() :
    moveAndTurnLeft()
    moveAndTurnRight()
    moveAndTurnRight()
    moveAndTurnLeft()

for i in range(0, 6) :
    path()
