import pygame
import random
from config import WIDTH, HEIGHT, ENEMY_COLOR

class Enemy:
    def __init__(self):
        self.width = 40
        self.height = 40
        self.x = random.randint(0, WIDTH - self.width)
        self.y = -self.height #Предметы падают за пределами экрана (сверху)
        self.speed = random.randint(9,11)
        try:
            self.image = pygame.image.load('assets/dumbbell.png')
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
        except Exception:
            self.image = None

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.rect.y += self.speed
    def draw(self, screen):
        if self.image:
            screen.blit(self.image, self.rect)
        else:
            pygame.draw.rect(screen, ENEMY_COLOR, self.rect)

    def off_screen(self, height):
        return self.rect.top > height
