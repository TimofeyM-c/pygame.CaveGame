import pygame


class sn:
    def __init__(self, x, y, wig, hig, color, facing):
        self.x = x
        self.y = y
        self.wig = wig
        self.hig = hig
        self.color = color
        self.facing = facing
        self.vel = 4 * facing

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.wig, self.hig))


class enemy:
    def __init__(self, x, y, wig, hig, color, facing, hp):
        self.x = x
        self.y = y
        self.wig = wig
        self.hig = hig
        self.color = color
        self.facing = facing
        self.vel = 2 * facing
        self.hp = hp

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.wig, self.hig))


class enemy2:
    def __init__(self, x, y, wig, hig, color, facing, hp):
        self.x = x
        self.y = y
        self.wig = wig
        self.hig = hig
        self.color = color
        self.facing = facing
        self.vel = 3 * facing
        self.hp = hp

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.wig, self.hig))


class heal:
    def __init__(self, x, y, hei, wei, color):
        self.x = x
        self.y = y
        self.hei = hei
        self.wei = wei
        self.color = color

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.wei, self.hei))
