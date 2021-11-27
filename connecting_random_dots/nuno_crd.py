import pygame

pygame.init()

WIDTH, HEIGHT = 700, 500
BG_COLOR = (0, 150, 150)
FPS = 60
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dots challenge")




def main():
    while True:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            
        screen.fill(BG_COLOR)
        pygame.display.update()


if __name__ == "__main__":
    main()