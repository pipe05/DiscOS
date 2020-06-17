#created by Felipe aka, pipe05
#FILE MAY NOT WORK IN TERMINAL
#all libraries are needed as this uses GPIO 
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
import time
from colorama import Fore
GPIO.output(27, GPIO.LOW)
GPIO.output(16, GPIO.LOW)
GPIO.output(26, GPIO.LOW)
GPIO.output(6, GPIO.LOW)
print(f"{Fore.RED}PROGRAM DOES NOT FUNCTION WELL IN TERMINAL")
x = input("Enter your password:")
if x == ("coolkid"):
    print(f"{Fore.BLUE}Correct password!")
if x != ("coolkid"):
    print (f"{Fore.RED}INCORRECT PASSWORD: " + "'" + x + "'")
    exit()
def lol(z):
 print(f"{Fore.BLUE}Turning on the blue light "+l+" times")
 time.sleep(2)
 for q in range(1, int(z)):
    GPIO.output(6, GPIO.HIGH)
    time.sleep(.2)
    GPIO.output(6, GPIO.LOW)
    time.sleep(.2)        
def joe(o):
    print(f"{Fore.GREEN}Turning on the green light "+l+" times")
    time.sleep(2)
    for i in range(1, int(o)):
        GPIO.output(26, GPIO.HIGH)            
        time.sleep(.2)
        GPIO.output(26, GPIO.LOW)
        time.sleep(.2)
def felipe(c):
    print(f"{Fore.RED}Turning on the red light "+l+" times")
    time.sleep(2)
    for g in range(1, int(c)):
         GPIO.output(27, GPIO.HIGH)
         time.sleep(.2)
         GPIO.output(27, GPIO.LOW)
         time.sleep(.2)
def matt(m):
    print(f"{Fore.YELLOW}Turning on the yellow light "+l+" times")
    time.sleep(2)
    for t in range(1, int(m)):
         GPIO.output(16, GPIO.HIGH)
         time.sleep(.2)
         GPIO.output(16, GPIO.LOW)
         time.sleep(.2)
def yeet(k):
    print(f"{Fore.RED}Turning on all the lights "+l+" times")
    print(f"{Fore.RED}lol")
    time.sleep(2)
    for z in range(1, int(k)):
        GPIO.output(16, GPIO.LOW)            
        time.sleep(.1)            
        GPIO.output(27, GPIO.HIGH)
        time.sleep(.1)
        GPIO.output(26, GPIO.LOW)
        time.sleep(.1)
        GPIO.output(6, GPIO.HIGH)            
        time.sleep(.1)            
        GPIO.output(6, GPIO.LOW)
        time.sleep(.1)
        GPIO.output(27, GPIO.LOW)            
        time.sleep(.1)            
        GPIO.output(26, GPIO.HIGH)
        time.sleep(.1)
        GPIO.output(16, GPIO.HIGH)
        time.sleep(.1)
def bob(h):
    print(f"{Fore.RED}Turning on all the lights "+l+" times")
    print(f"{Fore.RED}lol")
    time.sleep(2)
    for g in range(1, int(h)):
        GPIO.output(2, GPIO.HIGH)            
        time.sleep(1)            
        GPIO.output(2, GPIO.LOW)
        time.sleep(1)
        GPIO.output(2, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(2, GPIO.LOW)            
        time.sleep(1)            
        #GPIO.output(4, GPIO.HIGH)
        #time.sleep(1)
        #GPIO.output(4, GPIO.LOW)            
        #time.sleep(1)            
        #GPIO.output(4, GPIO.HIGH)
        #time.sleep(1)
        #GPIO.output(4, GPIO.LOW)
        #time.sleep(1)
        GPIO.output(3, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(3, GPIO.LOW)            
        time.sleep(1)            
        GPIO.output(3, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(3, GPIO.LOW)
        time.sleep(1)
        
ex_it = input(f"{Fore.RED}If you would like to exit type 1, if not type 0:")
if ex_it == ("1"):
    print(f"{Fore.GREEN} Exiting...")
    time.sleep(.5)
    print(f"{Fore.RED}.")
    time.sleep(.5)
    print(f"{Fore.RED}..")
    time.sleep(.5)
    print(f"{Fore.RED}...")
    time.sleep(.5)
    print(f"{Fore.RED}..")
    time.sleep(.5)
    print(f"{Fore.RED}.")
    time.sleep(.5)
    print(f"{Fore.RED}..")
    time.sleep(.5)
    print(f"{Fore.RED}...")
    time.sleep(.5)
    print(f"{Fore.RED}..")
    time.sleep(.5)
    print(f"{Fore.RED}.")
    time.sleep(.5)
    print(f"{Fore.RED}..")
    time.sleep(.5)
    print(f"{Fore.RED}...")
    time.sleep(.5)
    print(f"{Fore.RED}..")
    time.sleep(.5)
    print(f"{Fore.RED}.")
    time.sleep(.5)
    print(f"{Fore.RED}..")
    time.sleep(1.5)
    print(f"{Fore.GREEN} STOPPED!")
    
    exit()
elif ex_it == ("0"):
    pass
    
f = input(f"{Fore.RED}Would you like to flash {Fore.GREEN}green, {Fore.BLUE}blue, {Fore.YELLOW}yellow, {Fore.RED}red or {Fore.GREEN}c{Fore.BLUE}o{Fore.YELLOW}m{Fore.RED}b{Fore.BLACK}o{Fore.RED}.Or would you like to {Fore.BLUE}reset?:")
l = input(f"{Fore.BLACK}How many times would you like it to flash?{Fore.RED}(Type '0' if doing a reset):")   
    #if (l < 25):
        #print("Your number is too big!")
if f == ("red"):
    felipe(l)
elif f == ("green"):
    joe(l)
elif f == ("combo"):
    yeet(l)
    bob(l)
elif f == ("yellow"):
    matt(l)
elif f == ("blue"):
    lol(l)
elif f == ("felipe"):
    bob(l)
elif f == ("reset"):
    GPIO.output(27, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(26, GPIO.LOW)
    GPIO.output(6, GPIO.LOW)