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