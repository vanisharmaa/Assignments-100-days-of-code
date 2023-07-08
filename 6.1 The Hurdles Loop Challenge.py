# Program for Reeborg's world to make a square 

def turn_right() :
    turn_left()
    turn_left()
    turn_left()

def make_square() :
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()    
    
make_square()
