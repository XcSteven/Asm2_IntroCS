input.onSound(DetectedSound.Loud, function () {
    led.plot(2, 2)
    basic.pause(500)
    led.unplot(2, 2)
    basic.showLeds(`
        . . . . .
        . # # # .
        . # . # .
        . # # # .
        . . . . .
        `)
})
