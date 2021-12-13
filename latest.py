# 130 points - 60 lines - 30 seconds - 09.12.2021
from vexcode_vrc import *
from math import sqrt

def main():
    drivetrain.set_drive_velocity(100,PERCENT)
    fork_motor_group.spin_to_position(1800, DEGREES, wait=False)
    goto( -920,  920, 0)
    goto( -920,-1450, 0)
    goto(  750,-1400, 0) # blue in right zone
    goto(  500,-1150, 1)
#   goto(    0, -950, 0) # m = - 2/5
    goto( -600, -710, 0) # yellow in left zone
    goto(  400, -250, 1)
    goto(    0,    0, 0) # m = - 5/8
    goto( -600,  200, 0) # yellow in left zone
    goto(  400,  400, 1)
    goto(    0,  950, 0)
    goto( -600,  950, 0) # yellow in left zone
    goto(  920,  950, 1)
    goto(  920, 1500, 0)
    goto( -600, 1320, 0) # red in left zone
    goto(  600,  600, 1)
    goto(  600, -600, 1)
    goto( 1400,-1350, 1)
    goto( 1500, -900, 0) # red on balance
    pick_up() 
    goto( 1500,  100, 0)
    stop_project()

def goto(target_x, target_y, reverse):
    x1 = gps.x_position(MM)
    y1 = gps.y_position(MM)
    delta_x = target_x - x1
    delta_y = target_y - y1
    distance = math.sqrt(delta_x**2 + delta_y**2)     # pythagorean theorem
    if ( delta_x == 0 ):
        if ( delta_y < 0):
            direction = 90
        else:
            direction = 270
    else:
        direction = - math.atan(delta_y / delta_x) * 180 / math.pi
    if ( delta_x < 0 ):
        direction = direction + 180
    if ( reverse != 0 ):
        direction = direction + 180
    if ( direction > 360 ):
        direction = direction - 360
    drivetrain.turn_to_heading(direction, DEGREES, wait=True)
    if ( reverse != 0 ):
        drivetrain.drive_for(REVERSE, distance, MM, wait=True)
    else:
        drivetrain.drive_for(FORWARD, distance, MM, wait=True)
def pick_up():
    fork_motor_group.spin_to_position(1500, DEGREES, wait=True)
def set_down():
    fork_motor_group.spin_to_position(1800, DEGREES, wait=True)

vr_thread(main)
