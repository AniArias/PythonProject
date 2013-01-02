import pygame
from pygame.locals import *
import state
import time
import level
import player
import title
import surface_manager

class Game(state.State):
    score = 0
    streak_counter = 0
    combo_timer = time.clock()
    player
    def __init__(self,nivel):
        self.timer = pygame.time.Clock()
        self.display = pygame.display.get_surface()
        self.nivel = nivel
        print("el nivel del juego es")
        print (self.nivel)
        if self.nivel == 1:
            self.level_manager = state.StateMachine(self, level.Level())
        else:
            self.level_manager = state.StateMachine(self, level.Level_Escuela())
        self.player = player.Player(self.nivel)
        Game.player = self.player
        self.background = pygame.image.load("data/images/paisaje.jpg").convert_alpha()
        surface_manager.add(self.player)
        self.music = pygame.mixer.Sound("data/sound/game.wav")
        self.music.play(loops=-1)
        self.perdio=pygame.mixer.Sound("data/sound/perdiste.wav")
        self.p_vez = True
        self.display.blit(self.background, (0, 0))
        pygame.display.flip()
        self.perdio.play()
    def exit(self):
        self.music.stop()
        Game.score = 0
        Game.streak_counter = 0

    def reason(self):
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            self.level_manager.current_state.exit()
            return title.Title()
        if self.player.pos_y > self.display.get_height():
            if Game.streak_counter > 1:
                Game.score += 5 * (Game.streak_counter*2)
            self.level_manager.current_state.exit()
            return title.Title()
        if self.player.shurikens<=0:
            self.perdio.play()
            self.level_manager.current_state.exit()
            return title.Title()
 
        if self.player.current_life<=0:
            self.player.pos_x = self.display.get_width()/2
            self.player.pos_y = 450
            self.player.current_life = 10

    def act(self):
        
        self.timer.tick(60)
        surface_manager.clear(self.display, self.background)
        if self.p_vez:
            self.perdio.play()
            self.p_vez = False
        
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            self.player.mover_der()
        
        if keys[K_LEFT]:
            self.player.mover_izq()
        
        if keys[K_UP]:
            self.player.jump()
        else:
            self.player.stop_jumping()
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_1:
                    self.player.throw_shuriken()
        
 
        self.level_manager.update()
        surface_manager.update()
        dirty_rects = surface_manager.draw(self.display)
        pygame.display.update(dirty_rects)


def update_caritas():
    Game.score += 1
