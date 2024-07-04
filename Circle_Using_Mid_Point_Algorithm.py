# CIRCLE USING MID POINT ALGORITHM
import pygame
import sys

pygame.init()

screen=pygame.display.set_mode((700, 600))
pygame.display.set_caption("Midpoint circle  Algorithm")




# FUNCTION TO DRAW CIRCLE USING MID POINT ALGORITHM
def draw_circle_points(xc, yc, r):
    x=0
    y=r
    p=1-r
    while(x<=y):
            screen.set_at((xc + x, yc + y), "black")
            screen.set_at((xc - x, yc + y), "Blue")
            screen.set_at((xc + x, yc - y), "Green")
            screen.set_at((xc - x, yc - y), "Yellow")
            screen.set_at((xc + y, yc + x), "Red")
            screen.set_at((xc - y, yc + x), "Orange")
            screen.set_at((xc + y, yc - x), "Pink")
            screen.set_at((xc - y, yc - x), "Brown")
            x=x+1
            
            if(p<0):
                 p=p+2*x+1
            
       
            else:
                y=y-1
                p=p+2*x-2*y+1
    

# MAIN LOOP
def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        screen.fill("white")
        draw_circle_points(100,100,50)
        
        pygame.display.flip()

if __name__== "__main__":
    main()

   