import pygame
import random

from dino_runner.components.obstacles.cactus import *
from dino_runner.components.obstacles.bird import *
from dino_runner.utils.constants import *


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        
    def lose_condition(self,game):
        HITSOUND.play()
        pygame.time.delay(500)
        game.life -=1
        self.reset_obstacles()
        if game.life == 0:
            game.playing = False
            DEATHSOUND.play()
            game.death_count += 1
    
    def update(self, game):
        if len(self.obstacles) == 0:
            random_obstacle = random.randint(0, 2)
            if random_obstacle == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
                self.item = 1
            elif random_obstacle == 1:
                self.obstacles.append(CactusGrandes(LARGE_CACTUS))
                self.item = 1
            else:
                self.obstacles.append(Bird(BIRD))
                self.item = 2
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    self.lose_condition(game)
                    break
                elif game.player.has_power_up:
                    if game.player.type == SHIELD_TYPE and self.item == 2:
                        self.obstacles.remove(obstacle)
                    elif game.player.type == HAMMER_TYPE and self.item == 1:
                        self.obstacles.remove(obstacle)
                    else:
                        game.player.type = DEFAULT_TYPE
                        self.lose_condition()
    
    def reset_obstacles(self):
        self.obstacles.clear()
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)