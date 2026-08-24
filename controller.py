import serial
import pydirectinput
import time

# Apna COM port check karein
arduino_port = 'COM7' 

try:
    # Timeout ko kam rakha hai taake response fast ho
    arduino = serial.Serial(arduino_port, 9600, timeout=0.01)
    print("Controller Active: Arrows for Movement, Mouse Left Click for Action!")
except:
    print("Error: Port nahi mila. VS Code ko Admin mode mein chalayein.")
    exit()

# Mapping: Arduino signals ko PC keys/mouse mein badalna
while True:
    if arduino.in_waiting > 0:
        raw_data = arduino.readline().decode('utf-8').strip()
        
        if "_" in raw_data:
            key_name, action = raw_data.split("_")
            
            # Movement (Arrow Keys)
            if key_name == "W":
                pydirectinput.keyDown('up') if action == "DOWN" else pydirectinput.keyUp('up')
            elif key_name == "S":
                pydirectinput.keyDown('down') if action == "DOWN" else pydirectinput.keyUp('down')
            elif key_name == "A":
                pydirectinput.keyDown('left') if action == "DOWN" else pydirectinput.keyUp('left')
            elif key_name == "D":
                pydirectinput.keyDown('right') if action == "DOWN" else pydirectinput.keyUp('right')
            
            # Fire/Jump (Space Bar)
            elif key_name == "SPACE":
                pydirectinput.keyDown('space') if action == "DOWN" else pydirectinput.keyUp('space')
            
            # Sprint ki jagah Mouse Left Click
            elif key_name == "SHIFT":
                if action == "DOWN":
                    pydirectinput.mouseDown(button='left')
                    print("Mouse Left Click: DOWN")
                else:
                    pydirectinput.mouseUp(button='left')
                    print("Mouse Left Click: UP")

    time.sleep(0.001)