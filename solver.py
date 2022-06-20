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
                
                if not obj2.canMove:
                    continue
            
                dist = self.getDist(obj.pos,obj2.pos)
                if dist < 100:
                    continue
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
                        current.pos = numpy.add(current.pos,change*2,casting='unsafe')
                        current.velocity *= rest
                    elif collider.mass < current.mass:
                        collider.pos = numpy.subtract(collider.pos,change*2,casting='unsafe')
                        collider.velocity *= rest
                    else:
                        collider.pos = numpy.subtract(collider.pos,change*2,casting='unsafe')
                        collider.velocity *= rest
                        current.pos = numpy.add(current.pos,change*2,casting='unsafe')
                        current.velocity *= rest
    

    
    def update(self,objects,dt):
        self.applyGravity(objects,dt)
        self.resolveAcceleration(objects,dt)
        self.applyAcceleration(objects,dt)
        self.updatePositions(objects,dt)
        #self.solveCollisions(objects)
        
