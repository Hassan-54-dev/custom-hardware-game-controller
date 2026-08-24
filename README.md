# custom-hardware-game-controller
Designed a custom physical gamepad using Arduino Nano and a Python serial-to-keyboard mapping script to bridge hardware with PC gaming.
# Custom Hardware Game Controller & USB HID Interface

Designed a custom physical game controller/gamepad interface using an Arduino Nano and a custom Python serial-to-keyboard mapping script to bridge physical hardware controls with PC gaming environments.

## 🚀 Project Overview
This project reads digital input signals from physical pushbuttons and joysticks via an Arduino Nano, transmits binary/string data over USB Serial (UART), and uses a multi-threaded Python middleware script to emulate virtual keyboard inputs in real-time.

## 🛠️ Key Features
- **Hardware Layer:** Interfaced digital pushbuttons and directional switches using internal pull-up resistor configurations for stable digital input reading.
- **Serial Data Transmission:** Programmed the Arduino to poll pin states and transmit fast, low-latency data tokens over UART.
- **Python Middleware:** Wrote a multi-threaded Python script using `PySerial` and OS automation libraries to actively listen to the COM port and map hardware events to keystrokes.

## 📂 Repository Contents
- Arduino firmware code (`.ino`)
- Python automation/mapping script (`.py`)
- Project cover preview (`p3.png`)

## 💻 Tools Used
- Arduino Nano
- Python (PySerial)
- USB Serial (UART)
