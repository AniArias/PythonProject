import pygame

import state #mod dond se encontrara la clase ke controlara los difernte estados del juego cada vez que ocurra alguna actualizacion
import title # sera el modulo ke presente la pantalla inicial dl juego 
import game

pygame.init()
display = pygame.display.set_mode((800,600))
pygame.display.set_caption("Entrega tu tarea")

class RBR():
    def __init__(self):
        self.sm = state.StateMachine(self, title.Title())

    def start(self):
        while True:
            self.sm.update()

if __name__ == "__main__":
    game = RBR()
    game.start()
    