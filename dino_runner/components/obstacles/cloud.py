from dino_runner.components.obstacles.cloud_manager import *

class Cloud(Cloud):
    def __init__(self, images):
        super().__init__(images)
        
        self.rect.y = 90