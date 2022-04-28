# Team 76209X - SSIS Dragons X - 28.04.2022
# 142 points, 13 seconds remaining

from vexcode_vrc import *
from math import sqrt

def main():
    drivetrain.set_drive_velocity(100,PERCENT)
    fork_motor_group.set_velocity(100,PERCENT)
    fork_motor_group.spin_to_position(1800, DEGREES, wait=True)

    brain.screen.clear_screen()
    brain.screen.print("SSIS Dragon X starting.\n")

    brain.screen.print("Get blue in the right zone.\n")
    goto( -920,  920, 0)
    goto( -920,-1450, 0)        # location of bottom blue
    goto(  750,-1400, 0)        # blue in right zone
    brain.screen.print("Done.\n")
    goto(  500,-1150, 1)

#   goto(    0, -950, 0) # m = - 2/5
#    goto( -600, -710, 0) # yellow in left zone
    goto(  400, -250, 1)

    brain.screen.print("Get middle yellow in left zone.\n")
    goto(    0,    0, 0)        # location middle yellow goal
    goto( -600,  200, 0)        # yellow in left zone
    brain.screen.print("Done.\n")
    goto(  400,  400, 1)

    brain.screen.print("Top yellow into left zone.\n")
    goto(    0,  950, 0)        # location top yellow goal
    goto( -600,  950, 0)        # yellow in left zone
    brain.screen.print("Done.\n")

    brain.screen.print("Top red into the left zone.\n")
    goto(  920,  950, 1)
    goto(  920, 1500, 0)        # location red goal
    goto( -600, 1320, 0)        # red in left zone
    brain.screen.print("Done.\n")

    brain.screen.print("Get bottom red goal in left zone.\n")
    goto(  600,  600, 1)
    goto(  600, -600, 1)
    goto( 1400,-1350, 1)        
    goto( 1500, -900, 0)        # location bottom red goal
    pick_up()                   # get red over the platform
    brain.screen.print("Drive over the platform.\n")
    goto( 1500,  900, 0)
    goto( 1400, 1000, 0)
    goto( -600,  500, 0)
    brain.screen.print("Red goal is in the left zone.\n")
    set_down()
    brain.screen.print("Done.\n")



    brain.screen.print("Put the bottom blue on the platform.\n")
    goto(  750, -750, 1)
    goto(  750,-1400, 0)        # new location of blue goal
    pick_up() 
    fork_motor_group.spin_to_position(600, DEGREES, wait=False)
    goto( 1400,-1350, 1)
    goto( 1480, -850, 0)
    brain.screen.print("Push platform down.\n")
    set_down()                  # blue on balance
    fork_motor_group.spin_to_position(1850, DEGREES, wait=False)
    wait(2,SECONDS)
    goto( 1500, -100, 0)
    brain.screen.print("Done.\n")

    brain.screen.print("Get bottom yellow goal on the platform.\n")
    goto( 1400,-1350, 1)
    goto(    0, -950, 0)        # get one more yellow
    pick_up() 
    fork_motor_group.spin_to_position(700, DEGREES, wait=False)
    goto( 1400,-1350, 1)
    goto( 1450, -850, 0)        # yellow on balance
    set_down()
    goto( 1500, -50, 0)
    brain.screen.print("Done.\n")
    wait(1,SECONDS)


    brain.screen.print("Get top blue goal.\n")
    wait(0.5, SECONDS)
    goto(-1480, 1000, 0)
    goto(-1500,  750, 0)
    pick_up()
    goto(-1500,  850, 1)
    goto(    0,  700, 0)
    goto(  900,  700, 0)
    goto(  700,  800, 1)

    stop_project()

def goto(target_x, target_y, reverse):
    x1 = gps.x_position(MM)
    y1 = gps.y_position(MM)
    delta_x = target_x - x1
    delta_y = target_y - y1
    direction_fr = FORWARD          # direction either FORWARD or REVERSE fr
    distance = math.sqrt(delta_x**2 + delta_y**2)     # pythagorean theorem
    if ( delta_x == 0 ):            # can't divide by zero, vertical motion
        direction = 90              # standard: drive upwards
        if ( delta_y > 0):
            direction = 270         # otherwise down
    else:
        direction = - math.atan(delta_y / delta_x) * 180 / math.pi
    if ( delta_x < 0 ):             # atan range is [-180|180], but we need [0|360] 
        direction += 180
    if ( reverse is 1 ):            # driving reverse in oposite calculated direction
        direction += 180
        direction_fr = REVERSE
    direction = direction % 360     # with the modulo % operator, range < 360 degrees
    drivetrain.turn_to_heading(direction, DEGREES, wait=True)
    drivetrain.drive_for(direction_fr, distance, MM, wait=True)

def pick_up():
    fork_motor_group.spin_to_position(1500, DEGREES, wait=True)

def set_down():
    fork_motor_group.spin_to_position(1800, DEGREES, wait=True)

vr_thread(main)
