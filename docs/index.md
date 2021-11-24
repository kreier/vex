# VEX

Programs for team 76209X of the SSIS Dragons X. Code, functions and highscores constantly improve.

## Highscore

- 09/27/2021 43 points
- 10/08/2021 96 points
- 11/01/2021 102 points
- 11/06/2021 111 points
- 11/08/2021 130 points
- 11/23/2021 172 points

![Screenshot of 132 points](2021-11-08_132p.png)

## Latest code

Created November 8th. With the new `move(direction, coordinate, reverse)` function.

Possible update: rewrite the `move` function to `move( x-coordinate, y-coordinate, reverse)` and adjust the direction with starting position (GPS) and trigonometry. And then add more locations within one minute.

``` py
----------------------------------------------------------------------
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

## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/kreier/vex/edit/gh-pages/docs/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/kreier/vex/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
