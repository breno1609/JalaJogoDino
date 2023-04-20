import pygame
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
FONT_STYLE = "freesansbold.ttf"
# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))
MENU = pygame.image.load(os.path.join(IMG_DIR, 'Other/backmenu2.jpg'))
COIN = [
    pygame.image.load(os.path.join(IMG_DIR, 'Other/coin/star1.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/coin/star2.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/coin/star3.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/coin/star5.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/coin/star6.png'))
]

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

LOGODINORUN = pygame.image.load(os.path.join(IMG_DIR, 'Other/logo.png'))

pygame.mixer.init()
SOUNDTRACK = pygame.mixer.Sound('dino_runner/assets/Sounds/soundtrack.mp3')
SOUNDTRACK.set_volume(0.5)
DEATHSOUND = pygame.mixer.Sound('dino_runner/assets/Sounds/death.wav')
HITSOUND = pygame.mixer.Sound('dino_runner/assets/Sounds/hit01.wav')

JUMP_SOUND = pygame.mixer.Sound('dino_runner/assets/Sounds/jump.wav')
JUMP_SOUND.set_volume(0.7)

BACKGROUND = pygame.image.load(os.path.join(IMG_DIR, "Background/Background.png"))
BG = pygame.image.load(os.path.join(IMG_DIR, 'Background/Floor.png'))

BIRD2 = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird2/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird2/Bird2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird2/Bird3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird2/Bird4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird2/Bird5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird2/Bird6.png"))
]


DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
HAMMER_TYPE = "hammer"