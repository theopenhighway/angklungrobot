#include <SPI.h>
#include <RF24.h>
#include <SoftwareSerial.h>

// Define the radio pinout
#define CE_PIN 9
#define CSN_PIN 10

// Define the available radio channels and payloads
const uint8_t num_channels = 2;
const uint8_t num_payloads = 1;
const uint64_t addresses[num_channels] = {0xF0F0F0F0E1LL, 0xF0F0F0F0E2LL};
const uint8_t payload_sizes[num_payloads] = {32};

// Define the RF24 radio object
RF24 radio(CE_PIN, CSN_PIN);

// Define the available serial connections
SoftwareSerial rfSerial(2, 3); // RX, TX
Serial USBSerial(9600);

void setup() {
  // Initialize the radio
  radio.begin();
  radio.setPALevel(RF24_PA_MIN);
  radio.setChannel(0);
  radio.setDataRate(RF24_250KBPS);
  radio.setRetries(15, 15);
  radio.setAutoAck(1);
  radio.enableDynamicPayloads();
  radio.openReadingPipe(1, addresses[0]);
  radio.startListening();

  // Initialize the USB serial connection
  USBSerial.begin(9600);

  // Initialize the RF serial connection
  rfSerial.begin(9600);
}

void loop() {
  // Read data from USB serial
  if (USBSerial.available() > 0) {
    String data = USBSerial.readString();

    // Print the received data to the serial monitor
    Serial.print("Received data over USB: ");
    Serial.println(data);
  }

  // Wait for incoming data on the radio
  if (radio.available()) {
    // Read the incoming data
    uint8_t channel = 0;
    uint8_t payload_size = radio.getDynamicPayloadSize();
    char payload[payload_size + 1];
    radio.read(payload, payload_size);
    payload[payload_size] = '\0';

    // Print the received data to the serial monitor
    Serial.print("Received data over RF: ");
    Serial.println(payload);
  }

  // Read data from RF serial
  if (rfSerial.available() > 0) {
    String data = rfSerial.readString();

    // Print the received data to the serial monitor
    Serial.print("Received data over RF: ");
    Serial.println(data);
  }
}
