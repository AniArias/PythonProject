import pygame
import random
import time

import state
import plataforma
import enemigo
import surface_manager
import happy_face
import game

class Level(state.State):
    surface_manager = pygame.sprite.RenderUpdates()
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.current_platforms = []
        self.num_of_platforms = 4
        self.background = pygame.image.load("data/images/paisaje.jpg")
        self.display.blit(self.background, (0, 0))
        self.instr2 = pygame.mixer.Sound("data/sound/instruccionesnivel2.wav")
        self.instr3 = pygame.mixer.Sound("data/sound/instruccionesnivel3.wav")
        self.instr2_Rep = True
        self.instr3_Rep = False
        self.nivel=1
        self.enter()
        
    def enter(self):
        new_platform = plataforma.StartingPlatform("data/images/platform.png",self.nivel)
        surface_manager.add(new_platform)
        self.current_platforms.append(new_platform)
        self.time_since_last_enemyspawn = time.clock()
        self.time_since_last_sadspawn = time.clock()

    def exit(self):
        surface_manager.empty()

    def act(self):
        if game.Game.score == 0:
            self.nivel = 1
        elif game.Game.score > 0 and game.Game.score <=3:
            self.nivel = 1
        elif game.Game.score > 3 and game.Game.score <=6 and self.instr2_Rep:
            self.nivel= 2
            self.instr2.play()
            pygame.time.delay(int(self.instr2.get_length()*1000))
            self.instr2_Rep = False
            self.instr3_Rep = True
        elif game.Game.score > 6 and self.instr3_Rep:
                self.nivel=3
                self.instr3.play()
                pygame.time.delay(int(self.instr3.get_length()*1000))
                self.instr3_Rep = False
        
        print(game.Game.score)
        print(self.nivel)
        self.check_platforms()

        if (len(self.current_platforms) < self.num_of_platforms) \
                and ((self.current_platforms[-1].pos_x + self.current_platforms[-1].rect.width) <= (self.display.get_width() - random.randint(100, 600))):
            new_platform = plataforma.Plataforma("data/images/platform.png",self.nivel)
            surface_manager.add(new_platform)
            self.current_platforms.append(new_platform)


        if time.clock() >= self.time_since_last_enemyspawn + .60:
            surface_manager.add(enemigo.Enemigo())
            self.time_since_last_enemyspawn = time.clock()
        
        if time.clock() >= self.time_since_last_sadspawn + .90:
            surface_manager.add(happy_face.Happy())
            self.time_since_last_sadspawn = time.clock()
            
    def check_platforms(self):
        for platform in self.current_platforms:
            if not surface_manager.has(platform):
                self.current_platforms.remove(platform)


class Level_Escuela(state.State):
    surface_manager = pygame.sprite.RenderUpdates()
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.background = pygame.image.load("data/images/city.png")
        self.display.blit(self.background, (0, 0))
        self.lista = self.lista_p()
        self.lista_caritas = self.lista_carit()
        self.esc_cargado = False
        self.enter()

    def enter(self):
        pass
        #new_platform = platform.EscuelaPlatform("data/images/plataforma_2.png",self.lista[0])
        #surface_manager.add(new_platform)
        '''self.current_platforms.append(new_platform)
        self.time_since_last_powerup = time.clock()
        self.time_since_last_enemyspawn = time.clock()
        self.time_since_last_sadspawn = time.clock()'''

    def exit(self):
        surface_manager.empty()

    def act(self):
        if not self.esc_cargado:
            for lista_p in self.lista:
                new_platform = plataforma.EscuelaPlatform("data/images/plataforma_2.png",lista_p)
                surface_manager.add(new_platform)
                enemigos_L2 = enemigo.Enemy_L2(lista_p)
                surface_manager.add(enemigos_L2)
                
            for lista_c in self.lista_caritas:
                carita_L2 = happy_face.Happy_L2(lista_c)
                surface_manager.add(carita_L2)
                
            self.esc_cargado = True
            
    
    def lista_p(self):
        lista = [ [0,self.display.get_height(),self.display.get_width()],
                  [0,self.display.get_height()*4/5,self.display.get_width()/3],
                  [self.display.get_width()*2/3,self.display.get_height()*4/5,self.display.get_width()/3],
                  [self.display.get_width()/12,self.display.get_height()*7/12,self.display.get_width()*2/12],
                  [self.display.get_width()*7/16,self.display.get_height()*7/12,self.display.get_width()*2/17],
                  [self.display.get_width()*21/34,self.display.get_height()*21/50,self.display.get_width()*13/100],
                  [self.display.get_width()*7/10,self.display.get_height()/5,self.display.get_width()*3/10]]
                 
        return lista
    
    def lista_carit(self):
        lista = [[700,500],[100,500],[600,300],[75,100],[400,50],[700,50]]             
        return lista
    

