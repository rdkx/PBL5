int Threshold = 480;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int Signal = analogRead(A0);
  Serial.println(Signal);

  delay(100);
}
