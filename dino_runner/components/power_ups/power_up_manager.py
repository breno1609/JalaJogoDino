import random
import pygame

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.life import Heart
from dino_runner.components.power_ups.coin import Coin
from dino_runner.components.game import *


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.life = []
        self.when_appears = 100
        self.heart = 200

    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(200, 300)
            randomic_choice = random.randint(0, 1)
            if randomic_choice == 0:
                self.power_ups.append(Shield())
            elif randomic_choice == 1:
                self.power_ups.append(Hammer())
        
        if len(self.life) == 0 and self.heart == score:
            self.heart += random.randint(300, 400)
            
            choice_randomic = random.randint(0, 1)
            if choice_randomic == 0:
                self.life.append(Heart())
                self.tipo_poder = 'heart'
            elif choice_randomic == 1:
                self.life.append(Coin(COIN))
                self.tipo_poder = 'coin'

    def update(self, game):
        self.generate_power_up(game.score)
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            
            if game.player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                game.player.shield = True
                game.player.hammer = True
                game.player.has_power_up = True
                game.player.type = power_up.type
                game.player.power_up_time = power_up.start_time + (power_up.duration * 1000)

                self.power_ups.remove(power_up)
        
        for heart in self.life:
            heart.update(game.game_speed, self.life)
            
            if game.player.dino_rect.colliderect(heart.rect) and self.tipo_poder == 'heart':
                self.life.remove(heart)
                game.life += 1
            elif game.player.dino_rect.colliderect(heart.rect) and self.tipo_poder == 'coin':
                self.life.remove(heart)
                game.score += 100

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
        
        for heart in self.life:
            heart.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)