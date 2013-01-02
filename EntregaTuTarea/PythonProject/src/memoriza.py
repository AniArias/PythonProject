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
        
    def reason(self):
        if self.teclas == str(self.respuesta):
            self.correcto= True
            print(self.random)
            print(self.nivel)
            return anios.Anios(self.nivel)
        
        elif self.teclas != str(self.respuesta) and self.termino and not self.correcto:
            print(self.respuesta)
            print("no entro")
            self.oportunidad.play()
            self.delayopor.__init__
            self.oportunidades +=1
            
            if self.oportunidades > 3:
                print(self.teclas)
                print(self.respuesta)
                print(self.random)
                print(self.nivel)
                self.perdio.play()
                self.delayper.__init__
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
                    if evento.key == pygame.K_F5:
                        self.teclas = self.nombre
                        self.termino = True
                        print(self.teclas)
                    elif evento.key == pygame.K_BACKSPACE and len(self.nombre)>0:
                        self.nombre= self.nombre[0:len(self.nombre)-1]
                    else:
                        self.nombre= self.nombre + pygame.key.name(evento.key)
                        print(self.nombre)
            
        
    def seleccion_memoria(self):
       
        if self.random2 == 0 and self.nivel == 2:
                self.memoria1.play()
                self.respuesta= "7e563"
        
        if self.random2 == 1 and self.nivel == 2:
                self.memoria2.play()
                self.respuesta= "fw496"
        
        if self.random2 == 2 and self.nivel == 2:
                self.memoria3.play()
                self.respuesta= "12pkf"
        
        if self.random == 0 and self.nivel == 1:
                self.memoria4.play()
                self.respuesta= "2463"
        
        if self.random == 1 and self.nivel == 1:
                self.memoria5.play()
                self.respuesta= "1256"
    