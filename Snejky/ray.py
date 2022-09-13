
class Ray:
    """
    This class is light ray that draws one pixel
    
    `position` is tuple of x a y(z) coordinates of screen 
    """

    def __init__(self, screen: object, 
        camera: object, 
        position: tuple, 
        game_objects: list,
        lights: list):

        self.screen = screen
        self.camera = camera
        self.position = position
        self.game_objects = game_objects
        self.lights = lights

    def run(self):
        self.param = {
            "A": self.camera.position,
            "u": 
        }
        for obj in self.game_objects:
            pass

    def get_direction(self):
        direct = (self.position[0], self.camera.far, self.position[1])

    def collision(self, obj):
        pass