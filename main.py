def on_pin_pressed_p2():
    global sound
    for index in range(4):
        music.play_tone(sound, music.beat(BeatFraction.QUARTER))
        sound += -25
    sound = 440
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_pin_pressed_p1():
    global sound
    for index2 in range(4):
        music.play_tone(sound, music.beat(BeatFraction.QUARTER))
        sound += 25
    sound = 440
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

sound = 0
sound = 440

def on_forever():
    pass
basic.forever(on_forever)
