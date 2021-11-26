import pygame
import random as r

pygame.init()

WIDTH, HEIGHT = 700, 500
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


if __name__ == "__main__":
    main()
