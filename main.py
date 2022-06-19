import pygame
import numpy
import objects
import solver
import math
import random


global slowdown
width = 2560
height = 1000
FPS = 60
speed = 1


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255,255,0)
cyan = (0,255,255)
purple = (255,0,255)
darkPurple = (128,0,128)
darkYellow = (128,128,0)
darkRed = (128,0,0)
darkGreen = (0,128,0)
darkBlue = (0,0,128)


pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Gravity sim")
clock = pygame.time.Clock()
engine = solver.engine()
myfont = pygame.font.SysFont("monospace", 30)

def createPlanets():
    planets = []
    vel = 400#1335
    mass = 8000#600
    planets.append(objects.planet(numpy.array((1280,0)),mass,10,numpy.array((vel,0)),blue,"planet 1"))
    planets.append(objects.planet(numpy.array((1780,500)),mass,10,numpy.array((0,vel)),green,"planet 2"))
    planets.append(objects.planet(numpy.array((1280,1000)),mass,10,numpy.array((-1*vel,0)),red,"planet 3"))
    planets.append(objects.planet(numpy.array((780,500)),mass,10,numpy.array((0,-1*vel)),cyan,"planet 4"))
    planets.append(objects.planet(numpy.array((1280,500)),15000*mass,100,numpy.array((0,0)),yellow,"Star"))

    return(planets)


def calcMagnitude(x):
    return(math.sqrt(x[0]**2+x[1]**2))

planets = createPlanets()

def createStars():
    colour = (255,255,random.randint(0,255))
    stars = []
    for i in range(1,random.randint(1,100)):
            stars.append([screen, colour,(random.randint(0,width),random.randint(0,height)),random.randint(1,10)])
    return(stars)

stars = createStars()
showLines = 0
showPlanets = 0
showNames = 0
showStars = 0
frameTimes = []

running = True
while running:

    dt = clock.tick(FPS) / 1000
    frameTimes.append(dt)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                speed /=2
            elif event.key == pygame.K_MINUS:
                speed *=2
            elif event.key == pygame.K_r:
                planets = createPlanets()
                stars = createStars()
            elif event.key == pygame.K_l:
                showLines +=1
            elif event.key == pygame.K_p:
                  showPlanets += 1
            elif event.key == pygame.K_n:
                  showNames += 1
            elif event.key == pygame.K_n:
                  showNames += 1
            elif event.key == pygame.K_s:
                showStars +=1
    dt /= speed
    screen.fill(black)
    engine.update(planets,dt)

    if showStars %2 ==0:
        for star in stars:
            pygame.draw.circle(star[0],star[1],star[2],star[3])
        
    if showLines %2 ==0:
        for planet in planets:
            pygame.draw.lines(screen,planet.colour,False,planet.positions)
            
    if showPlanets %2 == 0:
        for planet in planets:
            pygame.draw.circle(screen,planet.colour,planet.pos,planet.radius)
            
    if showNames %2 == 0:
        for planet in planets:
            screen.blit(myfont.render(f"Name:{planet.debugName}, Velocity:{math.floor(calcMagnitude(planet.velocity))}", 1, white),(planet.pos[0],planet.pos[1] + planet.radius + 0.1*planet.radius))
        
    if len(frameTimes) % 100 == 0:
        frameTimes.pop(0)
    
    screen.blit(myfont.render(f"FPS:{math.floor(1/numpy.average(frameTimes))}, Speed: {1/speed}x", 1, white),(10,50))
    
    pygame.display.flip()       
pygame.quit()
