void setup()
{
    // initialize the digital pin as an output.
    // Pin 13 has an LED connected on most Arduino boards:
    pinMode(4, OUTPUT);
    Serial.begin(115200);
    delay(1000);
    Serial.println("Starte...");
}

void loop()
{
    Serial.println("Hight");
    digitalWrite(4, HIGH); // set the LED on
    delay(1000);           // wait for a second
    Serial.println("LOW");
    digitalWrite(4, LOW); // set the LED off
    delay(1000);          // wait for a second
}