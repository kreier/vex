// 2022-05-13 initial idea
// 2022-05-18 cycle down to 1 second, up to 45 with 100 psi

int Brain_precision = 0, Console_precision = 0;

float myVariable, cycles;

// "when started" hat block
int whenStarted1() {
  cycles = 1.0;
  Brain.Screen.print("Start in 2 second");
  Brain.Screen.newLine();
  DigitalOutC.set(false);
  wait(2.0, seconds);
  while (true) {
    repeat(10) {
      Brain.Screen.print("Open for 1 sec, ");
      DigitalOutC.set(true);
      wait(1.0, seconds);
      Brain.Screen.print("and closed for 1 sec. ");
      DigitalOutC.set(false);
      Brain.Screen.print(printToBrain_numberFormat(), static_cast<float>(cycles));
      Brain.Screen.newLine();
      wait(1.0, seconds);
      cycles = cycles + 1.0;
      wait(5, msec);
    }
    Brain.Screen.setCursor(1, 1);
    repeat(11) {
      Brain.Screen.print("                                                                 .");
      Brain.Screen.newLine();
      wait(5, msec);
    }
    Brain.Screen.setCursor(1, 1);
  wait(5, msec);
  }
  vexSystemExitRequest();
  return 0;
}


int main() {
  // post event registration

  // set default print color to black
  printf("\033[30m");

  // wait for rotation sensor to fully initialize
  wait(30, msec);

  whenStarted1();
}
