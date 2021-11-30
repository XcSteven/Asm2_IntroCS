input.onButtonPressed(Button.A, function () {
    basket.change(LedSpriteProperty.X, -1)
})
input.onButtonPressed(Button.B, function () {
    basket.change(LedSpriteProperty.X, 1)
})
let fruit: game.LedSprite = null
let basket: game.LedSprite = null
basket = game.createSprite(2, 4)
game.setScore(0)
game.setLife(3)
music.playMelody("E B C5 A B G A F ", 275)
basic.forever(function () {
    if (game.isGameOver()) {
        music.playMelody("C5 B A G F E D C ", 350)
        basic.pause(1000000)
    }
})
basic.forever(function () {
    fruit = game.createSprite(randint(0, 4), -1)
    fruit.set(LedSpriteProperty.Brightness, 120)
    if (game.score() < 20) {
        for (let index = 0; index < 5; index++) {
            basic.pause(500)
            fruit.change(LedSpriteProperty.Y, 1)
            if (fruit.isTouching(basket)) {
                game.addScore(1)
                fruit.delete()
            }
        }
    } else if (game.score() < 50) {
        for (let index = 0; index < 5; index++) {
            basic.pause(400)
            fruit.change(LedSpriteProperty.Y, 1)
            if (fruit.isTouching(basket)) {
                game.addScore(1)
                fruit.delete()
            }
        }
    } else if (game.score() < 100) {
        for (let index = 0; index < 5; index++) {
            basic.pause(300)
            fruit.change(LedSpriteProperty.Y, 1)
            if (fruit.isTouching(basket)) {
                game.addScore(1)
                fruit.delete()
            }
        }
    } else {
        for (let index = 0; index < 5; index++) {
            basic.pause(200)
            fruit.change(LedSpriteProperty.Y, 1)
            if (fruit.isTouching(basket)) {
                game.addScore(1)
                fruit.delete()
            }
        }
    }
    if (fruit.isTouchingEdge()) {
        music.playMelody("D - - - - - - - ", 500)
        game.removeLife(1)
    }
    fruit.delete()
})
