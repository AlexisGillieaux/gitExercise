import pygame
import random
pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Mon jeu Pygame")
clock=pygame.time.Clock()
running = True
dt = 0
screen.fill("black")
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_pos.y>=-200+screen.get_height() / 2:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s] and player_pos.y<=200+screen.get_height() / 2:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]and player_pos.x>=-200+screen.get_width() / 2:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]and player_pos.x<=200+screen.get_width() / 2:
        player_pos.x += 300 * dt
    if keys[pygame.K_t]:
        pos_rond=pygame.Vector2(random.randint(0,screen.get_width()),random.randint(0,screen.get_height()))
        pygame.draw.circle(screen,"yellow",pos_rond,5)
    if keys[pygame.K_0]:
        running=False
    a=0
    if player_pos.x>=500 and a==0:
        pygame.draw.circle(screen,"white",player_pos,10)
        a+=1
    pygame.display.flip()
    dt = clock.tick(60) / 1000  # limits FPS to 60
pygame.quit()