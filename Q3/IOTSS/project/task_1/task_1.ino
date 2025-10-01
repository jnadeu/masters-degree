#include "FastIMU.h"
#include <Wire.h>

#define IMU_ADDRESS 0x6B    //Change to the address of the IMU
#define PERFORM_CALIBRATION //Comment to disable startup calibration
QMI8658 IMU;               //Change to the name of any supported IMU! 

// Currently supported IMUS: MPU9255 MPU9250 MPU6886 MPU6500 MPU6050 ICM20689 ICM20690 BMI055 BMX055 BMI160 LSM6DS3 LSM6DSL QMI8658

calData calib = { 0 };  //Calibration data
AccelData accelData;    //Sensor data
GyroData gyroData;
MagData magData;

void get_giro_data_time_interval(uint8_t seconds) { //insert time in seconds
  uint16_t count = seconds * 250;
  uint16_t x = 0;

  while (x < count) {
    delay(4);

    //Read giroscope data
    Serial.print("giro:");
    IMU.update();
    IMU.getAccel(&accelData);
    Serial.print(accelData.accelX);
    Serial.print(",");
    Serial.print(accelData.accelY);
    Serial.print(",");
    Serial.print(accelData.accelZ);
    Serial.print(",");
    IMU.getGyro(&gyroData);
    Serial.print(gyroData.gyroX);
    Serial.print(",");
    Serial.print(gyroData.gyroY);
    Serial.print(",");
    Serial.print(gyroData.gyroZ);
    if (IMU.hasMagnetometer()) {
      IMU.getMag(&magData);
      Serial.print(",");
      Serial.print(magData.magX);
      Serial.print(",");
      Serial.print(magData.magY);
      Serial.print(",");
      Serial.print(magData.magZ);
    }
    if (IMU.hasTemperature()) {
      Serial.print(",");
      Serial.println(IMU.getTemp());
    }
    else {
      Serial.println();
    }
    x = x + 1;
  }
}

void wait_time(uint8_t s) {
  while (s > 0) {
    Serial.print(s);
    Serial.print(" ");
    delay(1000);
    s = s - 1;
  }
  Serial.println();
}

void setup() {
  Wire.begin(48, 47);
  Wire.setClock(400000); //400khz clock
  Serial.begin(115200);
  while (!Serial) {
    ;
  }

  int err = IMU.init(calib, IMU_ADDRESS);
  if (err != 0) {
    Serial.print("Error initializing IMU: ");
    Serial.println(err);
    while (true) {
      ;
    }
  }
  
#ifdef PERFORM_CALIBRATION
  Serial.println("FastIMU calibration & data example");
  if (IMU.hasMagnetometer()) {
    delay(1000);
    Serial.println("Move IMU in figure 8 pattern until done.");
    delay(3000);
    IMU.calibrateMag(&calib);
    Serial.println("Magnetic calibration done!");
  }
  else {
    delay(5000);
  }

  delay(5000);
  Serial.println("Keep IMU level.");
  delay(5000);
  IMU.calibrateAccelGyro(&calib);
  Serial.println("Calibration done!");
  Serial.println("Accel biases X/Y/Z: ");
  Serial.print(calib.accelBias[0]);
  Serial.print(", ");
  Serial.print(calib.accelBias[1]);
  Serial.print(", ");
  Serial.println(calib.accelBias[2]);
  Serial.println("Gyro biases X/Y/Z: ");
  Serial.print(calib.gyroBias[0]);
  Serial.print(", ");
  Serial.print(calib.gyroBias[1]);
  Serial.print(", ");
  Serial.println(calib.gyroBias[2]);
  if (IMU.hasMagnetometer()) {
    Serial.println("Mag biases X/Y/Z: ");
    Serial.print(calib.magBias[0]);
    Serial.print(", ");
    Serial.print(calib.magBias[1]);
    Serial.print(", ");
    Serial.println(calib.magBias[2]);
    Serial.println("Mag Scale X/Y/Z: ");
    Serial.print(calib.magScale[0]);
    Serial.print(", ");
    Serial.print(calib.magScale[1]);
    Serial.print(", ");
    Serial.println(calib.magScale[2]);
  }
  delay(5000);
  IMU.init(calib, IMU_ADDRESS);
#endif

  //err = IMU.setGyroRange(500);      //USE THESE TO SET THE RANGE, IF AN INVALID RANGE IS SET IT WILL RETURN -1
  //err = IMU.setAccelRange(2);       //THESE TWO SET THE GYRO RANGE TO ±500 DPS AND THE ACCELEROMETER RANGE TO ±2g
  
  if (err != 0) {
    Serial.print("Error Setting range: ");
    Serial.println(err);
    while (true) {
      ;
    }
  }
}

void loop() {
  get_giro_data_time_interval(1);
  
  wait_time(5);
}
