import serial
import time
arduino = serial.Serial(port ='COM16', baudrate = 9600, timeout = 0.1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
value = write_read(0)
while True:
    num = input ("Enter a number : ")
    value = write_read(num)
    print(value)