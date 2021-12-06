import pygame
import random as r

pygame.init()

WIDTH, HEIGHT = 1080, 720
BG_COLOR = (0, 0, 0)  # default for project was (0, 150, 150)
BG = pygame.Surface((WIDTH, HEIGHT))
BG.fill(BG_COLOR)  # set screen with background color
FPS = 30
MOUSE_LINE_COLOR = (0, 0, 255)
MAX_SPEED, MIN_SPEED = 4, 0  # maximum and minimum speed that a dot can reach
CONNECTING_DISTANCE = 300
DOT_CLUSTER_DISTANCE = 120
DOT_NUMBER = 200  # dot number in the normal execution (static)
MAX_DOT_NUMBER = DOT_NUMBER * 1.5  # max number of dots that can exist
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dots challenge")


class Dot:
    def __init__(self, position=None):
        self.position = (r.randint(0, WIDTH), r.randint(0, HEIGHT)) if position is None else position
        self.speed = (r.randint(MIN_SPEED, MAX_SPEED), r.randint(MIN_SPEED, MAX_SPEED))
        self.size = 2
        self.movement_probability = [0.95, 0.95, 0.95]  # change in module probability|x axis change p.| y ax. change p.
        self.color = (255, 255, 0)  # (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)) -> random color dots
        self.rect = ()
        self.update_rect()

    def update_rect(self):
        self.rect = (self.position[0], self.position[1], self.size, self.size)

    def update_speed(self):
        if r.random() > self.movement_probability[0]:  # change the module
            self.speed = ((self.speed[0] + r.random() * r.choice([1, -1])) % MAX_SPEED,
                          (self.speed[1] + r.random() * r.choice([1, -1])) % MAX_SPEED)
        if r.random() > self.movement_probability[1]:  # change the x axis direction
            self.speed = (self.speed[0] * -1, self.speed[1])
        if r.random() > self.movement_probability[2]:  # change the y axis direction
            self.speed = (self.speed[0], self.speed[1] * -1)

    def update(self):
        self.position = ((self.position[0] + self.speed[0]) % WIDTH, (self.position[1] + self.speed[1]) % HEIGHT)
        self.update_rect()
        self.update_speed()

    def vector_distance(self, p2):
        return abs(self.position[0] - p2[0]) + abs(self.position[1] - p2[1])

    def draw(self, screen_in):
        pygame.draw.rect(screen_in, self.color, self.rect, self.size)
        self.update()


def refresh(screen_in, dots, mouse_motion):
    screen_in.blit(BG, (0, 0))
    draw_straight_lines(screen, dots, mouse_motion)
    [dot.draw(screen_in) for dot in dots]
    pygame.display.update()


def draw_straight_lines(screen_in, dots, mouse_motion):  # draws the lines between objects (dot2dot and dot2cursor)
    mouse_position = pygame.mouse.get_pos() if mouse_motion else (-100, -100, -100)  # "else" just avoids syntax error
    for main_dot_index, dot_main in enumerate(dots):
        for dot_in in dots[main_dot_index+1:]:
            vector = dot_main.vector_distance(dot_in.position)  # distance between two dots
            if vector <= DOT_CLUSTER_DISTANCE:
                # default was (255*vector//DOT_CLUSTER_DISTANCE) if vector > DOT_CLUSTER_DISTANCE*0.6 else 150
                color = 255 - (255 * vector // DOT_CLUSTER_DISTANCE) if vector > DOT_CLUSTER_DISTANCE * 0.6 else 100
                pygame.draw.line(screen_in, (0, color, color), dot_main.position, dot_in.position, 1)
        if mouse_motion and dot_main.vector_distance(mouse_position) <= CONNECTING_DISTANCE:
            pygame.draw.line(screen_in, MOUSE_LINE_COLOR, mouse_position, dot_main.position, 1)


def main():
    dots = [Dot() for _ in range(DOT_NUMBER)]
    mouse_motion = False
    while True:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif len(dots) < MAX_DOT_NUMBER and pygame.mouse.get_pressed(3)[0]:
                dots.append(Dot(pygame.mouse.get_pos()))
            mouse_motion = event.type == pygame.MOUSEMOTION  # True if mouse has moved, False otherwise
        refresh(screen, dots, mouse_motion)


if __name__ == "__main__":
    main()
