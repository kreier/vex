# pneumatic test version

vexcode_brain_precision = 0
vexcode_console_precision = 0
myVariable = 0

def when_started1():
    global myVariable, vexcode_brain_precision, vexcode_console_precision
    brain.screen.print("Start in 2 seconds")
    wait(2, SECONDS)
    digital_out_c.set(False)
    brain.screen.print("open in 2 seconds")
    wait(2, SECONDS)
    digital_out_c.set(True)
    wait(2, SECONDS)
    digital_out_c.set(False)
    brain.screen.print("And done")
    wait(2, SECONDS)
    # stop project not currently supported

when_started1()
