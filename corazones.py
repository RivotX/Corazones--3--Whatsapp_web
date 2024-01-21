import pyautogui as pg
import pyperclip as pyc
import time

emojis='🌸💖🌺😻🌹😍🌻🥰🌷❤️'
emojis2='🖕😡🖕🤡🥵💩🖕🤬🤢🤡'

def dibujar_corazon(e):
    c = [
        [0,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,0],
        [0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0],
        [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0],
        [0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
        ]

    corazon = '‎'
    
    for i in range(len(c)):
        for j in range(len(c[i])):
            if c[i][j] == 1:
                corazon += e
            else:
                corazon += '   '
        corazon += '\n'

    pyc.copy(corazon)


mensajes = int(input('Número de mensajes: '))
time.sleep(4)

for i in range(mensajes):
    dibujar_corazon(emojis2[i%10])
    pg.hotkey('ctrl', 'v')
    pg.press('enter')