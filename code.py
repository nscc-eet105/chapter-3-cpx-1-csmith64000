from adafruit_circuitplayground import cp
import time


while True:
    if cp.switch:
        cp.red_led = True
    else:
        cp.red_led = False

    if cp.button_a:
        cp.play_file("applause_y.wav")

    if cp.button_b:
        cp.play_file("blip.wav")

    if cp.touch_A1:
        cp.pixels[0]= (100, 0, 0)
    else:
        cp.pixels[0]= (0, 0, 0)








