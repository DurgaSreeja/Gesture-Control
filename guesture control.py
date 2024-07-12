import serial
import time 
import pyautogui

ArduinoSerial = serial.Serial('com3',9600) 
time.sleep(2) 

while 1:
    incoming = str (ArduinoSerial.readline()) 
    print(incoming)    
    
    if 'Play/Pause' in incoming:
        pyautogui.typewrite(['space'], 0.2)

    if 'Rewind' in incoming:
        pyautogui.hotkey('alt', 'left')  

    if 'Forward' in incoming:
        pyautogui.hotkey('alt', 'right') 

    if 'Vup' in incoming:
        pyautogui.hotkey('ctrl', 'up')
        
    if 'Vdown' in incoming:
        pyautogui.hotkey('ctrl', 'down')

    if 'next' in incoming:
        pyautogui.hotkey('ctrl', 'x')

    incoming = "";
    
 
