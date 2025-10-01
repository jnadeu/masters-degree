#include <Wire.h>
#include "FastIMU.h"

#include "model_5.h"

#include <tflm_esp32.h>       // TensorFlow Lite Micro support for ESP32
#include <eloquent_tinyml.h>  // EloquentTinyML helper/wrapper for TF Micro

// Configuration
#define SAMPLE_HZ 400000
#define WINDOW_SIZE 250      // number of consecutive samples passed to the model
#define N_FEATURES 7         // gyroX, gyroY, gyroZ, accelX, accelY, accelZ, temp
#define NUMBER_OF_OUTPUTS 3  // 3 gestures
#define ARENA_SIZE model_5_len 

#ifndef TF_NUM_OPS
#define TF_NUM_OPS 250  // limit for operations resolver
#endif

// Instantiate the model
Eloquent::TF::Sequential<TF_NUM_OPS, ARENA_SIZE> tf;

#define IMU_ADDRESS 0x6B     
#define PERFORM_CALIBRATION  //Comment to disable startup calibration

QMI8658 IMU;
calData calib = { 0 };

// Sensor data
GyroData gyroData;
AccelData accelData;    

static float input_buffer[WINDOW_SIZE * N_FEATURES];

// ---------------------------
// Setup: run once on boot
// ---------------------------
void setup() {
  Wire.begin(48, 47);
  Wire.setClock(400000);
  Serial.begin(115200);
  while (!Serial) delay(10);
  Serial.println("Gesture inference with 3 different gestures starting");

  int err = IMU.init(calib, IMU_ADDRESS);
  if (err != 0) {
    Serial.print("FastIMU init failed: ");
    Serial.println(err);
    while (1) delay(1000);
  }
  Serial.println("IMU initialized");

  // Set up the TF Micro model input/output sizes and the operator resolver
  tf.setNumInputs(WINDOW_SIZE * N_FEATURES);
  tf.setNumOutputs(NUMBER_OF_OUTPUTS);

  // Register the operators that the model uses.
  tf.resolver.AddFullyConnected();
  tf.resolver.AddSoftmax();
  tf.resolver.AddReshape();
  tf.resolver.AddLogistic();


  // Load the model binary
  auto status = tf.begin(model_5);
  while (!status.isOk()) {
    Serial.print("tf.begin failed: ");
    Serial.println(tf.exception.toString());
    delay(1000);
    status = tf.begin(model_5);
  }
  Serial.println("Model loaded");
}

// Simple countdown helper used between inferences
void wait_time(uint8_t s) {
  while (s > 0) {
    Serial.print(s);
    Serial.print(" ");
    delay(1000);
    s = s - 1;
  }
  Serial.println();
}

// ---------------------------
// Main loop: collect WINDOW_SIZE samples, run inference, print results
// ---------------------------
void loop() {
  uint16_t count = WINDOW_SIZE;
  uint16_t i = 0;

  // Fill the input buffer with sensor readings
  while (i < count) {
    delay(4);

    // Read IMU sensors
    IMU.update();

    IMU.getGyro(&gyroData);
    IMU.getAccel(&accelData);
    float temp = IMU.getTemp();  // if supported; else use 0

    int idx = i * N_FEATURES;
    input_buffer[idx + 0] = gyroData.gyroX;
    input_buffer[idx + 1] = gyroData.gyroY;
    input_buffer[idx + 2] = gyroData.gyroZ;
    input_buffer[idx + 3] = accelData.accelX;
    input_buffer[idx + 4] = accelData.accelY;
    input_buffer[idx + 5] = accelData.accelZ;
    input_buffer[idx + 6] = temp;

    ++i;
  }

  // Run inference on the filled window
  auto predStatus = tf.predict(input_buffer);
  if (!predStatus.isOk()) {
    Serial.print("tf.predict failed: ");
    Serial.println(tf.exception.toString());
    delay(1000);
    return;
  }

  int predicted = tf.classification;
  Serial.print("Predicted gesture: ");
  Serial.println(predicted);

  // Print the confidence scores for each class
  Serial.print("Scores: ");
  for (int c = 0; c < NUMBER_OF_OUTPUTS; c++) {
    Serial.print(tf.output(c), 6);
    if (c < NUMBER_OF_OUTPUTS - 1) Serial.print(", ");
  }
  Serial.println();

  wait_time(5);
}