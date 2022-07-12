from constants import *
from game.scripting.action import Action


class ChangeSceneClickAction(Action):

    def __init__(self, mouse_service, button_x, button_y, next_scene):
        self._mouse_service = mouse_service
        self._button_x = button_x
        self._button_y = button_y
        self._next_scene = next_scene
        
    def execute(self, cast, script, callback):
        # Si se hace click sobre el boton, hacer 'callback.on_next(self._next_scene)'
        pass