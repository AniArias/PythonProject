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
        
    def reason(self):
        if self.teclas == self.nombre and self.termino == True:
            self.perdio.play()
            print("entro")
            return ejercicio.Ejercicio(self.nivel, self.teclas)

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
                        print(self.nombre)
            
       