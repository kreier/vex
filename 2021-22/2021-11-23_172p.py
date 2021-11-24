#----------------------------------------------------------------------
#   
#   Project:            Get Red home
#   Description:        Both goals in red home zone
#                       
#   Date:               23.11.2021
#   Maximum score:      172 points
#   Time left:          4 seconds
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
    stage = "Initiate system"
    monitor_variable("stage")
    drivetrain.set_drive_velocity(100,PERCENT)

    fork_motor_group.spin_to_position(1800, DEGREES, wait=False)
    move("right", -920, 0)
    stage = "Pick up red goal 1"    
    move("up",    1500, 0)
    move("right",  920, 0)    
    pick_up()
    move("left", -1500, 0)
    move("up",    1450, 0)
    set_down()
    move("up",    1150, 1)

    stage = "Pick up red goal 2"    
    move("right", -950, 0)
    move("down",  -500, 0)
    move("right",  950, 0)
    move("down", -1150, 0)
    move("right", 1500, 0)
    move("up",    -900, 0)
    pick_up()
    move("up",   -1200, 0)
    move("right", -900, 0)
    move("down", -1300, 0)
    set_down()
    move("down", -1100, 0)



    move("right", -900, 1)

    move("down",  -930, 0)
    move("right", -180, 0)
    pick_up()
    move("right", -930, 0)
    move("down",  -950, 0)
    set_down()

    stage = "Get 2nd yellow goal"
    move("down",   -50, 1)
    move("right", -180, 0)
    pick_up()
    move("right", -850, 0)
    move("down",   -70, 0)
    set_down()

    stage = "Remove the blue goal"
    move("down",  1200, 1)
    move("left", -1500, 0)
    move("down",   900, 0)
    pick_up()
    move("down",  1200, 0)
    stage = "Put blue goal down"
    drivetrain.turn_to_heading(180, DEGREES, wait=True)
    move("up",    1450, 0)
    set_down()
    move("up",    1150, 1)
 
    stage = "Get 3rd yellow goal"
    move("left",  -980, 1)
    move("down",   900, 0)
    move("right", -180, 0)
    pick_up()
    fork_motor_group.spin_to_position(400, DEGREES, wait=False)
    move("right", -500, 0)
    move("down",   920, 0)
    move("left", -1500, 1)
    move("down",   600, 0)
    set_down()
    move("down",  -100, 0)
    wait(2,SECONDS)
    stop_project()

# VR threads - Do not delete
vr_thread(main)