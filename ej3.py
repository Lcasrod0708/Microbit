# Imports go at the top
from microbit import *

while True:
    if button_a.was_pressed():
        display.show(Image.BUTTERFLY)
        sleep(1000)
    if button_b.was_pressed():
        display.show(Image.CHESSBOARD)
        sleep(1000)
    else:
        display.show(Image.HOUSE)
