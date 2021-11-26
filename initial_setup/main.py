import pygame

pygame.init()

WIDTH, HEIGHT = 700, 500
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dots challenge")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

