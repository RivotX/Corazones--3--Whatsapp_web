import pyautogui as pg
import pyperclip as pyc
import time

mensajes = int(input('Número de mensajes: '))
time.sleep(4)

for i in range(mensajes):
    pyc.copy("Geyson Mamahuevo")

    pg.hotkey('ctrl', 'v')
    pg.press('enter')