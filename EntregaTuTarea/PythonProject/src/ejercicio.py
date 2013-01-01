import pygame
import state
import game
import random
import title

class Ejercicio(state.State):
   
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
        self.background = pygame.image.load("data/images/paisaje.jpg").convert_alpha()
        self.seleccion_ejercicio()
        self.correcto= False
        self.oportunidades = 0
        
    def exit(self):
        self.music.stop()
        
        
    def reason(self):
        if self.teclas == str(self.respuesta):
            self.correcto= True
            print(self.random)
            print(self.nivel)
            return game.Game(self.nivel)
        
        elif self.teclas != str(self.respuesta) and self.termino and not self.correcto:
            self.perdio.play()# audio de que se le esta dando otra oportunidad
            self.oportunidades +=1
            
            if self.oportunidades > 3:
                print(self.teclas)
                print(self.respuesta)
                print(self.random)
                print(self.nivel)
                self.perdio.play()# audio de perdio
                return title.Title()
            else:
                self.letras=""
                self.termino=False
                self.correcto=False
                self.nombre=""

    def act(self):
        self.display.blit(self.background, (0, 0))
        pygame.display.flip()
        if not self.termino:  
            eventos=pygame.event.get()
            for evento in eventos:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_F3:
                        self.teclas = self.nombre
                        self.termino = True
                    elif evento.key == pygame.K_BACKSPACE and len(self.nombre)>0:
                        self.nombre= self.nombre[0:len(self.nombre)-1]
                    else:
                        self.nombre= self.nombre + pygame.key.name(evento.key)
            
       
    def seleccion_ejercicio(self):
        
        
        if self.random == 0 and self.nivel == 1:
            self.background = pygame.image.load("data/images/paisaje.jpg").convert_alpha()
            self.respuesta=10
        
        if self.random == 1 and self.nivel == 1:
            self.background = pygame.image.load("data/images/city.png").convert_alpha()
            self.respuesta=11
        '''
        if self.random == 2 and self.nivel == 1:
            self.background = pygame.image.load("data/images/paisaje.jpg").convert_alpha()
            self.respuesta=11
        
        if self.random == 3 and self.nivel == 1:
            self.background = pygame.image.load("data/images/paisaje.jpg").convert_alpha()
            self.respuesta=11
        
        if self.random == 4 and self.nivel == 1:
            self.background = pygame.image.load("data/images/paisaje.jpg").convert_alpha()
            self.respuesta=11
         '''   
        if self.random == 0 and self.nivel == 2:
            self.background = pygame.image.load("data/images/city.png").convert_alpha()
            self.respuesta=14
        
        if self.random == 1 and self.nivel == 2:
            self.background = pygame.image.load("data/images/paisaje.jpg").convert_alpha()
            self.respuesta=15
        '''
        if self.random == 2 and self.nivel == 2:
            self.background = pygame.image.load("data/images/paisaje.jpg").convert_alpha()
            self.respuesta=11
        
        if self.random == 3 and self.nivel == 2:
            self.background = pygame.image.load("data/images/paisaje.jpg").convert_alpha()
            self.respuesta=11
        
        if self.random == 4 and self.nivel == 2:
            self.background = pygame.image.load("data/images/paisaje.jpg").convert_alpha()
            self.respuesta=11    
        '''

