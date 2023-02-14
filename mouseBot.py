import pyautogui as pag
import random
import time

while True:
    x=random.randint(200,700)
    y = random.randint(100,700)
    pag.moveTo(x,y,0.5)
    time.sleep(0.5)

