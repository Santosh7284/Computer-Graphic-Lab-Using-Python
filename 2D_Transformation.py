
# Two dimension transformation

import pygame
import sys
import math

pygame.init()

width,height=1000,600
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Two dimensional tranformation")

def translation(x1,y1,x2,y2,tx,ty):
    pygame.draw.line(screen,"black",(x1,y1),(x2,y2),3)
    pygame.draw.line(screen,"red",(x1+tx,y1+ty),(x2+tx,y2+ty),3)
    
def scaling(x1,y1,x2,y2,sx,sy):
    pygame.draw.line(screen,"violet",(x1,y1),(x2,y2),3)
    pygame.draw.line(screen,"blue",(x1,y1),(x2*sx,y2*sy),3)
    
def rotation(x1,y1,x2,y2,ang):
    sinang=math.sin(ang)
    cosang=math.cos(ang)
    pygame.draw.line(screen,"green",(x1,y1),(x2,y2),3)
    pygame.draw.line(screen,"orange",(x1,y1),(x2*cosang-y2*sinang,x2*cosang+y2*sinang),3)
    
def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        screen.fill("white")
        translation(200,200,300,300,50,100)
        scaling(350,350,450,450,2,1)
        rotation(100,100,50,50,0.51)
        
        pygame.display.flip()
        
if __name__=="__main__":
    main()
        