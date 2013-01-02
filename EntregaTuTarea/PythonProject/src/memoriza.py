import pygame
import state
import game
import random
import title
import surface_manager
import anios

class Memoria(state.State):

    def __init__(self,nivel):
        self.timer = pygame.time.Clock()
        self.display = pygame.display.get_surface()
        self.nivel = nivel
        self.teclas = ""
        self.nombre = ""
        self.random = random.randint(0,2)
        self.random2 = random.randint(0,1)
        self.respuesta=0  
        
        '''FONDO CUALQUIERA, BUSCARRR!!!'''
        self.background = pygame.image.load("data/images/city.png").convert_alpha()
            
        self.oportunidad = pygame.mixer.Sound("data/sound/oportunidad.wav")
        self.delayopor= pygame.time.delay(int(self.oportunidad.get_length()*1000))
        
        self.perdio = pygame.mixer.Sound("data/sound/perdiste.wav")
        self.delayper= pygame.time.delay(int(self.perdio.get_length()*1000))
        
        self.instru = pygame.mixer.Sound("data/sound/instruccionesmemoriza.wav")
        self.delayinstru= pygame.time.delay(int(self.instru.get_length()*1000))
        
        self.instru.play()
        self.delayinstru.__init__
        
        self.termino = False
        self.correcto= False
        self.oportunidades = 0
        self.memoria1=pygame.mixer.Sound("data/sound/memoriaescuela1.wav")
        self.memoria2=pygame.mixer.Sound("data/sound/memoriaescuela2.wav")
        self.memoria3=pygame.mixer.Sound("data/sound/memoriaescuela3.wav")
        self.memoria4=pygame.mixer.Sound("data/sound/memoriajardin1.wav")
        self.memoria5=pygame.mixer.Sound("data/sound/memoriajardin2.wav")
        self.seleccion_memoria()
        print(self.respuesta)
    def exit(self):
        self.instru.stop()