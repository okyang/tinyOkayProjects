int relay1 = 2; //D2
int relay2 = 3; //D3
int tweezers = 12; //D4
int board = 4; //D12

void setup() {
  pinMode(relay1, OUTPUT);
  pinMode(relay2, OUTPUT);
  pinMode(tweezers, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(tweezers) == LOW) {
    // Activate the TENS units 
    digitalWrite(relay1, HIGH);
    digitalWrite(relay2, HIGH);
    delay(2000);
  }
  else {
    digitalWrite(relay1, LOW);
    digitalWrite(relay2, LOW);
  }
  

}
