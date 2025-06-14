import serial
import time
from pynput.keyboard import Controller, Key

# Initialize serial connection (adjust COM port for your setup)
ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your actual port
keyboard = Controller()

time.sleep(2)  # Give the connection some time to establish

while True:
    if ser.in_waiting > 0:
        data = ser.readline().decode().strip()
        print(f"Received: {data}")  # Debugging output
        keyboard.type(data)  # Simulate typing the received text
        keyboard.press(Key.enter)  # Press Enter after typing
        keyboard.release(Key.enter)  # Release the Enter key
