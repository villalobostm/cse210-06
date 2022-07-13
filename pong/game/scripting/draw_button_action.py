from constants import *
from game.scripting.action import Action


class DrawButtonAction(Action):
    """This class is responsable of draw a button.

        Args:
            video_service: An instance of Video Service.
            button: The button to be draw.
    """
    def __init__(self, video_service, button_group):
        self._video_service = video_service
        self._button = button_group
        
    def execute(self, cast, script, callback):
        button = cast.get_first_actor(self._button)
        body = button.get_body()

        if button.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        image = button.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)