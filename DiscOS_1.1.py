#created by Felipe aka, pipe05
#FILE MAY NOT WORK IN TERMINAL
import RPi.GPIO as GPIO
import time
from colorama import Fore
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#GPIO PINS ARE FROM © 2018 RASPBERRY PI 4 MODEL B
GPIO.setup(26, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.output(27, GPIO.LOW)
GPIO.output(16, GPIO.LOW)
GPIO.output(26, GPIO.LOW)
GPIO.output(6, GPIO.LOW)
print(f"{Fore.BLUE}                     ______________________________________________")
print(f"{Fore.BLUE}                    |                                              |") 
print(f"{Fore.BLUE}                    |{Fore.RED} Hello. Welcome to DiscOS 1.0 Beta testing!{Fore.BLUE}   |")
print(f"{Fore.BLUE}                    |                                              |")
print(f"{Fore.BLUE}                    ------------------------------------------------")
time.sleep(1.5)
print(f"{Fore.BLUE}                    ____________________________________________________________________________________________")
print(f"{Fore.BLUE}                    |                                                                                          |") 
print(f"{Fore.BLUE}                    |{Fore.RED} Only one program may be run (DiscOS will automatically exit when done with its process){Fore.BLUE}  |")
print(f"{Fore.BLUE}                    |                                                                                          |")
print(f"{Fore.BLUE}                    --------------------------------------------------------------------------------------------")
time.sleep(1.5)
print(f"{Fore.BLUE}                     ______________________________________________")
print(f"{Fore.BLUE}                    |                                              |") 
print(f"{Fore.BLUE}                    |{Fore.RED} This is a copyright free,open source software{Fore.BLUE}|")
print(f"{Fore.BLUE}                    |                                              |")
print(f"{Fore.BLUE}                    ------------------------------------------------")
time.sleep(1.5)
print(f"{Fore.BLUE}                     _________________________________________________________________________")
print(f"{Fore.BLUE}                    |                                                                        |") 
print(f"{Fore.BLUE}                    |{Fore.RED} Although this is more like just a program the name DiscOS sounds better{Fore.BLUE}|")
print(f"{Fore.BLUE}                    |                                                                        |")
print(f"{Fore.BLUE}                    --------------------------------------------------------------------------")
time.sleep(2.5)
print(f"{Fore.BLUE}                     ______________________________________________")
print(f"{Fore.BLUE}                    |                                              |") 
print(f"{Fore.BLUE}                    |{Fore.RED} Created by 'pipe05'. {Fore.BLUE}                        |")
print(f"{Fore.BLUE}                    |                                              |")
print(f"{Fore.BLUE}                    ------------------------------------------------")
time.sleep(2.5)
print(f"{Fore.BLUE}                     ______________________________________________")
print(f"{Fore.BLUE}                    |                                              |") 
print(f"{Fore.BLUE}                    |{Fore.RED} What would you like to do?{Fore.BLUE}                   |")
print(f"{Fore.BLUE}                    |                                              |")
print(f"{Fore.BLUE}                    ------------------------------------------------")
time.sleep(2.5)
print(f"{Fore.BLUE}                    __________________________________________________________________")
print(f"{Fore.BLUE}                    |                                                                |") 
print(f"{Fore.BLUE}                    |{Fore.RED} Turn on a light?{Fore.GREEN}(Type 'light' without the quotes){Fore.BLUE}              |")
print(f"{Fore.BLUE}                    |{Fore.RED} Flash a light?{Fore.GREEN}(Type 'flight' without the quotes){Fore.BLUE}               |")
print(f"{Fore.BLUE}                    |{Fore.RED} Say some words with color?{Fore.GREEN}(Type 'color' without the quotes){Fore.BLUE}    |")
print(f"{Fore.BLUE}                    |{Fore.RED} Want to know more about me?{Fore.GREEN}(Type 'about' without the quotes){Fore.BLUE}   |")
print(f"{Fore.BLUE}                    |{Fore.RED} Check out my youtube channel{Fore.GREEN}(Type 'youtube' without the quotes){Fore.BLUE}|")
print(f"{Fore.BLUE}                    |                                                                |")
print(f"{Fore.BLUE}                    -----------------------------------------------------------------")
screen_1 = input(">>>")
if screen_1 == "light":
    GPIO.output(27, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(26, GPIO.LOW)
    GPIO.output(6, GPIO.LOW)
    print(f"{Fore.RED}                    -----------------------------")
    print(f"{Fore.BLACK}                    |1.Turn on the {Fore.RED}red {Fore.BLACK}light?   |")
    print(f"{Fore.BLACK}                    |2.Turn on the {Fore.GREEN}green {Fore.BLACK}light? |")
    print(f"{Fore.BLACK}                    |3 Turn on the {Fore.YELLOW}yellow {Fore.BLACK}light?|")
    print(f"{Fore.BLACK}                    |4.Turn on the {Fore.BLUE}blue {Fore.BLACK}light?  |")
    print(f"{Fore.RED}                    -----------------------------")
    time.sleep(2.5)
    print(f"{Fore.BLUE}                     ______________________________________________")
    print(f"{Fore.BLUE}                    |                                              |") 
    print(f"{Fore.BLUE}                    |{Fore.RED} Answer with the color would like to turn on.{Fore.BLUE} |")
    print(f"{Fore.BLUE}                    |                                              |")
    print(f"{Fore.BLUE}                    ------------------------------------------------")
    color = input("                    >>>")
    print(f"{Fore.RED}LOADING...")
    print(".")
    time.sleep(.2)
    print("..")
    time.sleep(.2)
    print("...")
    time.sleep(.2)
    print("..")
    time.sleep(.2)
    print(".")
    time.sleep(.2)
    print(".")
    time.sleep(.2)
    print("..")
    time.sleep(.2)
    print("...")
    time.sleep(.2)
    print("..")
    time.sleep(.2)
    print(".")
    time.sleep(.2)
    print(".")
    time.sleep(.2)
    print("..")
    time.sleep(.2)
    print("...")
    time.sleep(.2)
    print("..")
    time.sleep(.2)
    print(".")
    time.sleep(.2)
    print(f"{Fore.RED}DONE!")

#print(f"{Fore.BLACK} ______________________________________________")
#print(f"{Fore.BLACK}|                                              |") 
#print(f"{Fore.BLACK}|{Fore.BLUE} How long would you like it to be on for?{Fore.BLACK}     |")
#print(f"{Fore.BLACK}|                                              |")
#print(f"{Fore.BLACK}------------------------------------------------")
#f = input(">>>")

    if color == "red":
        GPIO.output(27, GPIO.HIGH)
    if color == "blue":
       GPIO.output(6, GPIO.HIGH)
    if color == "yellow":
        GPIO.output(16, GPIO.HIGH)
    if color == "green":
        GPIO.output(26, GPIO.HIGH)
    exit()
if screen_1 == "about":
    print(f"{Fore.RED} Hello.")
    time.sleep(1)
    print(f"{Fore.RED} You may be wondering who I am.")
    time.sleep(1.5)
    print(f"{Fore.RED} My name is pipe05, or so to say.")
    time.sleep(1.5)
    print(f"{Fore.RED} I have always wanted to code, and now here I am, coding my own 'OS'")
    time.sleep(2)
    print(f"{Fore.RED} Anyways it was nice meeting you")
    time.sleep(1)
    exit()            
if screen_1 == "color":
    lol = input(f"{Fore.BLUE}What color would you like?:")
    uwu = input(f"{Fore.BLUE}What would you like to say:")
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
        exit()
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
        exit()
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
        exit()
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
        exit()
    
if screen_1 == "flight":
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
        exit()
    elif f == ("green"):
        joe(l)
        exit()
    elif f == ("combo"):
        yeet(l)
        bob(l)
        exit()
    elif f == ("yellow"):
        matt(l)
        exit()
    elif f == ("blue"):
        lol(l)
        exit()
    elif f == ("felipe"):
        bob(l)
        exit()
    elif f == ("reset"):
        GPIO.output(27, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(26, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)
        exit()
if screen_1 == "youtube":
    print(f"{Fore.BLUE}                     __________________________________________________________")
    print(f"{Fore.BLUE}                    |                                                         |") 
    print(f"{Fore.BLUE}                    |{Fore.RED} My youtube channel!   {Fore.BLUE}                                 |")
    print(f"{Fore.BLUE}                    |{Fore.RED}https://www.youtube.com/channel/UCMaIHy41sTwhst4pWbQMBxw{Fore.BLUE}|")
    print(f"{Fore.BLUE}                    |                                                         |")
    print(f"{Fore.BLUE}                    -----------------------------------------------------------")
else:
    print(f"{Fore.RED}ERROR:INVALID SYNTAX")