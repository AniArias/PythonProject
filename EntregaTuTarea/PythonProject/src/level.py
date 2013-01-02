import pygame
import random
import time

import state
import plataforma
import enemigo
import surface_manager
import sad_face
import game

class Level(state.State):
    surface_manager = pygame.sprite.RenderUpdates()
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.current_platforms = []
        self.num_of_platforms = 4
        self.background = pygame.image.load("data/images/paisaje.jpg")
        self.display.blit(self.background, (0, 0))
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
            self.nivel = 0
        elif game.Game.score > 0 and game.Game.score <=3:
            self.nivel = 1
        elif game.Game.score > 3 and game.Game.score <=6:
            self.nivel= 2
        else:
            self.nivel=3
        
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
            surface_manager.add(sad_face.Sad())
            self.time_since_last_sadspawn = time.clock()
            
    def check_platforms(self):
        for platform in self.current_platforms:
            if not surface_manager.has(platform):
                self.current_platforms.remove(platform)

