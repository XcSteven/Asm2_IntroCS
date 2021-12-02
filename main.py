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
music.play_melody("E B C5 A B G A F ", 275)

def on_forever():
    if game.is_game_over():
        music.play_melody("C5 B A G F E D C ", 350)
        basic.pause(1000000)
basic.forever(on_forever)

def on_forever2():
    global fruit
    fruit = game.create_sprite(randint(0, 4), -1)
    fruit.set(LedSpriteProperty.BRIGHTNESS, 120)
    if game.score() < 20:
        for index in range(5):
            basic.pause(500)
            fruit.change(LedSpriteProperty.Y, 1)
            if fruit.is_touching(basket):
                game.add_score(1)
                fruit.delete()
    elif game.score() < 50:
        for index2 in range(5):
            basic.pause(400)
            fruit.change(LedSpriteProperty.Y, 1)
            if fruit.is_touching(basket):
                game.add_score(1)
                fruit.delete()
    elif game.score() < 100:
        for index3 in range(5):
            basic.pause(300)
            fruit.change(LedSpriteProperty.Y, 1)
            if fruit.is_touching(basket):
                game.add_score(1)
                fruit.delete()
    else:
        for index4 in range(5):
            basic.pause(200)
            fruit.change(LedSpriteProperty.Y, 1)
            if fruit.is_touching(basket):
                game.add_score(1)
                fruit.delete()
    if fruit.is_touching_edge():
        music.play_melody("D - - - - - - - ", 500)
        game.remove_life(1)
    fruit.delete()
basic.forever(on_forever2)
