import arcade
import math
import time

#inizio gioco
Screen_Width = 800
screen_Height = 800
title = "Gioco in 2D"

class Gioco_2d(arcade.Window):

    def __init__(self, larghezza, altezza, titolo):
        super().__init__(larghezza, altezza, titolo)

        self.babbo = None
        self.lista_Sumabi = arcade.SpriteList()
        self.lista_macchina = arcade.SpriteList()

        self.background = None

        # Movimento
        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False
        self.velocita = 4

        #
        self.soundOnOff = True
        self.macchina_spawn_count = 1
        self.punteggio = 0

        self.setup()

    def setup(self):
        self.background = arcade.load_texture("")

        self.Sumabi = arcade.Sprite("", scale=1.0)
        self.Sumabi.center_x = 300
        self.Sumabi.center_y = 100
        self.lista_Sumabi.append(self.Sumabi)

        self.lista_macchina.clear()

        for _ in range(self.macchina_spawn_count):
            self.crea_macchina()
        
    def crea_macchina(self):
        macchina = arcade.Sprite("", scale=1.0)
        macchina.center_x = 800
        macchina.center_y = 100
        self.lista_macchina.append(macchina)

    

def main():
    gioco = Giocoin2D(600, 600, "Gioco in 2D")
    arcade.run()


if __name__ == "__main__":
    main()