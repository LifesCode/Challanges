import pygame
import random as r

pygame.init()

WIDTH, HEIGHT = 700, 500
BG_COLOR = (0, 150, 150)
FPS = 60
CONNECTING_DISTANCE = 80
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dots challenge")


def main():
    while True:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        pygame.draw.rect(screen, BG_COLOR, (200, 200, 200, 200))
        pygame.display.update()


if __name__ == "__main__":
    main()
