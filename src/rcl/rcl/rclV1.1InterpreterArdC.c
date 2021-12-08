
//arduino bullshit
#include <MeMCore.h>
#include <Arduino.h>
#include <Wire.h>
#include <SoftwareSerial.h>

MeDCMotor motor0(9);
MeDCMotor motor1(10);
MeBuzzer buzzer;
MeRGBLed rgbled(7, 2);
MeLineFollower linefollower(3);
MeUltrasonicSensor ultrasonic(3);


void delayMs(float seconds) {
	long endTime = millis() + seconds * 1000;
	while (millis() < endTime);
}



//takes 2 values from 0 to 100, setting the speed of the 2 motor on the robot
void setRobotMoveDir(float m0, float m1)
{
    int mMapped0 = (int)(m0 / 100.0 * 255);
    int mMapped1 = (int)(m1 / 100.0 * 255);

    motor0.run(mMapped0);
    motor1.run(-mMapped1);


}




void loop() {};
void setup()
{
	float code[] = { 0.0, 255.0, 5.0, 2.0, 2.0, 255.0, 5.0, 0.5, 7.0, 0.0 };
	int codeSize = sizeof(code) / sizeof(float);
    int execPtr = 0;

	short isRunning = 1;

    setRobotMoveDir(0, 0);

    pinMode(A7, INPUT);
  while(!(((analogRead(A7) > 10 ? 0 : 1))));

    rgbled.fillPixelsBak(0, 2, 1);
    rgbled.setColor(0, 0, 255, 0);
    rgbled.show();



	while (isRunning)
	{



		int command = (int)code[execPtr];
        float attr  = (float)code[execPtr + 1];

		switch (command)
		{
		case 0:
            setRobotMoveDir(attr, attr);
			execPtr += 2;
			break;

		case 1:
            setRobotMoveDir(-attr, -attr);
			execPtr += 2;
			break;

		case 2:
            setRobotMoveDir(attr, -attr);
			execPtr += 2;
			break;

		case 3:
            setRobotMoveDir(-attr, attr);
			execPtr += 2;
			break;

		case 4:
            setRobotMoveDir(0, 0);
			execPtr += 1;
			break;

		case 5:
			delayMs(attr);
			execPtr += 2;
			break;

		case 6:
			isRunning = 0;
			break;

        case 7:
            execPtr = (int)attr;
            break;

        case 8:
            int sensorCode = (int)code[execPtr + 2];
            int compType   = (int)code[execPtr + 3];
            int constValue = (int)code[execPtr + 4];

            int sensorValue = NULL;

            //get the sensor values
            switch(sensorCode)
            {
                case 0:
                    sensorValue = (int)linefollower.readSensors();
                    break;

                case 1:
                    sensorValue = (int)ultrasonic.distanceCm();
                    break;

            }

            int hasSet = 0;

            //do comp and override execPtr based on result
            switch(compType)
            {
                //==
                case 0:
                    if(sensorValue == constValue) hasSet = 1;
                    break;

                //sensor > const
                case 1:
                    if(sensorValue > constValue) hasSet = 1;
                    break;

                //sensor < const
                case 2:
                    if(sensorValue < constValue) hasSet = 1;
                    break;



            }


            if(hasSet) execPtr = (int)attr;
            else execPtr += 4;

		}

	}

    rgbled.fillPixelsBak(0, 2, 1);
    rgbled.setColor(0, 255, 0, 0);
    rgbled.show();


}

