# Documentation of programming progress

Starting in September 2021 we slowly moved from the blocky code to python. And our scores increased as well. Here just 43 points:

``` py
def when_started1():
    global myVariable
    fork_motor_group.spin_to_position(1100, DEGREES, wait=False)
    drivetrain.turn_for(RIGHT, 22, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 1200, MM, wait=True)
    drivetrain.drive_for(REVERSE, 100, MM, wait=True)
    drivetrain.turn_for(LEFT, 20, DEGREES, wait=True)
    fork_motor_group.spin_to_position(1800, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 200, MM, wait=True)
    fork_motor_group.spin_to_position(1300, DEGREES, wait=True)
    drivetrain.drive_for(REVERSE, 700, MM, wait=True)
    drivetrain.turn_to_heading(270, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 500, MM, wait=True)
    fork_motor_group.spin_to_position(1800, DEGREES, wait=True)
    drivetrain.drive_for(REVERSE, 300, MM, wait=True)
    drivetrain.turn_to_heading(350, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 1400, MM, wait=True)
    drivetrain.turn_to_heading(320, DEGREES, wait=True)
    fork_motor_group.spin_to_position(1100, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 200, MM, wait=True)
    fork_motor_group.spin_to_position(1200, DEGREES, wait=True)
    drivetrain.drive_for(REVERSE, 300, MM, wait=True)
    fork_motor_group.spin_to_position(1800, DEGREES, wait=False)
    drivetrain.turn_to_heading(340, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 400, MM, wait=True)
    fork_motor_group.spin_to_position(1200, DEGREES, wait=True)
    drivetrain.drive_for(REVERSE, 1600, MM, wait=True)
    stop_project()

vr_thread(when_started1)
```

By October 8th we gained already 96 points:

``` py
myVariable = 0

def when_started1():
    global myVariable
    fork_motor_group.spin_to_position(1100, DEGREES, wait=False)
    drivetrain.turn_for(RIGHT, 22, DEGREES, wait=True)

    # Get goalpost with 2 rings into our zone (22 points)
    drivetrain.drive_for(FORWARD, 1200, MM, wait=True)
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)
    drivetrain.drive_for(REVERSE, 100, MM, wait=True)
    drivetrain.turn_for(LEFT, 20, DEGREES, wait=True)
    fork_motor_group.spin_to_position(1800, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 200, MM, wait=True)
    fork_motor_group.spin_to_position(1300, DEGREES, wait=True)
    drivetrain.drive_for(REVERSE, 800, MM, wait=True)
    drivetrain.turn_to_heading(90, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 800, MM, wait=True)
    fork_motor_group.spin_to_position(1800, DEGREES, wait=True)
    drivetrain.drive_for(REVERSE, 1200, MM, wait=True)

    # Remove blue goalpost from lever
    drivetrain.turn_to_heading(130, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 600, MM, wait=True)
    fork_motor_group.spin_to_position(1300, DEGREES, wait=True)
    drivetrain.drive_for(REVERSE, 500, MM, wait=True)
    drivetrain.turn_to_heading(90, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 750, MM, wait=True)
    fork_motor_group.spin_to_position(1800, DEGREES, wait=True)
    drivetrain.drive_for(REVERSE, 580, MM, wait=True)

    # Get red goalpost
    drivetrain.turn_to_heading(0, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 1600, MM, wait=True)
    fork_motor_group.spin_to_position(1100, DEGREES, wait=True)
    drivetrain.turn_to_heading(320, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 300, MM, wait=True)
    drivetrain.drive_for(REVERSE, 300, MM, wait=True)
    fork_motor_group.spin_to_position(1800, DEGREES, wait=True)
    drivetrain.turn_to_heading(300, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 400, MM, wait=True)
    fork_motor_group.spin_to_position(0, DEGREES, wait=False)
    drivetrain.drive_for(REVERSE, 300, MM, wait=True)
    drivetrain.turn_to_heading(0, DEGREES, wait=True)
    drivetrain.drive_for(REVERSE, 1900, MM, wait=True)

    # Get on the balance
    drivetrain.set_drive_velocity(50, PERCENT)
    drivetrain.set_turn_velocity(50, PERCENT)
    drivetrain.turn_to_heading(125, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 400, MM, wait=True)
    drivetrain.turn_to_heading(90, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 200, MM, wait=True)
    fork_motor_group.spin_to_position(1700, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 750, MM, wait=True)
    drivetrain.stop()
    wait(1, SECONDS)
    stop_project()

vr_thread(when_started1)
```

With the help of the GPS sensor on November 1st the score jumped to 101.

``` py
myVariable = 0


def when_started1():
   global myVariable

   # put the blue in  the middle of the platform
   fork_motor_group.spin_to_position(1800, DEGREES, wait=False)
   drivetrain.turn_to_heading(98, DEGREES, wait=True)
   wait(2, SECONDS)
   drivetrain.drive_for(FORWARD, 450, MM, wait=True)
   fork_motor_group.spin_to_position(1400, DEGREES, wait=True)
   drivetrain.drive_for(FORWARD, 100, MM, wait=True)
   drivetrain.turn_to_heading(90, DEGREES, wait=True)
   drivetrain.drive_for(FORWARD, 700, MM, wait=True)
   fork_motor_group.spin_to_position(1800, DEGREES, wait=True)
   drivetrain.drive_for(REVERSE, 900, MM, wait=True)

   # put yellow on lever
   drivetrain.turn_to_rotation(4, DEGREES, wait=True)
   fork_motor_group.spin_to_position(1800, DEGREES, wait=False)
   drivetrain.drive_for(FORWARD, 1350, MM, wait=True)
   fork_motor_group.spin_to_position(800, DEGREES, wait=False)
   drivetrain.set_drive_velocity(70, PERCENT)
   while gps.x_position(MM) > -1400:
       drivetrain.drive(REVERSE)
       wait(5, MSEC)
   drivetrain.stop()
   drivetrain.turn_to_heading(97, DEGREES, wait=True)
   drivetrain.drive_for(FORWARD, 350, MM, wait=True)
   fork_motor_group.spin_to_position(1750, DEGREES, wait=True)
   drivetrain.drive_for(FORWARD, 100, MM, wait=True)
   drivetrain.turn_to_rotation(93, DEGREES, wait=True)
   drivetrain.drive_for(FORWARD, 470, MM, wait=True)
   fork_motor_group.spin_to_position(1800, DEGREES, wait=True)
   wait(1, SECONDS)
   drivetrain.drive_for(REVERSE, 1070, MM, wait=True)

   # get red in our sector
   drivetrain.turn_to_heading(-6, DEGREES, wait=True)
   drivetrain.drive_for(FORWARD, 2200, MM, wait=True)
   fork_motor_group.spin_to_position(1400, DEGREES, wait=True)
   while gps.x_position(MM) > -800:
       drivetrain.drive(REVERSE)
       wait(5, MSEC)
   drivetrain.stop()
   drivetrain.set_turn_velocity(100, PERCENT)
   drivetrain.turn_to_rotation(-90, DEGREES, wait=True)
   fork_motor_group.spin_to_position(1800, DEGREES, wait=True)
   drivetrain.drive_for(REVERSE, 1100, MM, wait=True)

   # get second yellow in our sector
   while gps.y_position(MM) > 50:
       drivetrain.drive(REVERSE)
       wait(5, MSEC)
   drivetrain.turn_to_heading(0, DEGREES, wait=True)
   drivetrain.drive_for(FORWARD, 900, MM, wait=True)
   fork_motor_group.spin_to_position(1400, DEGREES, wait=True)
   drivetrain.drive_for(REVERSE, 900, MM, wait=True)
   drivetrain.turn_to_heading(270, DEGREES, wait=True)
   fork_motor_group.spin_to_position(1800, DEGREES, wait=True)
   drivetrain.drive_for(REVERSE, 920, MM, wait=True)

   # get third yellow in our sector
   drivetrain.turn_to_heading(0, DEGREES, wait=True)
   drivetrain.drive_for(FORWARD, 1200, MM, wait=True)
   fork_motor_group.spin_to_position(1400, DEGREES, wait=True)
   drivetrain.turn_to_heading(180, DEGREES, wait=True)
   drivetrain.drive_for(FORWARD, 1200, MM, wait=True)
   fork_motor_group.spin_to_position(1800, DEGREES, wait=True)
   drivetrain.turn_to_heading(190, DEGREES, wait=True)
   drivetrain.drive_for(REVERSE, 2200, MM, wait=True)
   drivetrain.turn_to_heading(270, DEGREES, wait=True)
   drivetrain.drive_for(FORWARD, 700, MM, wait=True)
   fork_motor_group.spin_to_position(1400, DEGREES, wait=True)
   drivetrain.drive_for(FORWARD, 700, MM, wait=True)
   stop_project()


vr_thread(when_started1)
```

And finally on November 8th with the new programmed move(direction, distance, reverse) function we scored 130 points, using a much easier to read codel

``` py
#----------------------------------------------------------------------
#   
#   Project:            Calling GPS functions
#   Description:        Get more than 100 points with GPS
#                       Driving style: drive, check, correct
#   Date:               08.11.2021
#   Maximum score:      130 points
#   Time left:          10 seconds
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
    drivetrain.set_drive_velocity(60,PERCENT)

    stage = "Get 1st yellow goal"
    fork_motor_group.spin_to_position(1800, DEGREES, wait=False)
    move("right", -920, 0)
    move("down", -1300, 0)
    pick_up()
    move("right", 1000, 0)
    set_down()
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
    stop_project()

# VR threads - Do not delete
vr_thread(main)
```
