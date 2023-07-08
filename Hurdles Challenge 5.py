# Hurdles 5

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
    
def overcome_obstacle() :
    turn_left()
    while wall_on_right() :
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front() :
        move()
    turn_left()

while not at_goal() :
    if wall_in_front() :
        overcome_obstacle()
    else :
        move()
        
    
