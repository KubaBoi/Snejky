from Engine.vector import Vector
from Engine.camera import Camera
from Engine.vertex import Vertex
from Engine.mesh import Mesh
from Engine.face import Face
from Engine.object3D import Object3D

class Plain(Object3D):
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
        fcs = []
        for x in range(0, 10):
            for z in range(0, 10):
                if (z % 2 == 0):
                    
                
        return fcs 
 
    def Update(self):
        Object3D.Update(self)
        
    def Draw(self, screen):
        pass
