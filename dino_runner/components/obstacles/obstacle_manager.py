import pygame
import random

from dino_runner.components.obstacles.cactus import *
from dino_runner.components.obstacles.bird import *
from dino_runner.utils.constants import *
from dino_runner.components.power_ups.power_up_manager import PowerUpManager


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        
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
                self.tipo_obstacle = 'cactus'
            elif random_obstacle == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS, 300))
                self.tipo_obstacle = 'cactus'
            
            elif random_obstacle == 3:
                self.obstacles.append(Bird(BIRD2))
                self.tipo_obstacle = 'bird'
            
            else:
                self.obstacles.append(Bird(BIRD))
                self.tipo_obstacle = 'bird'
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    self.lose_condition(game)
                    break
                elif game.player.has_power_up:
                    if game.player.type == SHIELD_TYPE and self.tipo_obstacle == 'bird':
                        self.obstacles.remove(obstacle)
                    elif game.player.type == HAMMER_TYPE and self.tipo_obstacle == 'cactus':
                        self.obstacles.remove(obstacle)
                    else:
                        game.player.type = DEFAULT_TYPE
                        self.lose_condition(game)
    
    def reset_obstacles(self):
        self.obstacles.clear()
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)