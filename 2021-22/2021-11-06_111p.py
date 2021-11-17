#----------------------------------------------------------------------
#   
#   Project:            GPS limits
#   Description:        Get more than 100 points with GPS
#                       Driving style: drive, check, correct
#   Date:               06.11.2021
#   Maximum score:      44 points
#   Time left:          39 seconds
#
#   Starting position:  A
#   Orientation:        Facing East (standard)
#   Preload:            Zero Rings
#
#----------------------------------------------------------------------

# Library imports
from vexcode_vrc import *

# Add project code in "main"
def main():
    # define fundamental variables and monitor them
    global stage, x, y, head
    x = gps.x_position(MM)
    y = gps.y_position(MM)
    head = gps.heading()   # north is 0, but for the robot 0 is east - from start
    stage = "Initiate system"
    monitor_sensor("bumper.pressing()")
    monitor_variable("stage", "x", "y", "head")
    drivetrain.set_drive_velocity(100,PERCENT)

    # Get 3 yellow goalposts into homezone
    stage = "Get 3 yellow goalposts"
    fork_motor_group.spin_to_position(1800, DEGREES, wait=False)
    drivetrain.turn_to_heading(0, DEGREES, wait=True)
    x = gps.x_position(MM)
    drivetrain.drive_for(FORWARD, - x - 980, MM, wait=True)
    drivetrain.turn_to_heading(90, DEGREES, wait=True) # south
    drivetrain.drive_for(FORWARD, 2250, MM, wait=True)
    drivetrain.turn_to_heading(0, DEGREES, wait=True)  # east
    x = gps.x_position(MM)
    drivetrain.drive_for(FORWARD, -180 - x, MM, wait=True)
    # pick up goal 1 at -180, -928
    fork_motor_group.spin_to_position(1500, DEGREES, wait=True)
    x = gps.x_position(MM)
    drivetrain.drive_for(FORWARD, -980 - x, MM, wait=True)
    stage = "Put first goal down"
    drivetrain.turn_to_heading(90, DEGREES, wait=True)
    fork_motor_group.spin_to_position(1800, DEGREES, wait=True)
    # place goal at -979, -949
    x = gps.x_position(MM)
    y = gps.y_position(MM)
    head = gps.heading()


    # Get second
    stage = "Get second yellow goalpost"
    y = gps.y_position(MM)
    drivetrain.drive_for(REVERSE, abs(-50 + y), MM, wait=True)
    drivetrain.turn_to_heading(0, DEGREES, wait=True)
    x = gps.x_position(MM)
    drivetrain.drive_for(FORWARD, -180 - x, MM, wait=True)   
    fork_motor_group.spin_to_position(1500, DEGREES, wait=True)
    # pick up goal 2 at -180, 7  
    x = gps.x_position(MM)
    y = gps.y_position(MM)
    head = gps.heading()
    drivetrain.drive_for(FORWARD, -980 - x, MM, wait=True)
    stage = "Put second goal down"
    drivetrain.turn_to_heading(90, DEGREES, wait=True)
    fork_motor_group.spin_to_position(1800, DEGREES, wait=True)
    # place goal at -972, -75 is different every time because rings
    x = gps.x_position(MM)
    y = gps.y_position(MM)
    head = gps.heading()


    # remove the blue goal
    stage = "remove the blue"
    y = gps.y_position(MM)
    drivetrain.drive_for(REVERSE, 1200 - y, MM, wait=True)
    drivetrain.turn_to_heading(180, DEGREES, wait=True)
    x = gps.x_position(MM)
    drivetrain.drive_for(FORWARD, abs(-1500 - x), MM, wait=True) 
    drivetrain.turn_to_heading(90, DEGREES, wait=True)
    y = gps.y_position(MM)
    drivetrain.drive_for(FORWARD, -(900 - y), MM, wait=True)
    fork_motor_group.spin_to_position(1400, DEGREES, wait=True)
    # pick up blue goal at -1500, 900  
    x = gps.x_position(MM)
    y = gps.y_position(MM)
    head = gps.heading()
    y = gps.y_position(MM)  
    drivetrain.drive_for(REVERSE, 1200 - y, MM, wait=True)
    stage = "Put second goal down"
    drivetrain.turn_to_heading(180, DEGREES, wait=True)
    drivetrain.turn_to_heading(270, DEGREES, wait=True)
    y = gps.y_position(MM)  
    drivetrain.drive_for(FORWARD, 1450 - y, MM, wait=True)    
    fork_motor_group.spin_to_position(1800, DEGREES, wait=True)  
    drivetrain.drive_for(REVERSE, 300, MM, wait=True)
    drivetrain.turn_to_heading(180, DEGREES, wait=True)
    x = gps.x_position(MM)
    drivetrain.drive_for(REVERSE, - x - 980, MM, wait=True)
    drivetrain.turn_to_heading(90, DEGREES, wait=True) # south    
    x = gps.x_position(MM)
    y = gps.y_position(MM)
    head = gps.heading()

    # Get third
    stage = "Get third yellow goalpost"
    y = gps.y_position(MM)
    drivetrain.drive_for(REVERSE, 900 - y, MM, wait=True)
    drivetrain.turn_to_heading(0, DEGREES, wait=True)
    x = gps.x_position(MM)
    drivetrain.drive_for(FORWARD, -180 - x, MM, wait=True)   
    fork_motor_group.spin_to_position(800, DEGREES, wait=False)
    wait(1,SECONDS)
    # pick up goal 3 at -180, 900  
    drivetrain.drive_for(REVERSE, 300, MM, wait=True)
    drivetrain.turn_to_heading(90, DEGREES, wait=True)
    drivetrain.turn_to_heading(180, DEGREES, wait=True)
    x = gps.x_position(MM)
    drivetrain.drive_for(FORWARD, abs(-1500 - x), MM, wait=True) 
    drivetrain.turn_to_heading(90, DEGREES, wait=True)
    y = gps.y_position(MM)
    drivetrain.drive_for(FORWARD, -(700 - y), MM, wait=True)
    fork_motor_group.spin_to_position(1800, DEGREES, wait=True)
    y = gps.y_position(MM)
    drivetrain.drive_for(FORWARD, -(-100 - y), MM, wait=True) 
    stop_project()

# VR threads - Do not delete
vr_thread(main)