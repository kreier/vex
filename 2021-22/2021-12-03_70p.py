#----------------------------------------------------------------------
#   
#   Project:            New goto funtion
#   Description:        Just point the target coordinates
#                       
#   Date:               03.12.2021
#   Maximum score:      70 points
#   Time left:          31 seconds
#
#   Starting position:  A
#   Orientation:        Facing East (standard, 0 for the robot)
#   Preload:            Zero Rings
#
#----------------------------------------------------------------------

# Library imports
from vexcode_vrc import *
from math import sqrt

def goto(target_x, target_y, reverse):
    global angle, x1, y1, x2, y2, delta_x, delta_y, head, distance, directio
    angle = 0
    x1 = gps.x_position(MM)
    y1 = gps.y_position(MM)
    x2 = target_x
    y2 = target_y
    head = gps.heading()   # north is 0, but for the robot 0 is east - from start
    delta_x = x2 - x1
    delta_y = y2 - y1
    distance = math.sqrt(delta_x**2 + delta_y**2)     # pythagorean theorem
    if ( delta_x ):
        directio = - math.atan(delta_y / delta_x) * 180 / math.pi
    else:
        directio = 90

    if ( delta_x < 0 ):
        directio = directio + 180

    monitor_variable("angle","x1","y1", "x2", "y2", "delta_x", "delta_y","head", "distance", "directio")
    drivetrain.turn_to_heading(directio, DEGREES, wait=True)
    if (reverse == 0):
        drivetrain.drive_for(FORWARD, distance, MM, wait=True)
    else:
        drivetrain.drive_for(REVERSE, -distance, MM, wait=True)

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
        angle = -180
        dist = gps.x_position(MM) - coordinate
    if ( direction == "up" ):
        angle = -90 # 270
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

#    goto( -1020, 1320, 0)
#    goto(  -920, 1220, 0)
    goto(  -920, 1320, 0)
    goto(  -920,-1450, 0)
    pick_up()
    goto(   400,-1200, 0)
    set_down()
    goto(   600,-1400, 1)

#    goto( -500, 1320, 0)
#    goto( -500, 1500, 0)
    goto(  920, 1500, 0)
    pick_up()
    goto(  920, 1510, 0)
    goto( -550, 1510, 0)
    set_down()



#    move("right",  -500, 0)
#    move("up",    1500, 0)
#    move("right",  920, 0)
#    pick_up()
#    move("up",    1500, 0)
#    move("left",  -550, 0)
#   set_down()


    stage = "Pick up red goal 2"    
    move("left",   950, 1)
    move("up",   -1150, 0)
    move("right", 1500, 0)
    move("up",    -900, 0)
    pick_up()
    move("up",     100, 0)
    set_down()
    wait(3,SECONDS)
    stop_project()


 #   move("up",   -1200, 0)
 #   move("right", -800, 0)
 #   move("down", -1300, 0)
 #   set_down()
 #   move("down", -1100, 1)
 #   stop_project()

# VR threads - Do not delete
vr_thread(main)