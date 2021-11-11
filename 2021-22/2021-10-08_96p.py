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
