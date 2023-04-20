import pygame
import random

from dino_runner.components.obstacles.cactus import *
from dino_runner.components.obstacles.bird import *
from dino_runner.utils.constants import *
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.obstacles.cloud_manager import Cloud
from dino_runner.components.game import *


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.cloud = []
        
    def lose_condition(self,game):
        HITSOUND.play()
        pygame.time.delay(500)
        game.life -=1
        self.reset_obstacles()
        game.death_count += 1
        if game.life == 0:
            game.playing = False
            DEATHSOUND.play()
    
    def update(self, game):
        if len(self.obstacles) == 0:
            random_obstacle = random.randint(0, 3)
            if random_obstacle == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS, 325))
            elif random_obstacle == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS, 300))
            elif random_obstacle == 3:
                self.obstacles.append(Bird(BIRD2))
            else:
                self.obstacles.append(Bird(BIRD))
        
        if len(self.cloud) == 0:
            self.cloud.append(Cloud(CLOUD))
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    self.lose_condition(game)
                    break
                elif game.player.has_power_up:
                    if game.player.type == SHIELD_TYPE and isinstance(obstacle, Bird):
                        self.obstacles.remove(obstacle)
                    elif game.player.type == HAMMER_TYPE and isinstance(obstacle, Cactus):
                        self.obstacles.remove(obstacle)
                    else:
                        game.player.type = DEFAULT_TYPE
                        self.lose_condition(game)
        
        for cloud in self.cloud:
            cloud.update(game.game_speed, self.cloud)
    
    def reset_obstacles(self):
        self.obstacles.clear()
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            
        for cloud in self.cloud:
            cloud.draw(screen)