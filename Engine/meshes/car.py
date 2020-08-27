from Engine.vector import Vector
from Engine.camera import Camera
from Engine.vertex import Vertex
from Engine.mesh import Mesh
from Engine.face import Face
from Engine.object3D import Object3D

class Car(Object3D):
    def __init__(self, engine, x, y, z, color=None, rigidBody=False):
        self.color = color
        self.black = (0,0,0)
        self.blue = (176,225,230)

        faces = self.faces()
        mesh = Mesh(engine, x, y, z, faces)
    
        
        Object3D.__init__(self, engine, x, y, z, mesh, rigidBody)

    #Face(Vector(), Vector(), Vector(), self.black),
    #Face(Vector(), Vector(), Vector(), self.color),
    def faces(self):
        return [
            Face([Vector(2.5,-1,1.5), Vector(2.5,-1,-1.5), Vector(-2.5,-1,-1.5)], self.black),
            Face([Vector(2.5,-1,1.5), Vector(-2.5,-1,1.5), Vector(-2.5,-1,-1.5)], self.black),
            
            Face([Vector(2.5,-1,1.5), Vector(2.2,0,1.5), Vector(2.5,-1,-1.5)], self.color),
            Face([Vector(2.2,0,1.5), Vector(2.2,0,-1.5), Vector(2.5,-1,-1.5)], self.color),
            Face([Vector(2.2,-1,-1.5), Vector(2.2,0,-1.5), Vector(2.5,-1,-1.5)], self.color),
            Face([Vector(2.2,-1,1.5), Vector(2.2,0,1.5), Vector(2.5,-1,1.5)], self.color),
            
            Face([Vector(2.2,-1,1.5), Vector(-1.5,-1,1.5), Vector(-1.5,0,1.5)], self.color),
            Face([Vector(2.2,-1,-1.5), Vector(-1.5,-1,-1.5), Vector(-1.5,0,-1.5)], self.color),

            Face([Vector(2.2,-1,1.5), Vector(2.2,0,1.5), Vector(-1.5,0,1.5)], self.color),
            Face([Vector(2.2,-1,-1.5), Vector(2.2,0,-1.5), Vector(-1.5,0,-1.5)], self.color),

            Face([Vector(1,0.1,1.5), Vector(1,0.1,-1.5), Vector(2.2,0,-1.5)], self.color),
            Face([Vector(2.2,0,1.5), Vector(1,0.1,1.5), Vector(2.2,0,-1.5)], self.color),

            Face([Vector(1,0.1,1.5), Vector(1,0,1.5), Vector(2.2,0,1.5)], self.color),
            Face([Vector(1,0.1,-1.5), Vector(1,0,-1.5), Vector(2.2,0,-1.5)], self.color),

            Face([Vector(1,0.1,1.5), Vector(1,0,1.5), Vector(-1.5,0,1.5)], self.color),
            Face([Vector(-1.5,0,1.5), Vector(-1.5,0.1,1.5), Vector(1,0.1,1.5)], self.color),

            Face([Vector(1,0.1,-1.5), Vector(1,0,-1.5), Vector(-1.5,0,-1.5)], self.color),
            Face([Vector(-1.5,0,-1.5), Vector(-1.5,0.1,-1.5), Vector(1,0.1,-1.5)], self.color),

            Face([Vector(1,0.1,-1.5), Vector(1,0.1,1.5), Vector(0.5,2,1.5)], self.blue),
            Face([Vector(1,0.1,-1.5), Vector(0.5,2,-1.5), Vector(0.5,2,1.5)], self.blue),

            Face([Vector(-1,2,-1.5), Vector(0.5,2,-1.5), Vector(0.5,2,1.5)], self.color),
            Face([Vector(-1,2,-1.5), Vector(-1,2,1.5), Vector(0.5,2,1.5)], self.color),

            Face([Vector(-1,2,-1.5), Vector(-1.5,0.1,-1.5), Vector(-1,2,1.5)], self.blue),
            Face([Vector(-1.5,0.1,-1.5), Vector(-1.5,0.1,1.5), Vector(-1,2,1.5)], self.blue),

            Face([Vector(-1,2,1.5), Vector(0.5,2,1.5), Vector(1,0.1,1.5)], self.blue),
            Face([Vector(-1,2,1.5), Vector(-1.5,0.1,1.5), Vector(1,0.1,1.5)], self.blue),

            Face([Vector(-1,2,-1.5), Vector(0.5,2,-1.5), Vector(1,0.1,-1.5)], self.blue),
            Face([Vector(-1,2,-1.5), Vector(-1.5,0.1,-1.5), Vector(1,0.1,-1.5)], self.blue),

            Face([Vector(-1.5,0.1,1.5), Vector(-2.5,0,1.5), Vector(-1.5,-1,1.5)], self.color),
            Face([Vector(-2.5,-1,1.5), Vector(-2.5,0,1.5), Vector(-1.5,-1,1.5)], self.color),

            Face([Vector(-1.5,0.1,-1.5), Vector(-2.5,0,-1.5), Vector(-1.5,-1,-1.5)], self.color),
            Face([Vector(-2.5,-1,-1.5), Vector(-2.5,0,-1.5), Vector(-1.5,-1,-1.5)], self.color),

            Face([Vector(-1.5,0.1,-1.5), Vector(-1.5,0.1,1.5), Vector(-2.5,0,-1.5)], self.color),
            Face([Vector(-1.5,0.1,1.5), Vector(-2.5,0,1.5), Vector(-2.5,0,-1.5)], self.color),

            Face([Vector(-2.5,0,1.5), Vector(-2.5,0,-1.5), Vector(-2.5,-1,-1.5)], self.color),
            Face([Vector(-2.5,0,1.5), Vector(-2.5,-1,1.5), Vector(-2.5,-1,-1.5)], self.color),
            ]
 
    def Update(self):
        #self.Position.x += 0.1

        Object3D.Update(self)
        
    def Draw(self, screen):
        pass
