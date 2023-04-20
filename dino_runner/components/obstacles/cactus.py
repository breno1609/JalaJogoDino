import random

from dino_runner.components.obstacles.obstacle import *


class Cactus(Obstacle):
    def __init__(self, image, POS_Y):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = POS_Y
    
