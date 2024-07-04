# Bresenham's Line Algorithm
import pygame
import sys

pygame.init()
screen=pygame.display.set_mode((700,700))
pygame.display.set_caption("BLA drawing line algorithm")

# FUNCTION TO DRAW A LINE USING BLA 
def draw_line_bla(x1,y1,x2,y2):
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    if x2>x1:
      lx=1 
    else:
        lx=-1
       
    
    if y2>y1:
        ly=1 
    else:
        ly=-1
        
    x=x1
    y=y1
    
    if dx>dy:
        p=2*dy-dx
        while x!=x2:
            if p<0:
                x=x+lx
                y=y
                p=p+2*dy
            else:
                x=x+lx
                y=y+lx
                p=p+2*dy-2*dx
            screen.set_at((round(x),round(y)),"black")
    else:
        p=2*dx-dy
        while y!=y2:
            if p<0:
                x=x
                y=y+ly
                p=p+2*dx
            else:
                x=x+lx
                y=y+ly
                p=p+2*dx-2*dy
            screen.set_at((round(x),round(y)),"black")
            
 # MAIN LOOP 
def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill("white") 
        
        draw_line_bla(50,50,10,100)
        
        
        pygame.display.flip()      
            
if __name__=="__main__":
    main()
            