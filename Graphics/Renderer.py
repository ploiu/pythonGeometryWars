from abc import ABC


class Renderer(ABC):
    """
    abstract class used to render an object or entity. To render a specific entity, subclass this class and override the render function
    """

    # the type of renderer this is
    def __init__(self, _type=None):
        """
        inits the renderer and declares what class this renderer can render
        :param _type: a class reference
        """
        self.type = _type

    def render(self, obj_to_render):
        pass
