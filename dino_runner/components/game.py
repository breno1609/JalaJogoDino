import pygame
import time

from dino_runner.utils.constants import *
from dino_runner.utils.constants import BG,ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE
from dino_runner.components.dinosaur import *
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.power_ups.power_up import *


half_screen_height = SCREEN_HEIGHT // 2
half_screen_widht = SCREEN_WIDTH // 2


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.runnimg = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.score = 0
        self.death_count = 0
        self.life = 3
        self.font = pygame.font.Font(FONT_STYLE, 25)
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()

    def execute(self):
        self.runnimg = True
        while self.runnimg:
            if not self.playing:
                self.show_menu()
        
        pygame.display.quit()
        pygame.quit()
    
    def run(self):
        SOUNDTRACK.play(-1)
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        while self.playing:
            self.events()
            self.update()
            self.draw()
        SOUNDTRACK.stop()
    
    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.game_speed = 20
        self.death_count = 0
        self.score = 0
        self.life = 3

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.runnimg = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)
        self.update_score()
        
    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 1.5

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        self.draw_score()
        self.draw_deaths()
        self.draw_life()
        pygame.display.update()
        pygame.display.flip()
        
    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks())/1000, 2)
            
            if time_to_show >=0:
                font = pygame.font.Font(FONT_STYLE, 22)
                self.method_draw_score_deaths(f"Power Up: {time_to_show}",550,100,(255,0,0))
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    
    #PARA REUTILIZAR AS FONTES
    def method_draw_score_deaths(self,texto,x,y,rgb):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_widht = SCREEN_WIDTH // 2
        
        text = self.font.render(texto, True, rgb)
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text, text_rect)
    
    def draw_score(self):
        self.method_draw_score_deaths(f"Score: {self.score}",1000,50,(0,0,0))
        
    def draw_deaths(self):
        self.method_draw_score_deaths(f"Deaths: {self.death_count}",550,50,(178,34,34))
        
    def draw_life(self):
        self.method_draw_score_deaths(f"Life: {self.life}", 200, 50, (255, 0, 0))
    
    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.runnimg = False
            elif event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_s] and self.death_count == 0:
                    self.run()
                #elif pygame.key.get_pressed()[pygame.K_c]:
                    #self.run()
                elif pygame.key.get_pressed()[pygame.K_r]:
                    self.reset_game()
                    self.run()
    
    def show_menu(self):
        self.screen.fill((255, 255, 255))

        if self.death_count == 0:
            self.screen.blit(MENU, (self.x_pos_bg, 0))
            self.screen.blit(LOGODINORUN, (SCREEN_WIDTH - LOGODINORUN.get_width() - 290, 180))
            self.method_draw_score_deaths("Press (s) to start playing.",600,540,(0,0,0))
        else:
            self.screen.blit(ICON, (half_screen_widht - 20, half_screen_height - 140))
            #self.method_draw_score_deaths("Press (c) to continue playing.",600,350,(0,0,0))
            
            self.method_draw_score_deaths("Press (r) to restart playing.",600, 400,(0,0,0))
            
            self.method_draw_score_deaths(f"Your Score: {self.score}",600, 450,(0,255,0))
            
            self.method_draw_score_deaths(f"Death count: {self.death_count}",600,500,(204,0,0))
            
        pygame.display.flip()
        
        self.handle_events_on_menu()