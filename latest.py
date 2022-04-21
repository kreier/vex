from vexcode_vrc import *  # 130 points - 38 lines - 30 seconds - 20.04.2022
from math import sqrt
path = [[-920,  920, 0],[-920,-1450, 0],[750, -1400, 0],[ 500,-1150, 1],[-600, -710, 0],
        [ 400, -250, 1],[   0,    0, 0],[-600,  200, 0],[ 400,  400, 1],[   0,  950, 0],
        [-600,  950, 0],[ 920,  950, 1],[ 920, 1500, 0],[-600, 1320, 0],[ 600,  600, 1],
        [ 600, -600, 1],[1400,-1350, 1],[1500, -900, 0]]
def goto(target_x, target_y, reverse):  # only 21 lines for goto function
    x1 = gps.x_position(MM)
    y1 = gps.y_position(MM)
    delta_x = target_x - x1
    delta_y = target_y - y1
    direction_fr = FORWARD          # direction either FORWARD or REVERSE fr
    distance = math.sqrt(delta_x**2 + delta_y**2)     # pythagorean theorem
    if ( delta_x == 0 ):            # can't divide by zero, vertical motion
        direction = 90              # standard: drive upwards
        if ( delta_y > 0):
            direction = 270         # otherwise downwards
    else:
        direction = - math.atan(delta_y / delta_x) * 180 / math.pi
    if ( delta_x < 0 ):             # atan range is [-180|180] but need [0|360] 
        direction += 180
    if ( reverse is 1 ):            # driving reverse in opposite direction
        direction += 180
        direction_fr = REVERSE
    direction = direction % 360     # with the modulo % operator, range < 360 
    drivetrain.turn_to_heading(direction, DEGREES, wait=True)   # (1) DIRECTION
    drivetrain.drive_for(direction_fr, distance, MM, wait=True) # (2) DRIVING
def pick_up():
    fork_motor_group.spin_to_position(1500, DEGREES, wait=True)
def main():                         # five steps to 130 points
    drivetrain.set_drive_velocity(100, PERCENT)
    fork_motor_group.spin_to_position(1800, DEGREES, wait=False)
    for x, y, r in path:            # loop for all coordinates in path array
        goto(x, y, r)
    pick_up() 
    goto( 1500,  100, 0)
    stop_project()
vr_thread(main)