import pygame
import random
import surface_manager

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, img_location,nivel):
        super(Plataforma, self).__init__()
        self.display = pygame.display.get_surface()
        self.surface_manager = surface_manager
        self.image = pygame.image.load(img_location).convert_alpha()
        self.image = pygame.transform.scale(self.image, (random.randint(100, 1000), self.image.get_height()))
        self.rect = pygame.Rect(0, 0, self.image.get_width(), self.image.get_height())
        self.pos_x = self.display.get_width()
        self.pos_y = random.randint(self.display.get_height() - self.rect.height*5, self.display.get_height() - self.rect.height)
        self.nivel= nivel
        
    def update(self):
        if self.pos_x < 0 - self.rect.width:
            surface_manager.remove(self)
            return
        else:

            if self.nivel==1:
                self.pos_x -= 1
            elif self.nivel==2:
                self.pos_x -= 3
            elif self.nivel==3:
                self.pos_x -=4
            else:
                self.pos_x -=0  
        self.rect.topleft = (self.pos_x, self.pos_y)

class StartingPlatform(pygame.sprite.Sprite):
    def __init__(self, img_location,nivel):
        super(StartingPlatform, self).__init__()
        self.display = pygame.display.get_surface()
        self.image = pygame.image.load(img_location).convert_alpha()
        self.rect = pygame.Rect(0, 0, self.image.get_width(), self.image.get_height())
        self.pos_x = 0
        self.pos_y = self.display.get_height() - 100
        self.nivel= nivel

    def update(self):
        if self.pos_x < 0 - self.rect.width:
            surface_manager.remove(self)
            return
        else:
            
            if self.nivel==1:
                self.pos_x -= 1
            elif self.nivel==2:
                self.pos_x -= 3
            elif self.nivel==3:
                self.pos_x -=4
            else:
                self.pos_x -=0

        self.rect.topleft = (self.pos_x, self.pos_y)



class EscuelaPlatform(pygame.sprite.Sprite): 
    def __init__(self,img_location,lista):
        super(EscuelaPlatform, self).__init__()
        self.display = pygame.display.get_surface()
        self.image = pygame.image.load(img_location).convert_alpha()
        self.pos_x = lista[0]
        self.pos_y = lista[1] - self.image.get_height()
        self.width = lista[2]
        self.image = pygame.transform.scale(self.image, (self.width, self.image.get_height()) )
        self.rect = pygame.Rect(self.pos_x, self.pos_y , self.image.get_width(),self.image.get_height())
        
    def update(self):
        self.rect.topleft = (self.pos_x, self.pos_y)

