from Engine.vector import Vector
from Engine.camera import Camera
from Engine.vertex import Vertex
from Engine.mesh import Mesh
from Engine.face import Face
from Engine.object3D import Object3D

class Cube(Object3D):
    def __init__(self, engine, x, y, z, scale, color=None, rigidBody=False):
        self.scale = scale
        self.color = color
        faces = self.faces(scale, color)
        mesh = Mesh(engine, self, x, y, z, faces)
    
        
        Object3D.__init__(self, engine, x, y, z, mesh, rigidBody)

    def faces(self, scale, color):
        return [
            Face([Vector(scale,scale,scale), Vector(scale,-scale,scale), Vector(-scale,-scale,scale)], color), #1
            Face([Vector(scale,scale,scale), Vector(-scale,scale,scale), Vector(-scale,-scale,scale)], color), #2
            Face([Vector(-scale,-scale,scale), Vector(-scale,scale,scale), Vector(-scale,scale,-scale)], color), #3
            Face([Vector(-scale,-scale,-scale), Vector(-scale,-scale,scale), Vector(-scale,scale,-scale)], color), #4
            Face([Vector(-scale,scale,-scale), Vector(scale,scale,-scale), Vector(-scale,-scale,-scale)], color), #5
            Face([Vector(-scale,-scale,-scale), Vector(scale,scale,-scale), Vector(scale,-scale,-scale)], color), #6
            Face([Vector(scale,-scale,scale), Vector(scale,scale,-scale), Vector(scale,-scale,-scale)], color), #7
            Face([Vector(scale,-scale,scale), Vector(scale,scale,-scale), Vector(scale,scale,scale)], color), #8
            Face([Vector(-scale,scale,-scale), Vector(scale,scale,-scale), Vector(scale,scale,scale)], color), #9
            Face([Vector(-scale,scale,-scale), Vector(-scale,scale,scale), Vector(scale,scale,scale)], color), #10
            Face([Vector(-scale,-scale,-scale), Vector(scale,-scale,-scale), Vector(scale,-scale,scale)], color), #11
            Face([Vector(-scale,-scale,-scale), Vector(-scale,-scale,scale), Vector(scale,-scale,scale)], color)] #12
 
    def Update(self):
        Object3D.Update(self)
        
    def Draw(self, screen):
        Object3D.Draw(self, screen)
    
