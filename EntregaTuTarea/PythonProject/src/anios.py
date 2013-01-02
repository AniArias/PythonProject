import pygame
import state
import game
import random
import title
import ejercicio
class Anios(state.State):
   
    def __init__(self,nivel):
        self.timer = pygame.time.Clock()
        self.display = pygame.display.get_surface()
        self.nivel = nivel
        self.teclas = ""
        self.nombre = ""
        self.random = random.randint(0,1)
        self.respuesta=0        
        self.music = pygame.mixer.Sound("data/sound/game.wav")
        self.music.play(loops=-1)
        self.perdio=pygame.mixer.Sound("data/sound/perdiste.wav")
        self.termino = False
        self.background = pygame.image.load("data/images/cuantosanios.jpg").convert_alpha()
        
    def exit(self):
        self.music.stop()
        
   