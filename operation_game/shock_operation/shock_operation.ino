// initialize variables for used pins
int relay1 = 2; //D2
int relay2 = 3; //D3

int tweezers = 12; //D4

void setup() {
  Serial.begin(9600);

  pinMode(relay1, OUTPUT);
  pinMode(relay2, OUTPUT);
  pinMode(tweezers, INPUT);
}

void loop() {
  // detect if circuit was closed
  if (digitalRead(tweezers) == LOW) {
    Serial.println("Yikes");

    // Activate Relay 1 and Relay 2
    digitalWrite(relay1, HIGH);
    digitalWrite(relay2, HIGH);

    // keep on for 2 seconds
    delay(2000);

    // turn off the relays
    digitalWrite(relay1, LOW);
    digitalWrite(relay2, LOW);

    // keep off for 1 seconds
    delay(1000);
  }
  else {
    // turn off the relays
    digitalWrite(relay1, LOW);
    digitalWrite(relay2, LOW);
  }


}
