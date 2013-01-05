import time
import pygame
from pygame.locals import *
import arma
import enemigo
import plataforma
import surface_manager
import sad_face

class Player(pygame.sprite.DirtySprite):
    #shuri=10;
    
    def __init__(self, nivel):
        super(Player, self).__init__()
        self.display = pygame.display.get_surface()

        '''
        frame_1 = pygame.image.load("data/images/ninja_frame1.png").convert_alpha()
        frame_2 = pygame.image.load("data/images/ninja_frame2.png").convert_alpha()
        frame_3 = pygame.image.load("data/images/ninja_frame3.png").convert_alpha()
        '''
        frame_1 = pygame.image.load("data/images/cesar_toma_1.png").convert_alpha()
        frame_2 = pygame.image.load("data/images/cesar_toma2.png").convert_alpha()
        frame_3 = pygame.image.load("data/images/cesar_toma3.png").convert_alpha()
        frame_4 = pygame.image.load("data/images/cesar_toma_1.png").convert_alpha()
        frame_5 = pygame.image.load("data/images/cesar_toma2.png").convert_alpha()
        frame_6 = pygame.image.load("data/images/cesar_toma3.png").convert_alpha()
        '''
        frame_4 = pygame.image.load("data/images/ninja_frame1_izq.png").convert_alpha()
        frame_5 = pygame.image.load("data/images/ninja_frame2_izq.png").convert_alpha()
        frame_6 = pygame.image.load("data/images/ninja_frame3_izq.png").convert_alpha()
        '''
        self.frame_set_der = [frame_1, frame_2, frame_3, frame_2]
        self.frame_set_izq = [frame_4, frame_5, frame_6, frame_5]
        self.current_frame = 1
        self.timer = time.clock()
        self.nivel = nivel
        self.image = self.frame_set_der[self.current_frame]
        self.rect = pygame.Rect((0, 0), (self.image.get_width(), self.image.get_height()))
        self.pos_x = 0
        self.pos_y = self.display.get_height() - (100 + self.rect.height)
        self.is_jumping = False
        self.max_jump_height = 256
        self.current_jump = 0
        self.is_falling = True
        self.shurikens = 30
        self.throw_sound = pygame.mixer.Sound("data/sound/throw.wav")
        self.current_life=10
        
    def update(self):

        
        if on_platform(self):
            self.is_jumping = False
            self.is_falling = False
            self.current_jump = 0
            self.dirty = 1
            
        
        if on_enemy(self):
            
            self.current_life-=1
            print (self.current_life)
            
            
        if self.is_falling:
            self.pos_y += 8
            self.dirty = 1
            self.throw_sound

        self.rect.topleft = (self.pos_x, self.pos_y)

    def jump(self):
        if self.current_jump <= self.max_jump_height and not self.is_falling:
            self.is_jumping = True
            self.current_frame = 0
            self.image = self.frame_set_der[self.current_frame]
            self.pos_y -= 10
            self.dirty = 1
            self.current_jump += 10
            if self.current_jump >= self.max_jump_height:
                self.is_falling = True

    def stop_jumping(self):
        self.jumping = False
        self.is_falling = True

    def throw_shuriken(self):
        if self.shurikens > 0:
            self.throw_sound.play()
            surface_manager.add(arma.Arma(self))
            self.shurikens -= 1
            
      

    def mover_der(self):
        try:
            self.current_frame += 1
            self.image = self.frame_set_der[self.current_frame]
        except IndexError:
            self.current_frame = 0
            self.image = self.frame_set_der[self.current_frame]
            
        if(self.pos_x <= self.display.get_width()):
            self.pos_x += 5
            
        self.dirty = 1
    
    
    def mover_izq(self):
        try:
            self.current_frame += 1
            self.image = self.frame_set_izq[self.current_frame]
        except IndexError:
            self.current_frame = 0
            self.image = self.frame_set_izq[self.current_frame]
            
        if(self.pos_x >= 0):
            self.pos_x -= 5
            
        self.dirty = 1
        
def on_sad_face(player):
    collidelist = pygame.sprite.spritecollide(player, surface_manager.surface_list, False)
    for item in collidelist:
        if type(item) is enemigo.Enemigo:
            continue
        elif type(item) is sad_face.Sad():   
            return True  
    return False 
 
def on_enemy(player):
    collidelist = pygame.sprite.spritecollide(player, surface_manager.surface_list, False)

    for item in collidelist:
        if type(item) is enemigo.Enemigo and player.nivel==2 :
            return True
        else:
            return False
    
def on_platform(player):
    collidelist = pygame.sprite.spritecollide(player, surface_manager.surface_list, False)

    for item in collidelist:
        if type(item) is enemigo.Enemigo:   
            continue
        if type(item) is plataforma.Plataforma or type(item) is plataforma.StartingPlatform or type(item) is plataforma.EscuelaPlatform:
            if (player.pos_y + player.rect.height) <= (item.pos_y + 8) and (player.pos_x + player.rect.width) >= item.pos_x:
                return True
    
            

    return False
