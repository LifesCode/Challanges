import pygame
import random as r

pygame.init()

WIDTH, HEIGHT = 1080, 720
BG_COLOR = (0, 0, 0)  # default is (0, 150, 150)
BG = pygame.Surface((WIDTH, HEIGHT))
BG.fill(BG_COLOR)  # set screen with background color
FPS = 30
MOUSE_LINE_COLOR = (0, 0, 255)
CONNECTING_DISTANCE = 200
DOT_CLUSTER_DISTANCE = 80
DOT_NUMBER = 200
MAX_DOT_NUMBER = DOT_NUMBER*1.5
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dots challenge")


class Dot:
    def __init__(self, x=None, y=None):
        self.position = (r.randint(0, WIDTH), r.randint(0, HEIGHT)) if x is None else (x, y)
        self.speed = (r.randint(0, 3), r.randint(0, 3))
        self.size = 2
        self.color = (255, 255, 255)
        self.rect = ()
        self.update_rect()

    def update_rect(self):
        self.rect = (self.position[0], self.position[1], self.size, self.size)

    def update_speed(self):
        if r.random() > 0.95:
            self.speed = ((self.speed[0]+r.random()*r.choice([1, -1])) % 4,
                          (self.speed[1]+r.random()*r.choice([1, -1])) % 4)
        if r.random() > 0.95:
            self.speed = (self.speed[0]*-1, self.speed[1])
        if r.random() > 0.95:
            self.speed = (self.speed[0], self.speed[1]*-1)

    def update(self):
        self.position = ((self.position[0]+self.speed[0]) % WIDTH, (self.position[1]+self.speed[1]) % HEIGHT)
        self.update_rect()
        self.update_speed()

    def draw(self, screen_in):
        pygame.draw.rect(screen_in, self.color, self.rect, self.size)
        self.update()


def refresh(screen_in, dots):
    screen_in.blit(BG, (0, 0))
    [dot.draw(screen_in) for dot in dots]
    draw_straight_lines(screen, dots)
    pygame.display.update()


def vector_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def draw_straight_lines(screen_in, dots):
    mouse_position = pygame.mouse.get_pos()
    for dot_main in dots:
        for dot_in in dots:
            vector = vector_distance(dot_main.position, dot_in.position)
            if dot_main is not dot_in and vector <= DOT_CLUSTER_DISTANCE:
                # default was (255*vector//DOT_CLUSTER_DISTANCE) if vector > DOT_CLUSTER_DISTANCE*0.6 else 150
                color = 255-(255*vector//DOT_CLUSTER_DISTANCE) if vector > DOT_CLUSTER_DISTANCE*0.6 else 100
                pygame.draw.line(screen_in, (0, color, color), dot_main.position, dot_in.position, 1)
        if vector_distance(mouse_position, dot_main.position) <= CONNECTING_DISTANCE:
            pygame.draw.line(screen_in, MOUSE_LINE_COLOR, mouse_position, dot_main.position, 1)


def main():
    dots = [Dot() for _ in range(DOT_NUMBER)]
    while True:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif pygame.mouse.get_pressed(3)[0] and len(dots) < MAX_DOT_NUMBER:
                x, y = pygame.mouse.get_pos()
                dots.append(Dot(x, y))
        refresh(screen, dots)


if __name__ == "__main__":
    main()
