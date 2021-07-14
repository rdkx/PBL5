int LED = 13;
int LED2 = 12;
int Button = 4;
int counter = 0;
int BPM = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(LED, OUTPUT);
  pinMode(Button, INPUT);
  pinMode(LED2, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(Button) == HIGH){
    digitalWrite(LED, LOW);
    counter++;
  } else {
    digitalWrite(LED, HIGH);
  }
}
