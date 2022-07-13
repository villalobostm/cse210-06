from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Button(Actor):
    """A button that can be clicked."""
    
    def __init__(self, body, image, debug = False):
        """Constructs a new Button.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image

    def get_body(self):
        """Gets the button's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the button's image.
        
        Returns:
            An instance of Image.
        """
        return self._image
