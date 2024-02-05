import pyautogui
import time
import os


def message_sender(message):
   
    for i in range(1,3):
        print(i)
        time.sleep(1)
    pyautogui.typewrite(message ,interval=0.1)
    pyautogui.press("enter")

    print("tera kaam ho gaya")


message= "happy birthday bro radha rani tereko humesha khush rakhe❤️ "


message_sender(message)

time.sleep(2)
os.system("shutdown /s /t 2")

happy birthday bro radha rani tereko humesha khush rakhe 







