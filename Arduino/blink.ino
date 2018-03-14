#include <WiFi.h>
WiFiServer server(80);

void setup()
{
    // initialize the digital pin as an output.
    // Pin 13 has an LED connected on most Arduino boards:
    pinMode(4, OUTPUT);
    Serial.begin(115200);
    delay(1000);
    Serial.println("Starte...");
    
    String t = "test";
    t.substring(3);
}

void loop()
{
     WiFiClient clientS = server.available();
    Serial.println("Hight");
    digitalWrite(4, HIGH); // set the LED on
    delay(200);           // wait for a second
    Serial.println("LOW");
    digitalWrite(4, LOW); // set the LED off
    delay(200);          // wait for a second
}