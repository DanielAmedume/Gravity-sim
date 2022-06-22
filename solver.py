import math
import numpy
import objects as planetTypes
class engine():
    def __init__(self):
        self.G =1 #6.67x10^-11
        self.density = 5500

    def getDist(self,x,y):
       return(math.sqrt((abs(x[0] - y[0])**2 + abs(x[1] - y[1])**2)))

    def applyGravity(self,objects,dt):
        for obj in objects:
            for obj2 in objects:

                if obj == obj2:
                    continue
                
                if not obj2.canMove:
                    continue
            
                dist = self.getDist(obj.pos,obj2.pos)

                if dist <= (obj.radius + obj2.radius) * 0.3:
                    continue

                vector = obj.pos - obj2.pos
                force = self.G * ((obj.mass * obj2.mass) / (dist*dist))
                norm = vector / dist
                obj2.applyForce(force*norm)
                #dampen the force to prevent infinities
                obj2.applyForce(force*norm*-0.1)


    def resolveAcceleration(self,objects,dt):
        for obj in objects:
            obj.accelerate(dt)

    def applyAcceleration(self,objects,dt):
        for obj in objects:
            obj.applyAcceleration(dt)

    def updatePositions(self,objects,dt):
        for obj in objects:
            obj.updatePos(dt)

            
    def solveCollisions(self,objects):
        rest = -0.8
        for current in objects:
            for collider in objects:
                
                if current == collider:
                    break

                collisionVector = current.pos - collider.pos
                dist = self.getDist(current.pos, collider.pos)

                if dist < 1:
                    norm = collisionVector / dist
                    delta = (current.radius + collider.radius) - dist
                    change = 0.5 * delta * norm
                    if collider.mass > current.mass:
                        current.pos = numpy.add(current.pos,change*2)
                        current.velocity *= rest
                    elif collider.mass < current.mass:
                        collider.pos = numpy.subtract(collider.pos,change*2)
                        collider.velocity *= rest
                    else:
                        collider.pos = numpy.subtract(collider.pos,change*2)
                        collider.velocity *= rest
                        current.pos = numpy.add(current.pos,change*2)
                        current.velocity *= rest
    
    def merge(self,objects):
        for obj in objects:
            for obj2 in objects:
                
                if obj == obj2:
                    continue
                
                if self.getDist(obj.pos,obj2.pos) < (obj.radius + obj2.radius):
                    mass = obj.mass + obj2.mass
                    radius = (((mass / self.density) / (4/3 * 3.14)) ** (1/3)) * 2
                    totalMass = obj.mass + obj2.mass
                    vel = (((obj.velocity * obj.mass) / totalMass) + ((obj2.velocity * obj2.mass) / totalMass))
                    colour = (((obj.colour[0]+obj2.colour[0])/2),(((obj.colour[1]+obj2.colour[1])/2)),(((obj.colour[2]+obj2.colour[2])/2)))
                    obj.mass = mass
                    obj.radius = radius
                    obj.velocity = vel
                    obj.colour = colour
                    obj.debugName = f"{obj.debugName}+{obj2.debugName}"
                    #objects.append(planetTypes.planet(obj.pos,mass,radius,vel,colour,f"{obj.debugName}+{obj2.debugName}"))

                    objects.remove(obj2)

        return(objects)
    
    def update(self,objects,dt):
        #objects = self.merge(objects)
        self.applyGravity(objects,dt)
        self.resolveAcceleration(objects,dt)
        self.applyAcceleration(objects,dt)
        self.updatePositions(objects,dt)
        #self.solveCollisions(objects)
        return(objects)
        
