import pygame
import random


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animated Circle with Key Interaction")

clock = pygame.time.Clock()


x, y = WIDTH // 2, HEIGHT // 2
radius = 40
radius_change = 1
color = (0, 150, 255)
speed = 5

running = True

while running:
    screen.fill((30, 30, 30)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                color = (
                    random.randint(0,255),
                    random.randint(0,255),
                    random.randint(0,255)
                )

    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    
    radius += radius_change
    if radius > 60 or radius < 30:
        radius_change *= -1

    pygame.draw.circle(screen, color, (x, y), radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()