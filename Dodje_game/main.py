import pygame
import sys
import time
import random
from config import WIDTH, HEIGHT, FPS, BG_COLOR, GROUND_COLOR, GROUND_HEIGHT
from player import Player
from enemy import Enemy

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("assets/game-music.wav")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

walk_channel = pygame.mixer.Channel(1)
walk_sound = pygame.mixer.Sound("assets/walk.mp3")
walk_sound.set_volume(0.1)

hit_sound = pygame.mixer.Sound("assets/hit.wav")
backround = pygame.image.load("assets/backround.png")

icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)

backround = pygame.transform.scale(backround, (WIDTH, HEIGHT))
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Dodje game: dumbbels rain")
clock = pygame.time.Clock()

player = Player(walk_channel, walk_sound)

enemies = []
enemy_timer = 0

def draw_game_over(screen):
    font = pygame.font.SysFont('arial', 64, bold=True)
    text = font.render("GAME OVER!",True, (255,0,0))
    text_rect =  text.get_rect(center=(WIDTH //2, HEIGHT //2 - 50))
    screen.blit(text, text_rect)

score = 0
font = pygame.font.SysFont(None, 36)
start_time = time.time()

running = True
while running:
    clock.tick(FPS)
    screen.blit(backround, (0,0))

    GROUND_HEIGHT = 50
    pygame.draw.rect(screen, GROUND_COLOR, (0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT))

    current_time = time.time()
    score = int(current_time - start_time)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.handle_keys()

    enemy_timer += 1
    if enemy_timer > 30:
        enemies.append(Enemy())
        enemy_timer = 0

    for enemy in enemies[:]:
        enemy.update()
        if enemy.off_screen(HEIGHT):
            enemies.remove(enemy)
        elif enemy.rect.colliderect(player.rect):  # 💥 Столкновение
            hit_sound.play()        #звук столкновения
            draw_game_over(screen)
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False

    player.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)

    score_text = font.render(f"Score:{score}", True, (0,0,0,))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
