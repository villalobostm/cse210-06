from constants import *
from game.scripting.action import Action
from game.casting.point import Point
"This class is responsable of tracking click on the menu"
class ChangeSceneClickAction(Action):

    def __init__(self, mouse_service, button, next_scene): 
        self._mouse_service = mouse_service
        self._button = button
        self._next_scene = next_scene
        
    def execute(self, cast, script, callback):
        # Si se hace click sobre el boton, hacer 'callback.on_next(self._next_scene)'
        cursor = self._mouse_service.get_coordinates()
        button = cast.get_first_actor(self._button)
        body = button.get_body()
        
        if cursor.is_aprox(body.get_position(), body.get_size()):
            if self._mouse_service.is_button_down("left"):
                callback.on_next(self._next_scene)