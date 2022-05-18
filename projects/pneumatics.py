# 2022-05-13 pneumatic test version
# 2022-05-18 test time 1 second, with 100 psi up to 40 cycles

vexcode_brain_precision = 0
vexcode_console_precision = 0
myVariable = 0
cycles = 0

def when_started1():
    global myVariable, cycles, vexcode_brain_precision, vexcode_console_precision
    cycles = 1
    brain.screen.print("Start in 2 second")
    brain.screen.next_row()
    digital_out_c.set(False)
    wait(2, SECONDS)
    while True:
        for repeat_count in range(10):
            brain.screen.print("Open for 1 sec, ")
            digital_out_c.set(True)
            wait(1, SECONDS)
            brain.screen.print("and closed for 1 sec. ")
            digital_out_c.set(False)
            brain.screen.print(cycles, precision=6 if vexcode_brain_precision is None else vexcode_brain_precision)
            brain.screen.next_row()
            wait(1, SECONDS)
            cycles = cycles + 1
            wait(5, MSEC)
        brain.screen.set_cursor(1, 1)
        for repeat_count2 in range(11):
            brain.screen.print("                                                                 .")
            brain.screen.next_row()
            wait(5, MSEC)
        brain.screen.set_cursor(1, 1)
        wait(5, MSEC)
    # stop project not currently supported

when_started1()
