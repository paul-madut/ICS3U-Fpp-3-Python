#!/usr/bin/env python3

# Created by: Paul Madut
# Created on: Oct 2019
# This program changes the background of the Pybadge

import ugame
import stage

# an image bank of CircuitPython
image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")

sprites = []

def main():


    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 10 , 8 )

    alien = stage.Sprite(image_bank_1, 9, 64, 56)
    sprites.append(alien)
    ship = stage.Sprite(image_bank_1, 5, 75, 56)
    sprites.insert(0, ship)

    # setting up the background to show up on the PyPadge
    # setting up the frame rate to 60fps
    game = stage.Stage (ugame.display, 60)
    game.layers = sprites + [background]

    game.render_block()

    while True:
        game.render_sprites(sprites)
        game.tick()

if __name__ == "__main__":
    main()