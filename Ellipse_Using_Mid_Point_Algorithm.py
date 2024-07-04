
# ELLIPSE USING MID POINT ALGORITHM
import pygame
import sys
#initialize pygame
pygame.init()
#setup the display
WIDTH, HEIGHT=1200,800
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midpoint circle  Algorithm")
#colors
WHITE=(123, 231, 111)
BLACK=(10,20,30)

def draw_ellipse_region1(xc,yc,x,y):
     screen.set_at((x + xc, y + yc),WHITE)
     screen.set_at((-x + xc, y + yc),WHITE)
     screen.set_at((x + xc, -y + yc),WHITE)
     screen.set_at((-x + xc, -y + yc),WHITE)

def draw_ellipse_region2(xc,yc,x,y):
     screen.set_at((x + xc, y + yc),WHITE)
     screen.set_at((-x + xc, y + yc),WHITE)
     screen.set_at((x + xc, -y + yc),WHITE)
     screen.set_at((-x + xc, -y + yc),WHITE)

def draw_ellipse(rx, ry, xc, yc):
    x = 0
    y = ry
   
    # Initial decision parameter of region 1
    p1 = (ry**2) - (rx**2 * ry) + (0.25 * rx**2)
    while (2 * ry**2 * x) <= (2 * rx**2 * y):
        draw_ellipse_region1(xc,yc,x,y)
        if p1 < 0:
            x += 1
            p1 = p1 + (2 * ry**2 * x) + (ry**2)
        else:
            x += 1
            y -= 1
            p1 = p1 + (2 * ry**2 * x) - (2 * rx**2 * y) + (ry**2)

    # Decision parameter of region 2
    p2 = ((ry**2) * ((x + 0.5)**2)) + ((rx**2) * ((y - 1)**2)) - (rx**2 * ry**2)
    while y != 0:
        draw_ellipse_region2(xc,yc,x,y)

        if p2 > 0:
            y -= 1
            p2 = p2 - (2 * rx**2 * y) + (rx**2)
        else:
            y -= 1
            x += 1
            p2 = p2 + (2 * ry**2 * x) - (2 * rx**2 * y) + (rx**2)

def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        #clear the screen
        screen.fill(BLACK)
        # pygame.draw.circle(screen,"orange",(600,400),100)
        # pygame.draw.circle(screen,"red",(300,400),39)
        # pygame.draw.circle(screen,"skyblue",(930,355),50)
        # pygame.draw.circle(screen,"brown",(1090,400),60)
        # pygame.draw.circle(screen,"blue",(700,525),50)
        # #draw ellipse  using Midpont ellipse algorithm
        # draw_ellipse(300,50, 600,400)
        # draw_ellipse(400,80, 600,400)
        # draw_ellipse(500,100, 600,400)
        draw_ellipse(600,120, 600,400)

        
        
        #update the diplay
        pygame.display.flip()

if __name__== "__main__":
    main()