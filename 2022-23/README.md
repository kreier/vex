# Season 2022-2023 "Spin Up"

Here are some sample codes for the robot brain:

``` py
def main():
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

vr_thread(main)
```
