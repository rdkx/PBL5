from playsound import playsound
from multiprocessing import Process
import datetime 
import time
import keyboard 
import serial
import sys
import threading

ser = serial.Serial('COM5', 9600, timeout=0)
time.sleep(3)

def main(): 
    elapsedTime = datetime.datetime.now() - datetime.datetime.now()
    record = open("Output.csv", "w")

    record.write("Elapsedtime," + "r," + "g," + "b," + "bpm\n")

    red = 0
    green = 0
    blue = 0
    bpm = ''

    for i in range(1, 1300):
        if (ser.inWaiting()>0):
            reading = ser.read(ser.inWaiting()).decode('ascii').strip()
 
            if(bpm != reading):
                bpm = reading
                
        start = datetime.datetime.now()
        time.sleep(0.01)
        end = datetime.datetime.now()
        elapsedTime = elapsedTime + (end - start)

        if keyboard.is_pressed('r'):
            red = 1

        if keyboard.is_pressed('g'):
            green = 1

        if keyboard.is_pressed('b'):
            blue = 1

        print(elapsedTime, red, green, blue, bpm)
        record.write("%s," % elapsedTime + "%s," %red + "%s," %green + "%s," %blue + "%s\n" %bpm)

        red = 0
        green = 0
        blue = 0

    ser.close()
    record.close()

def play():
    playsound('track1.wav')

thread = threading.Thread(target=play)

if __name__ == "__main__":
    thread.start()
    main()
