
import pygame
from random import randint

pygame.init()

WIDTH, HEIGHT = 700, 500
#WIDTH, HEIGHT = 1280, 720
BG_COLOR = (0, 150, 150,255)
DOT_COLOR=(230,230,230)
FPS = 60
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dots challenge")



class Dot():
    def __init__(self,surfece,position,vel) -> None:
        super().__init__()


        self.pos=position
        self.vel=vel
        self.screen=surfece
        self.ray=5
        self.diretion=pygame.Vector2(self.diretion_generate())
        self.near_dots=[]
        self.field=80
        
    def draw_dot(self,color)->None:
        pygame.draw.circle(screen,color,self.pos,self.ray)

    def draw_lines(self,color)->None:
        for dot in self.near_dots:
            pygame.draw.line(screen,color,(self.pos),dot.pos,1)

    def color_generation(self,near_dots)->tuple:
        num_near_dots=len(near_dots)
        if num_near_dots>5:
            num_near_dots=5
        colors=[(46,166,166),(92,182,182),(138,198,198),(184,214,241),(230,230,230)]

        return colors[num_near_dots-1]
       

    def diretion_generate(self)->tuple:
        x:int
        y:int
        x=0
        y=0
        while(x==0):
            x=randint(-2,2)
        while(y==0):
            y=randint(-2,2)

        x=x/self.vel
        y=y/self.vel
        return (x,y)

    def get_near_dot(self,dot_list):

        for dot in dot_list:
            if (dot.pos[0]>=self.pos[0]-self.field)and (dot.pos[0]<=self.pos[0]+self.field):
              if((dot.pos[1]>=self.pos[1]-self.field)and (dot.pos[1]<=self.pos[1]+self.field)):
                 self.near_dots.append(dot)

    def out_of_screen(self,WIDTH, HEIGHT):
        if self.pos[0]>WIDTH or self.pos[0]<0:
            return True
        if self.pos[1]>HEIGHT or self.pos[1]<0:
            return True
        
    def update(self):
        self.pos=self.pos+self.diretion
        color=self.color_generation(self.near_dots)
        self.draw_dot(color)
        self.draw_lines(color)
        self.near_dots.clear()
        



def generat_dot(dot_list):
    dot=Dot(screen,(randint(0,WIDTH),randint(0,HEIGHT)),randint(1,3))
    dot_list.append(dot)

    return dot_list

def mouse_lines(dot_list):
    mouse_pos=pygame.mouse.get_pos()
    near_dots=[]
    field=200
    for dot in dot_list:
            if (dot.pos[0]>=mouse_pos[0]-field)and (dot.pos[0]<=mouse_pos[0]+field):
              if((dot.pos[1]>=mouse_pos[1]-field)and (dot.pos[1]<=mouse_pos[1]+field)):
                 near_dots.append(dot)
            
    if mouse_pos[0]==0 or mouse_pos[1]==0:
        near_dots.clear()
    for dot in near_dots:
         pygame.draw.line(screen,(DOT_COLOR),(mouse_pos),dot.pos,1)
    near_dots.clear()



def main():
    dot_list=[]
    
    for i in range(50):
        dot_list=generat_dot(dot_list)
    while True:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            
        screen.fill(BG_COLOR)
        mouse_lines(dot_list)
        for dot in dot_list:
            dot.update()
            dot.get_near_dot(dot_list)
            if dot.out_of_screen(WIDTH, HEIGHT):
                dot_list.remove(dot)
                generat_dot(dot_list)
        
       
              
            
        pygame.display.update()


if __name__ == "__main__":
    main()