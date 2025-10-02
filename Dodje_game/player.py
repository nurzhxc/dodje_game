import pygame
from config import WIDTH, HEIGHT, PLAYER_COLOR, GROUND_HEIGHT

class Player:
    def __init__(self, walk_channel, walk_sound):
        self.width = 50
        self.height = 70
        #Это позиция нашего героя которая фиксированна по вертикали
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - GROUND_HEIGHT - self.height  #чуть выше низа
        self.speed = 7
        self.walk_channel = walk_channel
        self.walk_sound = walk_sound

        try:
            self.image = pygame.image.load('assets/fighter.png')
            self.image = pygame.transform.scale(self.image, (self.width,self.height))
        except Exception:
            self.image = None

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        moving = False

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
            moving = True

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
            moving = True
            if moving and not self.walk_channel.get_busy():
                self.walk_channel.play(self.walk_sound)
        #Ставим ограничение по горизонтали
        if self.rect.left <0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        #Вертикальная позиция у нас зафиксирована тоесть персонаж не сможет идти вверх или вниз
        self.rect.y = self.y

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, self.rect)
        else:
            pygame.draw.rect(screen, PLAYER_COLOR, self.rect)