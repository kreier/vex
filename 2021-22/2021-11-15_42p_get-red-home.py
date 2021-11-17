#----------------------------------------------------------------------
#   
#   Project:            Get Red home
#   Description:        Both goals in red home zone
#                       
#   Date:               15.11.2021
#   Maximum score:      42 points
#   Time left:          39 seconds
#
#   Starting position:  A
#   Orientation:        Facing East (standard)
#   Preload:            Zero Rings
#
#----------------------------------------------------------------------

# Library imports
from vexcode_vrc import *

def move(direction, coordinate, reverse):
    global angle, x, y, head, dist
    angle = 0
    x = gps.x_position(MM)
    y = gps.y_position(MM)
    head = gps.heading()   # north is 0, but for the robot 0 is east - from start    
    monitor_variable("angle","dist","x","y","head") 
    if ( direction == "right" ):
        angle = 0
        dist = coordinate - gps.x_position(MM)
    if ( direction == "left" ):
        angle = 180
        dist = gps.x_position(MM) - coordinate
    if ( direction == "up" ):
        angle = 270
        dist = coordinate - gps.y_position(MM)
    if ( direction == "down" ):
        angle = 90
        dist = gps.y_position(MM) - coordinate
    drivetrain.turn_to_heading(angle, DEGREES, wait=True)
    if (reverse == 0):
        drivetrain.drive_for(FORWARD, dist, MM, wait=True)
    else:
        drivetrain.drive_for(REVERSE, -dist, MM, wait=True)

def pick_up():
    fork_motor_group.spin_to_position(1500, DEGREES, wait=True)

def set_down():
    fork_motor_group.spin_to_position(1800, DEGREES, wait=True)

# Add project code in "main"
def main():
    global stage
    monitor_variable("stage")
    drivetrain.set_drive_velocity(100,PERCENT)

    fork_motor_group.spin_to_position(1800, DEGREES, wait=False)
    stage = "Pick up red goal 1"    
    move("right",  -500, 0)
    move("up",    1500, 0)
    move("right",  920, 0)
    pick_up()
    move("up",    1500, 0)
    move("left",  -550, 0)
    set_down()

    stage = "Pick up red goal 2"    
    move("left",   950, 1)
    move("up",   -1150, 0)
    move("right", 1500, 0)
    move("up",    -900, 0)
    pick_up()
    move("up",   -1200, 0)
    move("right", -800, 0)
    move("down", -1300, 0)
    set_down()
    move("down", -1100, 1)
    stop_project()

# VR threads - Do not delete
vr_thread(main)