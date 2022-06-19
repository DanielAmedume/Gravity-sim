import math
import numpy
class engine():
    def __init__(self):
        self.G =1 #6.67x10^-11

    def getDist(self,x,y):
       return(math.sqrt((abs(x[0] - y[0])**2 + abs(x[1] - y[1])**2)))

    def applyGravity(self,objects,dt):
        for obj in objects:
            for obj2 in objects:
                if obj == obj2:
                    continue
            
                dist = self.getDist(obj.pos,obj2.pos) / 10
                vector = obj2.pos - obj.pos
                force = self.G * ((obj.mass * obj2.mass) / (dist*dist))
                norm = vector / dist
                obj2.applyForce(force*norm*-1)  

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
        for current in objects:
            for collider in objects:
                
                if current == collider:
                    break

                collisionVector = current.pos - collider.pos
                dist = self.getDist(current.pos, collider.pos)
                
                if dist < current.radius + collider.radius:
                    norm = collisionVector / dist
                    delta = (current.radius + collider.radius) - dist
                    change = 0.5 * delta * norm
                    if collider.mass > current.mass:
                        current.pos = numpy.add(current.pos,change*2,casting='unsafe')
                    else:
                        collider.pos = numpy.subtract(collider.pos,change*2,casting='unsafe')

    

    
    def update(self,objects,dt):
        self.applyGravity(objects,dt)
        self.resolveAcceleration(objects,dt)
        self.applyAcceleration(objects,dt)
        self.updatePositions(objects,dt)
        self.solveCollisions(objects)
        
