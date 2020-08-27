from Engine.vector import Vector
from Engine.camera import Camera
from Engine.vertex import Vertex
from Engine.mesh import Mesh
from Engine.face import Face
from Engine.object3D import Object3D

import math

class Pyramid(Object3D):
    def __init__(self, engine, x, y, z, scale, orientation, color=None, rigidBody=False):
        self.scale = scale
        self.color = color
        faces = self.faces(scale, color, orientation)
        mesh = Mesh(engine, self, x, y, z, faces)
    
        
        Object3D.__init__(self, engine, x, y, z, mesh, rigidBody)

    def faces(self, scale, color, ori):
        tc = math.sqrt(scale*scale - (scale/2)*(scale/2))
        return [
            Face([Vector(scale,ori*scale/2,scale), Vector(scale,ori*scale/2,-scale), Vector(-scale,ori*scale/2,scale)], color),
            Face([Vector(-scale,ori*scale/2,-scale), Vector(scale,ori*scale/2,-scale), Vector(-scale,ori*scale/2,scale)], color),

            Face([Vector(scale,ori*scale/2,scale), Vector(scale,ori*scale/2,-scale), Vector(0,-scale*ori,0)], color),
            Face([Vector(scale,ori*scale/2,-scale), Vector(-scale,ori*scale/2,-scale), Vector(0,-scale*ori,0)], color),
            Face([Vector(-scale,ori*scale/2,scale), Vector(-scale,ori*scale/2,-scale), Vector(0,-scale*ori,0)], color),
            Face([Vector(-scale,ori*scale/2,scale), Vector(scale,ori*scale/2,scale), Vector(0,-scale*ori,0)], color),
            ]
 
    def Update(self):
        Object3D.Update(self)
        
    def Draw(self, screen):
        pass
