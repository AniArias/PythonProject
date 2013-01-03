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

