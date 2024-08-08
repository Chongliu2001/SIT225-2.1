#include "DHT.h"

// Define the pin where DHT22 data pin is connected
#define DHTPIN 2

// Define the type of DHT sensor
#define DHTTYPE DHT22

// Initialize DHT sensor
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  // Initialize serial communication at 9600 baud rate
  Serial.begin(9600);

  // Begin DHT sensor
  dht.begin();

  // Print a message to indicate that setup is complete
  Serial.println("DHT22 sensor is ready.");
}

void loop() {
  // Wait for 30 seconds between measurements
  delay(30000);

  // Read humidity from DHT sensor
  float humidity = dht.readHumidity();

  // Read temperature from DHT sensor
  float temperature = dht.readTemperature();

  // Check if any reads failed and exit early (to try again)
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // Print temperature and humidity values to the serial monitor in CSV format
  Serial.print(temperature);
  Serial.print(",");
  Serial.println(humidity);
}
