import pygame
import state
import game
import random
import title
import surface_manager

class Ejercicio(state.State):
    def __init__(self,nivel,anios):
        self.timer = pygame.time.Clock()
        self.display = pygame.display.get_surface()
        self.nivel = nivel
        self.teclas = ""
        self.nombre = ""
        self.random = random.randint(0,1)
        self.respuesta=0     
        self.anios = anios   
        
        '''FONDO CUALQUIERA, BUSCAR!!!'''
        
        self.background = pygame.image.load("data/images/paisaje.jpg").convert_alpha()
        
        self.music = pygame.mixer.Sound("data/sound/game.wav")
        self.delaymu= pygame.time.delay(int(self.music.get_length()*1000))
        
        self.perdio = pygame.mixer.Sound("data/sound/perdiste.wav")
        self.delayper= pygame.time.delay(int(self.perdio.get_length()*1000))
        
        self.oportunidad = pygame.mixer.Sound("data/sound/oportunidad.wav")
        self.delayopor= pygame.time.delay(int(self.oportunidad.get_length()*1000))
        
        self.instrucciones = pygame.mixer.Sound("data/sound/instruccionesejercicios.wav")
        self.delayins= pygame.time.delay(int(self.instrucciones.get_length()*1000))
        
        self.instrucciones.play()
        self.delayins.__init__

        self.music.play()
        
        self.termino = False
        
       
        self.anos=7
        self.correcto= False
        self.oportunidades = 0
        
        print(self.random)
        print(self.nivel)
        print(self.anios)
        print(self.respuesta)
        self.seleccion_ejercicio()
        print(self.random)
        print(self.nivel)
        print(self.anios)
        print(self.respuesta)
        
    def exit(self):
        self.music.stop()
        
    def reason(self):
        if self.teclas == str(self.respuesta):
            self.correcto= True
            print(self.random)
            print(self.nivel)
            return game.Game(self.nivel)
        
        elif self.teclas != str(self.respuesta) and self.termino and not self.correcto:
            print(self.respuesta)
            print("no entro")
            self.oportunidad = pygame.mixer.Sound("data/sound/oportunidad.wav")
            self.delayopor= pygame.time.delay(int(self.oportunidad.get_length()*1000))
            self.oportunidades +=1
            
            if self.oportunidades > 3:
                print(self.teclas)
                print(self.respuesta)
                print(self.random)
                print(self.nivel)
                self.perdio = pygame.mixer.Sound("data/sound/perdiste.wav")
                self.delayper= pygame.time.delay(int(self.perdio.get_length()*1000))
                return title.Title()
            else:
                self.letras=""
                self.termino=False
                self.correcto=False
                self.nombre=""

    def act(self):
        self.timer.tick(60)
        surface_manager.clear(self.display, self.background)
        self.display.blit(self.background, (0, 0))
        pygame.display.flip()
        if not self.termino:  
            eventos=pygame.event.get()
            for evento in eventos:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_F4:
                        self.teclas = self.nombre
                        self.termino = True
                        print(self.teclas)
                    elif evento.key == pygame.K_BACKSPACE and len(self.nombre)>0:
                        self.nombre= self.nombre[0:len(self.nombre)-1]
                    else:
                        self.nombre= self.nombre + pygame.key.name(evento.key)
                        print(self.nombre)
            
        
    def seleccion_ejercicio(self):

        '''JARDIN'''
        if self.random == 0 and self.nivel == 1 and self.anios >= str(6) and self.anios < str(8):
            self.background = pygame.image.load("data/images/ejerciciojardin1.jpg").convert_alpha()
            self.respuesta=8
        
        if self.random == 1 and self.nivel == 1 and self.anios >= str(6) and self.anios < str(8):
            self.background = pygame.image.load("data/images/ejerciciojardin2").convert_alpha()
            self.respuesta=9
 
        if self.random == 2 and self.nivel == 1 and self.anios >= str(6) and self.anios < str(8):
            self.background = pygame.image.load("data/images/ejerciciojardin3.jpg").convert_alpha()
            self.respuesta=7
        
        ''' ESCUELA 8-9'''
        if self.random == 0 and self.nivel == 2 and self.anios >= str(8) and self.anios <= str(9):
            self.background = pygame.image.load("data/images/ejercicioescuela1.jpg").convert_alpha()
            self.respuesta= 5029092
            
        if self.random == 1 and self.nivel == 2 and self.anios >= str(8) and self.anios <= str(9):
            self.background = pygame.image.load("data/images/ejercicioescuela2.jpg").convert_alpha()
            self.respuesta= 9369924

        if self.random == 2 and self.nivel == 2 and self.anios >= str(8) and self.anios <= str(9):
            self.background = pygame.image.load("data/images/ejercicioescuela3.jpg").convert_alpha()
            self.respuesta= 54
        
        ''' ESCUELA 10-12'''
            
        if self.random == 0 and self.nivel == 2 and self.anios >= str(10) and self.anios <= str(12):
            self.background = pygame.image.load("data/images/ejercicioescuela4.jpg").convert_alpha()
            self.respuesta= 60
            
        if self.random == 1 and self.nivel == 2 and self.anios >= str(10) and self.anios <= str(12):
            self.background = pygame.image.load("data/images/ejercicioescuela5.jpg").convert_alpha()
            self.respuesta= 6

        if self.random == 2 and self.nivel == 2 and self.anios >= str(10) and self.anios <= str(12):
            self.background = pygame.image.load("data/images/ejercicioescuela6.jpg").convert_alpha()
            self.respuesta= 35
      
