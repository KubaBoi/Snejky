
import threading

from Snejky.ray import Ray

class GameScreen:
    """
    Class where are all gameobjects
    """

    def __init__(self):
        self.game_objects = []
        self.lights = []
        self.camera = None

    def update(self):
        self.camera.update()

        for obj in self.game_objects:
            obj.update()

    def draw(self, screen):
        threads = []

        for x in range(0, screen.get_width()):
            for y in range(0, screen.get_height()):
                ray = Ray(screen, self.camera, (x,y), self.game_objects, self.lights)

                th = threading.Thread(target=ray.run)
                threads.append(th)
                th.start()

        for th in threads:
            th.join()

    def get_objects(self):
        return self.game_objects

    def add_object(self, obj):
        self.game_objects.append(obj)

    def remove_object(self, obj):
        self.game_objects.remove(obj)

    def set_camera(self, camera):
        self.camera = camera

    