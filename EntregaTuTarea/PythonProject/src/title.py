import sys
import pygame
from pygame.locals import *
import state
import memoriza
#import surface_manager

class Title(state.State):
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.background = pygame.image.load("data/images/paisaje.jpg")
        self.font_manager = pygame.font.Font("data/fonts/SEVEMFBR.TTF", 64)
        self.help_font_manager = pygame.font.Font("data/fonts/SEVEMFBR.TTF", 28)
        self.title_font_manager = pygame.font.Font("data/fonts/SEVEMFBR.TTF", 128)

        self.title = self.title_font_manager.render("ENTREGA TU TAREA", True, (255, 255, 255))
        self.title_rect = pygame.Rect((self.display.get_width()/2 - self.title.get_width()/2, self.display.get_height()/2 - self.title.get_height()*2),
            (self.title.get_width(), self.title.get_height()))
        self.title_color = "white"
        
        self.jardin_game = self.font_manager.render("JARDIN", True, (255, 255, 255))
        self.jardin_game_rect = pygame.Rect((self.display.get_width()/4 - self.jardin_game.get_width()/2, self.display.get_height()/2 - self.jardin_game.get_height()),
            (self.jardin_game.get_width(), self.jardin_game.get_height()))
        
        self.escuela_game = self.font_manager.render("ESCUELA", True, (0, 0, 0))
        self.escuela_game_rect = pygame.Rect((self.display.get_width()*3/4 - self.escuela_game.get_width()/2, self.display.get_height()/2 - self.escuela_game.get_height()),
            (self.escuela_game.get_width(), self.escuela_game.get_height()))
        
        self.developers = self.font_manager.render("CREADORES", True, (0, 0, 0))
        self.dev_rect = pygame.Rect((self.display.get_width()/4 - self.developers.get_width()/2,self.display.get_height()*4/5 - self.developers.get_height()),
                                    (self.developers.get_width(), self.developers.get_height()))

        self.exit_game = self.font_manager.render("EXIT", True, (0, 0, 0))
        self.exit_game_rect = pygame.Rect((self.display.get_width()*7/8 - self.exit_game.get_width()/2, self.display.get_height()*4/5 - self.exit_game.get_height()),
            (self.exit_game.get_width(), self.exit_game.get_height()))

        self.current_choice = 1
        
        self.show_help = False
            
        self.timer = pygame.time.Clock()

        self.music = pygame.mixer.Sound("data/sound/title_highscore.wav")
        self.music.play(loops=-1)

    def exit(self):
        self.music.stop()
        self.display.blit(self.background, (0, 0))
        pygame.display.flip()

    def reason(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if self.show_help:
                        self.show_help = False
                    else:
                        if self.current_choice == 1:
                            return memoriza.Memoria(self.current_choice)
                        elif self.current_choice == 2:
                            return memoriza.Memoria(self.current_choice)

                        elif self.current_choice == 3:
                            self.current_choice = 3
                            
                        elif self.current_choice == 4:
                            pygame.quit()
                            sys.exit()
                if event.key == K_RIGHT:
                    self.next()
                if event.key == K_LEFT:
                    self.previous()
                if event.key == K_DOWN:
                    self.down()
                if event.key == K_UP:
                    self.up()

    def act(self):
        self.timer.tick(40)
        self.animate_title()
        self.display.blit(self.background, (0, 0))
        if self.show_help:
            self.display.blit(self.help_image, self.help_image_rect)
        else:
            self.display.blit(self.title, self.title_rect)
            self.display.blit(self.jardin_game, self.jardin_game_rect)
            self.display.blit(self.escuela_game, self.escuela_game_rect)
            self.display.blit(self.developers,self.dev_rect)
            self.display.blit(self.exit_game, self.exit_game_rect)

        pygame.display.update()

    def next(self):
        if self.current_choice == 1:
            self.jardin_game = self.font_manager.render("JARDIN", True, (0, 0, 0))
            self.escuela_game = self.font_manager.render("ESCUELA", True, (255, 255, 255))
            self.developers = self.font_manager.render("CREADORES",True, (0, 0, 0))
            self.exit_game = self.font_manager.render("EXIT", True, (0, 0, 0))
            self.current_choice = 2
        elif self.current_choice == 2:
            self.jardin_game = self.font_manager.render("JARDIN", True, (0, 0, 0))
            self.escuela_game = self.font_manager.render("ESCUELA", True, (0, 0, 0))
            self.developers = self.font_manager.render("CREADORES",True, (255, 255, 255))
            self.exit_game = self.font_manager.render("EXIT", True, (0, 0, 0))
            self.current_choice = 3
        elif self.current_choice == 3:
            self.jardin_game = self.font_manager.render("JARDIN", True, (0, 0, 0))
            self.escuela_game = self.font_manager.render("ESCUELA", True, (0, 0, 0))
            self.developers = self.font_manager.render("CREADORES",True, (0, 0, 0))
            self.exit_game = self.font_manager.render("EXIT", True, (255, 255, 255))
            self.current_choice = 4
        else:
            self.jardin_game = self.font_manager.render("JARDIN", True, (255, 255, 255))
            self.escuela_game = self.font_manager.render("ESCUELA", True, (0, 0, 0))
            self.developers = self.font_manager.render("CREADORES",True, (0, 0, 0))
            self.exit_game = self.font_manager.render("EXIT", True, (0, 0, 0))
            self.current_choice = 1

    def previous(self):
        if self.current_choice == 1:
            self.jardin_game = self.font_manager.render("JARDIN", True, (0, 0, 0))
            self.escuela_game = self.font_manager.render("ESCUELA", True, (0, 0, 0))
            self.developers = self.font_manager.render("CREADORES",True, (0, 0, 0))
            self.exit_game = self.font_manager.render("EXIT", True, (255, 255, 255))
            self.current_choice = 4
        elif self.current_choice == 2:
            self.jardin_game = self.font_manager.render("JARDIN", True, (255, 255, 255))
            self.escuela_game = self.font_manager.render("ESCUELA", True, (0, 0, 0))
            self.developers = self.font_manager.render("CREADORES",True, (0, 0, 0))
            self.exit_game = self.font_manager.render("EXIT", True, (0, 0, 0))
            self.current_choice = 1
        elif self.current_choice == 3:
            self.jardin_game = self.font_manager.render("JARDIN", True, (0, 0, 0))
            self.escuela_game = self.font_manager.render("ESCUELA", True, (255, 255, 255))
            self.developers = self.font_manager.render("CREADORES",True, (0, 0, 0))
            self.exit_game = self.font_manager.render("EXIT", True, (0, 0, 0))
            self.current_choice = 2
        else:
            self.jardin_game = self.font_manager.render("JARDIN", True, (0, 0, 0))
            self.escuela_game = self.font_manager.render("ESCUELA", True, (0, 0, 0))
            self.developers = self.font_manager.render("CREADORES",True, (255, 255, 255))
            self.exit_game = self.font_manager.render("EXIT", True, (0, 0, 0))
            self.current_choice = 3
    
    def down(self):
        if self.current_choice == 1:
            self.jardin_game = self.font_manager.render("JARDIN", True, (0, 0, 0))
            self.escuela_game = self.font_manager.render("ESCUELA", True, (0, 0, 0))
            self.developers = self.font_manager.render("CREADORES",True, (255, 255, 255))
            self.exit_game = self.font_manager.render("EXIT", True, (0, 0, 0))
            self.current_choice = 3
        elif self.current_choice == 2:
            self.jardin_game = self.font_manager.render("JARDIN", True, (0, 0, 0))
            self.escuela_game = self.font_manager.render("ESCUELA", True, (0, 0, 0))
            self.developers = self.font_manager.render("CREADORES",True, (0, 0, 0))
            self.exit_game = self.font_manager.render("EXIT", True, (255, 255, 255))
            self.current_choice = 4
    
    def up(self):
        if self.current_choice == 3:
            self.jardin_game = self.font_manager.render("JARDIN", True, (255, 255, 255))
            self.escuela_game = self.font_manager.render("ESCUELA", True, (0, 0, 0))
            self.developers = self.font_manager.render("CREADORES",True, (0, 0, 0))
            self.exit_game = self.font_manager.render("EXIT", True, (0, 0, 0))
            self.current_choice = 1
        elif self.current_choice == 4:
            self.jardin_game = self.font_manager.render("JARDIN", True, (0, 0, 0))
            self.escuela_game = self.font_manager.render("ESCUELA", True, (255, 255, 255))
            self.developers = self.font_manager.render("CREADORES",True, (0, 0, 0))
            self.exit_game = self.font_manager.render("EXIT", True, (0, 0, 0))
            self.current_choice = 2
            
    def animate_title(self):
        if self.title_color == "white":
            self.title = self.title_font_manager.render("ENTREGA TU TAREA", True, (0, 0, 0))
            self.title_color = "black"
        else:
            self.title = self.title_font_manager.render("ENTREGA TU TAREA", True, (255, 255, 255))
            self.title_color = "white"

        