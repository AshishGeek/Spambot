import pyautogui
import webbrowser
import time
time.sleep(10)

for i in range(1):


    f = open("spam.txt", 'r')
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
       
      

    
 