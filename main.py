def on_sound_loud():
    led.plot(2, 2)
    basic.pause(100)
    led.unplot(2, 2)
    basic.show_leds("""
        . . . . .
                . # # # .
                . # . # .
                . # # # .
                . . . . .
    """)
    basic.pause(100)
    basic.clear_screen()
    basic.show_leds("""
        # # # # #
                # . . . #
                # . . . #
                # . . . #
                # # # # #
    """)
    basic.pause(100)
    basic.clear_screen()
input.on_sound(DetectedSound.LOUD, on_sound_loud)
