class Component:
    def __init__(self, engine, mesh=None, rigidBody=False):
        self.engine = engine
        self.mesh = mesh
        self.rigidBody = rigidBody

    def Update(self):
        pass

    def Draw(self, screen):
        pass
