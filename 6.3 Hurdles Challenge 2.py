# Hurdles 2 challenge

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

while not(at_goal()):
    print(at_goal())
    path()
