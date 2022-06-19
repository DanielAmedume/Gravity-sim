import pygame
import numpy
import objects
import solver
import math
import random


global slowdown
width = 1280
height = 1000
FPS = 60
slowdown = 1


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255,255,0)
cyan = (0,255,255)
purple = (255,0,255)


pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Gravity sim")
clock = pygame.time.Clock()
engine = solver.engine()
myfont = pygame.font.SysFont("monospace", 30)

#bg = pygame.image.load('bg.png')
#bg = pygame.transform.scale(bg, (width, height))


def createPlanets():
    planets = []
    planets.append(objects.planet(numpy.array((100,500)),82,30,numpy.array((10,0)),blue,"earth")) #earth
    planets.append(objects.planet(numpy.array((100,400)),1,5,numpy.array((250,0)),green,"moon")) #moon
    planets.append(objects.planet(numpy.array((100,300)),1,5,numpy.array((200,0)),red,"moon2"))
    planets.append(objects.planet(numpy.array((100,200)),1,5,numpy.array((175,0)),cyan,"moon3"))
    planets.append(objects.planet(numpy.array((100,100)),1,5,numpy.array((100,0)),purple,"moon4"))

    return(planets)


planets = createPlanets()

def createStars():
    colours = [(255,255,255),(255,255,random.randint(0,255))]
    stars = []
    for i in range(1,random.randint(1,100)):
            stars.append([screen, random.choice(colours),(random.randint(0,width),random.randint(0,height)),random.randint(1,10)])
    return(stars)

stars = createStars()
showLines = 0
showPlanets = 0


running = True
while running:

    dt = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                slowdown += 1
            elif event.key == pygame.K_MINUS:
                if slowdown != 1:
                    slowdown -= 1
            elif event.key == pygame.K_r:
                planets = createPlanets()
                stars = createStars()

            elif event.key == pygame.K_l:
                showLines +=1

            elif event.key == pygame.K_p:
                  showPlanets += 1

    dt /=slowdown

    #screen.blit(bg,(0,0))
    screen.fill(black)
    
    engine.update(planets,dt)

    for star in stars:
        pygame.draw.circle(star[0],star[1],star[2],star[3])
        
    if showLines %2 ==0:
        for planet in planets:
            pygame.draw.lines(screen,planet.colour,False,planet.positions)
            
    if showPlanets %2 == 0:
        for planet in planets:
            pygame.draw.circle(screen,planet.colour,planet.pos,planet.radius)

        

    screen.blit(myfont.render(f"FPS:{math.floor(1/dt)}, DT:{dt}, slowdown:{slowdown}, speed:{1/slowdown}x", 1, white),(10,50))
    
    pygame.display.flip()       
pygame.quit()
