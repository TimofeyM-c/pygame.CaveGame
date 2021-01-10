import pygame

pygame.mixer.pre_init(44100, -16, 2, 512)

pygame.init()

win = pygame.display.set_mode((1000, 500))

bomb = pygame.image.load("sprites/bomb.png")

bg = pygame.image.load("sprites/try.png")

staloktit = pygame.image.load("sprites/st1.png")

staloktit2 = pygame.image.load("sprites/st2.png")

heart2 = pygame.image.load("sprites/heart2.png")

goLeft = pygame.image.load("sprites/left.png")

goRight = pygame.image.load("sprites/right.png")

idle = pygame.image.load("sprites/idle.png")

anim = [pygame.image.load("sprites/animation1.png"
                          ), pygame.image.load("sprites/animation2.png")]

pygame.display.set_caption("Cave battle")

pygame.font.init()

pygame.mixer.music.load("C:/Users/1/Desktop/music/arcade.mp3")

shot = pygame.mixer.Sound("C:/Users/1/Desktop/music/bullet.wav")
shot.set_volume(0.4)

explosion = pygame.mixer.Sound("C:/Users/1/Desktop/music/explosion.wav")
explosion.set_volume(0.55)

shortExplosion = pygame.mixer.Sound("C:/Users/1/Desktop/music/shortExplosion.wav")

bonus = pygame.mixer.Sound("C:/Users/1/Desktop/music/bonus.ogg")

hurt = pygame.mixer.Sound("C:/Users/1/Desktop/music/hurt.wav")

pygame.mixer.music.play(-1)

clock = pygame.time.Clock()
