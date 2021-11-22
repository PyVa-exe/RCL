
//arduino bullshit
//#include <MeMCore.h>
//#include <Arduino.h>
//#include <Wire.h>
//#include <SoftwareSerial.h>

#include <stdio.h>
#include <time.h>


long millis()
{
	clock_t timer;
	timer = clock();
	return (long)timer;
}


void delay(float seconds) {
	long endTime = millis() + seconds * 1000;
	while (millis() < endTime);
}



void loop() {};
void setup()
{
	float code[] = { 2.0, 229.5, 5.0, 1.0, 0.0, 25.5, 5.0, 1.0, 3.0, 229.5, 5.0, 1.0, 0.0, 25.5, 5.0, 1.0, 4.0, 6.0 };
	int codeSize = sizeof(code) / sizeof(float);
	float* execPtr = code;

	short isRunning = 1;

	while (isRunning)
	{

		int command = (int)*execPtr;


		switch (command)
		{
		case 0:
			printf("forward\n");
			execPtr += 2;
			break;

		case 1:
			printf("backward\n");
			execPtr += 2;
			break;

		case 2:
			printf("left\n");
			execPtr += 2;
			break;

		case 3:
			printf("right\n");
			execPtr += 2;
			break;

		case 4:
			printf("stop\n");
			execPtr += 1;
			break;

		case 5:
			delay(*(execPtr + 1));
			execPtr += 2;
			break;

		case 6:
			isRunning = 0;
			break;
		}

	}


	printf("exit");

}



int main()
{
	setup();
	for (;;) loop();

	return 0;
}