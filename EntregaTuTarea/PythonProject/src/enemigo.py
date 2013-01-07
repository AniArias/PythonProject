import random
import pygame
import arma
import game
import surface_manager
import player
import plataforma

class Enemigo(pygame.sprite.DirtySprite):
    def __init__(self):
        super(Enemigo, self).__init__()
        self.display = pygame.display.get_surface()

        enemy_sprite = pygame.image.load("data/images/carita-triste.png").convert_alpha()
        self.image = pygame.transform.flip(enemy_sprite, True, False)
        self.rect = pygame.Rect((0, 0), (self.image.get_width(), self.image.get_height()))
        paths = [[1000, -128, -12, 12], [1000, self.display.get_height()+128, -12, -12]]
        self.pos_x, self.pos_y, self.velx, self.vely = random.choice(paths)
        self.is_hit = False
        self.hit_sound = pygame.mixer.Sound("data/sound/hit.wav")
        self.dirty = 1
        
    def update(self):
        if self.pos_x < 0 - self.rect.width:
            surface_manager.remove(self)

        self.check_if_hit()

        if self.is_hit:
            self.pos_y += 10
            if self.pos_y >= self.display.get_height():
                surface_manager.remove(self)
        if not self.is_hit:                
            self.pos_x += self.velx
            self.pos_y += self.vely

        self.rect.topleft = (self.pos_x, self.pos_y)
        self.dirty = 1

    def check_if_hit(self):
        if self.is_hit:
            return
        collidelist = pygame.sprite.spritecollide(self, surface_manager.surface_list, False)

        for item in collidelist:
            if type(item) is arma.Arma:
                surface_manager.remove(item)
                self.is_hit = True
                self.image = pygame.transform.flip(self.image, False, True)
                self.hit_sound.play()
                #game.update_caritas()


class Enemy_L2(pygame.sprite.DirtySprite):
    def __init__(self,lista):
        super(Enemy_L2, self).__init__()
        self.display = pygame.display.get_surface()
        enemy_sprite = pygame.image.load("data/images/enemy1_L2.png").convert_alpha()
        self.image = pygame.transform.flip(enemy_sprite, True, False)
        self.is_hit = False
        self.posx_plat = lista[0]
        self.pos_x = lista[0] 
        self.pos_y = lista[1] - ( 10+self.image.get_height())
        self.anc_plat = self.pos_x + lista[2]
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.image.get_width(), self.image.get_height())
        self.is_falling = True
        self.is_mov_der = True
        self.hit_sound = pygame.mixer.Sound("data/sound/hit.wav")
        self.dirty = 1
        frame_1 = pygame.image.load("data/images/enemy1_L2.png").convert_alpha()
        frame_2 = pygame.image.load("data/images/enemy2_L2.png").convert_alpha()
        frame_3 = pygame.image.load("data/images/enemy3_L2.png").convert_alpha()
        frame_4 = pygame.image.load("data/images/enemy4_L2.png").convert_alpha()
        frame_5 = pygame.image.load("data/images/enemy5_L2.png").convert_alpha()
        frame_6 = pygame.image.load("data/images/enemy6_L2.png").convert_alpha()
        frame_7 = pygame.image.load("data/images/enemy7_L2.png").convert_alpha()
        frame_8 = pygame.image.load("data/images/enemy8_L2.png").convert_alpha()
        frame_9 = pygame.image.load("data/images/enemy9_L2.png").convert_alpha()
        frame_10 = pygame.image.load("data/images/enemy10_L2.png").convert_alpha()
        self.frame_set_der = [frame_1, frame_2, frame_3, frame_4, frame_5]
        self.frame_set_izq = [frame_6, frame_7, frame_8, frame_9, frame_10]
        self.current_frame = 0
        self.timer = pygame.time.Clock()

    def update(self):
        self.check_if_hit()
        
        if self.is_hit:
            surface_manager.remove(self)
        
        if self.on_platform_L2():
            self.is_falling = False
            
        if self.pos_x < self.anc_plat and self.is_mov_der:
                
            self.pos_x += 1
            try:
                self.timer.tick(50)
                self.current_frame += 1
                self.image = self.frame_set_der[self.current_frame]
            except IndexError:
                self.timer.tick(50)
                self.current_frame = 0
                self.image = self.frame_set_der[self.current_frame]
                
        if self.pos_x >= self.anc_plat:
            self.timer.tick(50)
            self.is_mov_der = False
            self.current_frame = 0
            self.image = self.frame_set_der[self.current_frame]
                
            
        if self.pos_x > self.posx_plat and not self.is_mov_der:
            self.pos_x -= 1
            try:
                self.timer.tick(50)
                self.current_frame += 1
                self.image = self.frame_set_izq[self.current_frame]
            except IndexError:
                self.timer.tick(50)
                self.current_frame = 0
                self.image = self.frame_set_izq[self.current_frame]
            
        if self.pos_x <= self.posx_plat:
            self.timer.tick(50)
            self.is_mov_der = True
            self.current_frame = 0
            self.image = self.frame_set_izq[self.current_frame]

        if self.is_falling:
            self.pos_y += 8
            self.dirty = 1
            
        self.rect.topleft = (self.pos_x, self.pos_y)
        
    def check_if_hit(self):
        if self.is_hit:
            return
        collidelist = pygame.sprite.spritecollide(self, surface_manager.surface_list, False)

        for item in collidelist:
            if type(item) is arma.Arma:
                surface_manager.remove(item)
                self.is_hit = True
                self.image = pygame.transform.flip(self.image, False, True)
                self.hit_sound.play()
    
    def on_platform_L2(self):
        collidelist = pygame.sprite.spritecollide(self, surface_manager.surface_list, False)
    
        for item in collidelist:
            if type(item) is player.Player:
                item.current_life -=1
                continue
            if type(item) is plataforma.EscuelaPlatform:
                if (self.pos_y + self.rect.height) <= (item.pos_y + 8) and (self.pos_x + self.rect.width) >= item.pos_x :
                    return True
                
        return False

