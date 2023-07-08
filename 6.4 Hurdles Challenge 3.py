# Hurdles 3

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
    
while not at_goal() :
    if front_is_clear() :
        move()
    elif wall_in_front() :
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
    
