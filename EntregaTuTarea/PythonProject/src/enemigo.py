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
                game.update_caritas()


class Enemy_L2(pygame.sprite.DirtySprite):
    def __init__(self,lista):
        super(Enemy_L2, self).__init__()
        self.display = pygame.display.get_surface()
        enemy_sprite = pygame.image.load("data/images/enemy_frame4.png").convert_alpha()
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

    def update(self):
        self.check_if_hit()
        
        if self.is_hit:
            surface_manager.remove(self)
        
        if self.on_platform_L2():
            self.is_falling = False
            
            if self.pos_x < self.anc_plat and self.is_mov_der:
                self.pos_x += 3
                
            if self.pos_x >= self.anc_plat:
                self.is_mov_der = False
            
            if self.pos_x > self.posx_plat and not self.is_mov_der:
                self.pos_x -= 3
            
            if self.pos_x <= self.posx_plat:
                self.is_mov_der = True

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

