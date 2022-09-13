
from Snejky.gameScreen import GameScreen

class Engine:
    """
    Main class of engine

    takes care of objects updates and drawings
    """

    def __init__(self, screen):
        self.screen = screen
        self.game_screen = GameScreen()

    def set_camera(self, camera):
        self.game_screen.set_camera(camera)

    def run_frame(self):
        self.update()
        self.draw()

    def update(self):
        pass

    def draw(self):
        self.game_screen.draw(self.screen)
