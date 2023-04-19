import pygame
import random

from dino_runner.components.obstacles.cactus import *
from dino_runner.components.obstacles.bird import *
from dino_runner.utils.constants import *

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
    
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
                    game.life -= 1
                    pygame.time.delay(1000)
                    game.playing = False
                    game.death_count += 1
                    break
                elif game.player.has_power_up:
                    if game.player.type == SHIELD_TYPE and self.item == 2:
                        self.obstacles.remove(obstacle)
                    elif game.player.type == HAMMER_TYPE and self.item == 1:
                        self.obstacles.remove(obstacle)
                    else:
                        game.player.type = DEFAULT_TYPE
                        pygame.time.delay(1000)
                        game.playing = False
                        game.death_count += 1
    
    def reset_obstacles(self):
        self.obstacles.clear()
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)