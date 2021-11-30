def on_button_pressed_a():
    basket.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basket.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

fruit: game.LedSprite = None
basket: game.LedSprite = None
basket = game.create_sprite(2, 4)
game.set_score(0)
game.set_life(3)

def on_forever():
    global fruit
    fruit = game.create_sprite(randint(0, 4), -1)
    fruit.change(LedSpriteProperty.BRIGHTNESS, 200)
    for index in range(5):
        basic.pause(500)
        fruit.change(LedSpriteProperty.Y, 1)
        if fruit.is_touching(basket):
            game.add_score(1)
            fruit.delete()
    if fruit.is_touching_edge():
        game.remove_life(1)
    fruit.delete()
basic.forever(on_forever)
