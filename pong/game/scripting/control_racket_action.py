from constants import *
from game.scripting.action import Action


class ControlRacketAction(Action):

    def __init__(self, keyboard_service,up,down):
        self._keyboard_service = keyboard_service
        self._up = up
        self._down = down
        
    def execute(self, cast, script, callback):
        racket = cast.get_first_actor(RACKET_GROUP)
        if self._keyboard_service.is_key_down(self._up): 
            racket.swing_left()
        elif self._keyboard_service.is_key_down(self._down): 
            racket.swing_right()  
        else: 
            racket.stop_moving()        