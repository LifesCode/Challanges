import pygame
from random import randint, choice

pygame.init()

WIDTH, HEIGHT = 1000, 600
BG_COLOR = (0, 150, 150)
FPS = 150
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dots challenge")

class Fragment_point:
    def __init__(self, initial_position) -> None:
        self.radium = randint(1,2)
        self.counter = 0
        self.possible_speed = [-2, -1, 1, 2]
        self.speed = (choice(self.possible_speed), choice(self.possible_speed))
        self.colors = [(255, 255, 255), (155, 155, 155)]
        self.in_use_color = choice(self.colors)
        self.position = [initial_position[0],initial_position[1]]
        self.point_distance, self.mouse_distance = randint(10, 100), 200
        self.mouse_pos = pygame.mouse.get_pos()
    
    def get_position(self) -> list:
        return self.position

    def set_fade_color(self) -> None:
        self.in_use_color = self.colors[1]

    def euclidean_distance(self, p1, p2) -> int:
        return (((int(p1[0])-int(p2[0]))**2) + ((int(p1[1]) - int(p2[1]))**2))**0.5

    def mouse_connection(self) -> None:
        if(self.euclidean_distance((self.mouse_pos[0], self.mouse_pos[1]), (self.position[0], self.position[1])) <= self.mouse_distance):
            pygame.draw.line(screen,(0, 255, 0),tuple(self.position),self.mouse_pos, 2)

    def other_point_connections(self, other_point_position: list) -> None:
        for pos in other_point_position:
            if(self.euclidean_distance(pos, (self.position[0], self.position[1])) <= self.point_distance):
                pygame.draw.line(screen,(50, 50, 50),tuple(self.position) , pos, 1) if (self.euclidean_distance(pos, (self.position[0], self.position[1])) > self.point_distance - 20) else\
                  pygame.draw.line(screen,(205, 205, 205),tuple(self.position) , pos, 1)              
    
    def speed_control(self) -> None:
        if(self.counter > 20):
            self.speed = (choice(self.possible_speed), choice(self.possible_speed))
            self.counter = 0
        self.counter += 1

    def draw(self, other_point_pos) -> None:
        self.speed_control()
        self.mouse_pos = pygame.mouse.get_pos()
        self.other_point_connections(other_point_pos)
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]
        pygame.draw.circle(screen, self.in_use_color, tuple(self.position), self.radium)
        # self.mouse_connection()
    
class Animation:
    def __init__(self) -> None:
        self.point_number = 200
        self.fade_distance = 70
        self.conection_distance = 200
        self.point_list = [Fragment_point((randint(20, WIDTH-20), randint(20, HEIGHT-20))) for _ in range(self.point_number)]

    def generate_new_points(self) -> None:
        [self.point_list.append(Fragment_point((randint(20, WIDTH-20), randint(20, HEIGHT-20)))) for _ in range(self.point_number - len(self.point_list))]

    def generate_new_points_by_click(self) -> None:
        self.point_list.append(Fragment_point(pygame.mouse.get_pos()))

    def draw_all_points(self) -> None:
        point_to_delete = [point for point in self.point_list if point.get_position()[0] not in range(0, WIDTH) and \
                point.get_position()[1] not in range(0, HEIGHT)]
        [self.point_list.remove(point) for point in point_to_delete]
        # [point.set_fade_color() for point in self.point_list if point.get_position()["x"] not in range(self.fade_distance, WIDTH-self.fade_distance) and \
        #         point.get_position()["y"] not in range(self.fade_distance, HEIGHT-self.fade_distance) ]
        [point.draw([tuple(point.get_position()) for point in self.point_list]) for point in self.point_list]
        self.generate_new_points()
        if pygame.mouse.get_pressed(3)[0]:
            self.generate_new_points_by_click() 
        [point.mouse_connection() for point in self.point_list]

animation = Animation()
def main():
    while True:
        # CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_KP_ENTER]:
                    exit()
            
        screen.fill((25, 25, 25))
        animation.draw_all_points()
        pygame.display.update()

if __name__ == "__main__":
    main()