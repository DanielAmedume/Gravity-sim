import numpy
import math
class planet():
    def __init__(self,pos,mass,radius,velocity,colour,name):
        self.pos = pos
        self.mass = mass
        self.radius = radius
        self.velocity = velocity
        self.colour = colour
        self.force = numpy.array((0,0))
        self.acceleration = numpy.array((0,0))
        self.positions = [list(self.pos),list(self.pos)]
        self.debugName = name
        self.canMove = True

    def applyForce(self,force):
        
        self.force = numpy.add(self.force, force, casting="unsafe")

    def accelerate(self,dt):
        acceleration = self.force / self.mass
        
        self.acceleration = numpy.add(self.acceleration,acceleration*dt)
        self.force = numpy.array((0,0))

    def applyAcceleration(self,dt):
        self.velocity = numpy.add(self.velocity,self.acceleration)

    def updatePos(self,dt):
        self.pos = self.pos + (self.velocity*dt)
        self.force = numpy.array((0,0))
        self.acceleration = numpy.array((0,0))
        self.positions.append(list(self.pos))
        
class fixedMass():
    def __init__(self,pos,mass,radius,velocity,colour,name):
        self.pos = pos
        self.mass = mass
        self.radius = radius
        self.velocity = velocity
        self.colour = colour
        self.force = numpy.array((0,0))
        self.acceleration = numpy.array((0,0))
        self.positions = [list(self.pos),list(self.pos)]
        self.debugName = name
        self.canMove = False

    def applyForce(self,force):
        pass
    
    def accelerate(self,dt):
        pass
    
    def applyAcceleration(self,dt):
        pass

    def updatePos(self,dt):
        pass
