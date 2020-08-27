from Engine.vector import Vector
from Engine.camera import Camera
from Engine.vertex import Vertex
from Engine.mesh import Mesh
from Engine.face import Face
from Engine.object3D import Object3D

class Penguin(Object3D):
    def __init__(self, engine, x, y, z, rigidBody=False):
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.yellow = (255,165,0)
        faces = self.faces()
        mesh = Mesh(engine, x, y, z, faces)
    
        
        Object3D.__init__(self, engine, x, y, z, mesh, rigidBody)

    def faces(self):
        return [
            Face(Vector(1,-2,1), Vector(1,-2,-1), Vector(-1,-2,-1), self.black),
            Face(Vector(1,-2,1), Vector(-1,-2,1), Vector(-1,-2,-1), self.black),

            Face(Vector(1,1,1), Vector(1,1,-1), Vector(-1,1,-1), self.black),
            Face(Vector(1,1,1), Vector(-1,1,1), Vector(-1,1,-1), self.black),
            
            Face(Vector(1,-2,1), Vector(1,1,1), Vector(1,-2,-1), self.black),
            Face(Vector(1,1,1), Vector(1,1,-1), Vector(1,-2,-1), self.black),

            Face(Vector(-1,-2,1), Vector(-1,1,1), Vector(-1,-2,-1), self.black),
            Face(Vector(-1,1,1), Vector(-1,1,-1), Vector(-1,-2,-1), self.black),

            Face(Vector(1,-2,-1), Vector(-1,-2,-1), Vector(-1,-1,-1), self.black),
            Face(Vector(1,-2,-1), Vector(-1,-1,-1), Vector(1,-1,-1), self.black),

            Face(Vector(0.5,1,-1), Vector(0.5,-1,-1), Vector(1,1,-1), self.black),
            Face(Vector(1,-1,-1), Vector(0.5,-1,-1), Vector(1,1,-1), self.black),
            
            Face(Vector(-0.5,1,-1), Vector(-0.5,-1,-1), Vector(-1,1,-1), self.black),
            Face(Vector(-1,-1,-1), Vector(-0.5,-1,-1), Vector(-1,1,-1), self.black),

            Face(Vector(-0.5,1,-1), Vector(-0.5,0,-1), Vector(0.5,1,-1), self.black),
            Face(Vector(-0.5,0,-1), Vector(0.5,0,-1), Vector(0.5,1,-1), self.black),

            Face(Vector(-0.25,-0.1,-1.25), Vector(-0.25,-0.1,-1), Vector(-0.25,0.1,-1), self.yellow),
            Face(Vector(-0.25,-0.1,-1.25), Vector(-0.25,0.1,-1), Vector(-0.25,0.1,-1.25), self.yellow),
            
            Face(Vector(0.25,-0.1,-1.25), Vector(0.25,-0.1,-1), Vector(0.25,0.1,-1), self.yellow),
            Face(Vector(0.25,-0.1,-1.25), Vector(0.25,0.1,-1), Vector(0.25,0.1,-1.25), self.yellow),

            Face(Vector(0.25,0.1,-1.25), Vector(0.25,0.1,-1), Vector(-0.25,0.1,-1), self.yellow),
            Face(Vector(0.25,0.1,-1.25), Vector(-0.25,0.1,-1), Vector(-0.25,0.1,-1.25), self.yellow),

            Face(Vector(0.25,0.1,-1.25), Vector(0.25,-0.1,-1.25), Vector(-0.25,0.1,-1.25), self.yellow),
            Face(Vector(-0.25,-0.1,-1.25), Vector(-0.25,0.1,-1.25), Vector(0.25,-0.1,-1.25), self.yellow),

            Face(Vector(0.30,0.15,-1.01), Vector(0.30,0.30,-1.01), Vector(0.45,0.3,-1.01), self.white),
            Face(Vector(0.30,0.15,-1.01), Vector(0.45,0.15,-1.01), Vector(0.45,0.3,-1.01), self.white),

            Face(Vector(-0.30,0.15,-1.01), Vector(-0.30,0.30,-1.01), Vector(-0.45,0.3,-1.01), self.white),
            Face(Vector(-0.30,0.15,-1.01), Vector(-0.45,0.15,-1.01), Vector(-0.45,0.3,-1.01), self.white),
            ]
            
 
    def Update(self):
        pass
    def Draw(self, screen):
        pass
