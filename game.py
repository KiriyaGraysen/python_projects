import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Termux Dodge")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Player settings
player_radius = 25
player_x = WIDTH // 2
player_y = HEIGHT - 100

# Enemy settings
enemy_size = 50
enemy_speed = 7
enemies = []

# Clock to control frame rate
clock = pygame.time.Clock()
score = 0
font = pygame.font.SysFont("monospace", 35)

def spawn_enemy():
    x_pos = random.randint(0, WIDTH - enemy_size)
    enemies.append([x_pos, 0])

running = True
while running:
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Move player to touch/mouse position
        elif event.type == pygame.MOUSEMOTION:
            # event.pos returns a tuple (x, y)
            mouse_x, mouse_y = event.pos
            player_x = mouse_x
            # We keep player_y fixed at the bottom for this game

    # 2. Update Game Logic
    # Spawn enemies roughly every 30 frames
    if random.randint(1, 30) == 1:
        spawn_enemy()

    # Move enemies
    for enemy in enemies:
        enemy[1] += enemy_speed
        
        # Check Collision
        # Simple box vs circle collision check
        e_rect = pygame.Rect(enemy[0], enemy[1], enemy_size, enemy_size)
        p_rect = pygame.Rect(player_x - player_radius, player_y - player_radius, player_radius*2, player_radius*2)
        
        if e_rect.colliderect(p_rect):
            print(f"Game Over! Final Score: {score}")
            score = 0
            enemies = [] # Clear enemies to restart

    # Remove enemies that go off screen
    # (We iterate backwards to safely remove items from a list)
    for i in range(len(enemies)-1, -1, -1):
        if enemies[i][1] > HEIGHT:
            enemies.pop(i)
            score += 1

    # 3. Drawing
    screen.fill(BLACK)

    # Draw Player
    pygame.draw.circle(screen, BLUE, (player_x, player_y), player_radius)

    # Draw Enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_size, enemy_size))

    # Draw Score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
