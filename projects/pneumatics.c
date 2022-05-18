// Initial idea from 2022-05-13

int Brain_precision = 0, Console_precision = 0;

float myVariable;

// "when started" hat block
int whenStarted1() {
  Brain.Screen.print("Start in 2 seconds");
  wait(2.0, seconds);
  DigitalOutC.set(false);
  Brain.Screen.print("open in 2 seconds");
  wait(2.0, seconds);
  DigitalOutC.set(true);
  wait(2.0, seconds);
  DigitalOutC.set(false);
  Brain.Screen.print("And done");
  wait(2.0, seconds);
  vexSystemExitRequest();
  return 0;
}


int main() {
  whenStarted1();
}
