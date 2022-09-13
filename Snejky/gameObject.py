
import json

from Snejky.vector import Vector

class GameObject:
    """
    This class stores mesh data about object

    x, y, z
    width, depth, height

    `mesh_loaded`:
        loaded data
        relative to model

    `mesh`:
        calculated rotations and translations
        list of scalars 
        `first triangle` are first 3 triples of scalars
        `first vertex` are first 3 scalars
        vertices are inserted anti-clockwise

    `color`:
        list of scalars same as `mesh data`
        but scalars are not positions but colors

    `normals`:
        calculated after load
        every triangle has one normal -> triple of scalars
    """

    def __init__(self, position):
        self.position = position
        self.mesh_loaded = []
        self.mesh = []
        self.color = []
        self.normals = []

    def load_mesh(self, path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.loads(f.read())

        self.mesh_loaded = data["mesh"]
        self.color = data["color"]

        for i in range(0, self.mesh_loaded, 3):
            self.mesh.append(self.position[0] + self.load_mesh[i])
            self.mesh.append(self.position[1] + self.load_mesh[i+1])
            self.mesh.append(self.position[2] + self.load_mesh[i+2])

    def calculateNormals(self):
        for i in range(0, self.mesh, 9):
            vert1 = (self.mesh[i], self.mesh[i+1], self.mesh[i+2])
            vert2 = (self.mesh[i+3], self.mesh[i+4], self.mesh[i+5])
            vert3 = (self.mesh[i+6], self.mesh[i+7], self.mesh[i+8])

            vec1 = Vector.sub(vert3, vert2)
            vec2 = Vector.sub(vert1, vert2)

            norm = Vector.product(vec1, vec2)

            self.normals.append(norm[0])
            self.normals.append(norm[1])
            self.normals.append(norm[2])