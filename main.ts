input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {
    
    for (let index = 0; index < 4; index++) {
        music.playTone(sound, music.beat(BeatFraction.Quarter))
        sound += -25
    }
    sound = 440
})
input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {
    
    for (let index2 = 0; index2 < 4; index2++) {
        music.playTone(sound, music.beat(BeatFraction.Quarter))
        sound += 25
    }
    sound = 440
})
let sound = 0
sound = 440
basic.forever(function on_forever() {
    
})
