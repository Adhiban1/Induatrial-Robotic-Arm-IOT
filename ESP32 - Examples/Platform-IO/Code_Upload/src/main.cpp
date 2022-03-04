#include <Arduino.h>
#include <ESP32Servo.h>
#include <math.h>

// Servos.
Servo myservo1;
#define PIN_SERVO1 13

// Setup function.
void setup()
{ // Servos.
	myservo1.attach(PIN_SERVO1);

	// Serial Moniter.
	Serial.begin(9600);
}

int delay1 = 1000; // it is used to set the delay time between each moves.

// this the main loop function. Program inside it continuesly looping.
void loop()
{
	myservo1.write(0);
	delay(delay1);
	myservo1.write(180);
	delay(delay1);
	if (delay1 > 400)
	{
		delay1 -= 100;
	}
}