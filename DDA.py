# DIGITAL DIFFERENTIIAL ANALYZER(DDA) ALGORITHM
import pygame
import sys

pygame.init()
screen=pygame.display.set_mode((700,600))
pygame.display.set_caption("DDA algorithm")

# FUNCTION TO DRAW LINE USING DDA ALGORITHM

def dda(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    x_inc = dx / steps
    y_inc = dy / steps

    x = x1
    y = y1

    for i in range(steps):

        x += x_inc
        y += y_inc
        
        screen.set_at((round(x),round(y)),"black")






# MAIN LOOP
def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        screen.fill("white")       
        
        dda(10,10,50,50)
        
        pygame.display.flip()
        
if __name__=="__main__":
    main()
        