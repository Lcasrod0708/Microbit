# Imports go at the top
from microbit import *
import music

i=0
musica=['a:4', 'b:6','c:8', 'd7', music.BA_DING,'a:4', 'b:6','c:8', 'd7', music.BA_DING]

while True:
    if button_a.was_pressed():
        i=i+1
    elif button_b.was_pressed():
        i=i-1
    else:
        music.play(musica[i])
