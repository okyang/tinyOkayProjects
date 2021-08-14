/*
Resources:
- https://randomnerdtutorials.com/installing-esp8266-nodemcu-arduino-ide-2-0/
- https://learn.adafruit.com/adafruit-io/mqtt-api
- https://randomnerdtutorials.com/esp8266-pinout-reference-gpios/
- https://learn.adafruit.com/pm25-air-quality-sensor/arduino-code
- https://learn.adafruit.com/diy-air-quality-monitor
- https://learn.adafruit.com/adafruit-io-basics-temperature-and-humidity
*/

#include "Adafruit_PM25AQI.h"


/* You need to create your own "config.h" file in the same
directory as this file
*/
#include "config.h"

#include <ESP8266WiFi.h>
#include "Adafruit_MQTT.h"
#include "Adafruit_MQTT_Client.h"



// If your PM2.5 is UART only, for UNO and others (without hardware serial)
// we must use software serial...
// pin #2 is IN from sensor (TX pin on sensor), leave pin #3 disconnected
// comment these two lines if using hardware serial
#include <SoftwareSerial.h>
SoftwareSerial pmSerial(2, 3);

// Setup AQI Sensor Object
Adafruit_PM25AQI aqi = Adafruit_PM25AQI();

// setup distance feed
AdafruitIO_Feed *aqi_feed = io.feed("air-quality-sensor.aqi");


void setup() {

  // -------- Adafruit PMSA003I Air Quality Sensor Setup ----------
  // Wait for serial monitor to open
  Serial.begin(115200);
  while (!Serial) delay(10);

  Serial.println("Adafruit PMSA003I Air Quality Sensor");

  // Wait one second for sensor to boot up!
  delay(1000);

  // baud rate of the PM2.5 sensor is set
  pmSerial.begin(9600);

  // There are 3 options for connectivity!
  // if (! aqi.begin_I2C()) {      // connect to the sensor over I2C
  //if (! aqi.begin_UART(&Serial1)) { // connect to the sensor over hardware serial
  if (! aqi.begin_UART(&pmSerial)) { // connect to the sensor over software serial
    Serial.println("Could not find PM 2.5 sensor!");
    while (1) delay(10);
  }

  Serial.println("PM25 found!");

  // --------- Adafruit IO Setup -------------
  io.connect();

  // wait for a connection
  while(io.status() < AIO_CONNECTED) {
    Serial.print(".");
    delay(500);
  }

  // we are connected
  Serial.println();
  Serial.println(io.statusText());

}

void loop() {
  // io.run(); is required for all sketches.
  // it should always be present at the top of your loop
  // function. it keeps the client connected to
  // io.adafruit.com, and processes any incoming data.
  io.run();


  PM25_AQI_Data data;

  if (! aqi.read(&data)) {
    Serial.println("Could not read from AQI");
    delay(500);  // try again in a bit!
    return;
  }

  // save pm reading to Adafruit IO
  aqi_feed->save(data.pm25_standard);


  // print out for debugging
  Serial.println("AQI reading success");
  Serial.println(F("Concentration Units (standard)"));
  Serial.print(F("\tPM 2.5: ")); Serial.print(data.pm25_standard);
  Serial.println();

  // delay for a certain number of seconds
  for (int i; i < 301; ++i){
    delay(1000);
  }

}
