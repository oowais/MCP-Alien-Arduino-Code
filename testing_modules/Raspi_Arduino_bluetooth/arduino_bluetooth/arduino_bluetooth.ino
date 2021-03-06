void setup() {
  Serial.begin( 9600 );    // 9600 is the default baud rate for the serial Bluetooth module
}

void loop() {
  // listen for the data
  if ( Serial.available() > 0 ) {
    // read a numbers from serial port
    int count = Serial.parseInt();
    
     // print out the received number
    if (count > 0) {
        Serial.print("You have input: ");
        Serial.println(String(count));
        // blink the LED
        blinkLED(count);
    }
  }
}

void blinkLED(int count) {
  for (int i=0; i< count; i++) {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(500);
    digitalWrite(LED_BUILTIN, LOW);
    delay(500);
  } 
}
