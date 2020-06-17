#uwu
#Created by pipe05
import RPi.GPIO as GPIO
import time
from colorama import Fore
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.output(27, GPIO.LOW)
GPIO.output(16, GPIO.LOW)
GPIO.output(26, GPIO.LOW)
GPIO.output(6, GPIO.LOW)
lol = input("wat color would u like:")
uwu = input("wat u want to say:")
if lol == "red":
    print(f"{Fore.RED} "+uwu)
    #27
    GPIO.output(27, GPIO.HIGH)
    time.sleep(.2)
    GPIO.output(27, GPIO.LOW)
    time.sleep(.2)
    GPIO.output(27, GPIO.HIGH)
    time.sleep(.2)
    GPIO.output(27, GPIO.LOW)
    time.sleep(.2)
if lol == "blue":
    print(f"{Fore.BLUE} "+uwu)
    #6
    GPIO.output(6, GPIO.HIGH)
    time.sleep(.2)
    GPIO.output(6, GPIO.LOW)
    time.sleep(.2)
    GPIO.output(6, GPIO.HIGH)
    time.sleep(.2)
    GPIO.output(6, GPIO.LOW)
    time.sleep(.2)
if lol =="yellow":
    print(f"{Fore.YELLOW} "+uwu)
    #16
    GPIO.output(16, GPIO.HIGH)
    time.sleep(.2)
    GPIO.output(16, GPIO.LOW)
    time.sleep(.2)
    GPIO.output(16, GPIO.HIGH)
    time.sleep(.2)
    GPIO.output(16, GPIO.LOW)
    time.sleep(.2)
if lol == "green":
    print(f"{Fore.GREEN} "+uwu)
    #26
    GPIO.output(26, GPIO.HIGH)
    time.sleep(.2)
    GPIO.output(26, GPIO.LOW)
    time.sleep(.2)
    GPIO.output(26, GPIO.HIGH)
    time.sleep(.2)
    GPIO.output(26, GPIO.LOW)
    time.sleep(.2)
    
        
