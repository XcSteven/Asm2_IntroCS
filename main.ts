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
basic.forever(function () {
    fruit = game.createSprite(randint(0, 4), -1)
    fruit.change(LedSpriteProperty.Brightness, 200)
    for (let index = 0; index < 5; index++) {
        basic.pause(500)
        fruit.change(LedSpriteProperty.Y, 1)
        if (fruit.isTouching(basket)) {
            game.addScore(1)
            fruit.delete()
        }
    }
    if (fruit.isTouchingEdge()) {
        game.removeLife(1)
    }
    fruit.delete()
})
