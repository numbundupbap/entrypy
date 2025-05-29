class Sprite:
    def __init__(self, object, clone= False):
        for key, value in object.items():
            setattr(self, key, value)
        self.flip = False
        self.is_clone = clone
        self.scaleOriginX = int(self.entity["scaleX"])
        self.scaleOriginY = int(self.entity["scaleY"]) 
            
    # X, Y
    def setX(self, x):
        if type(x) != int:
            return
        self.entity["x"] = x
        
    def getX(self):
        return self.entity["x"]
    
    def setY(self, y):
        if type(y) != int:
            return
        self.entity["y"] = y
        
    def getY(self):
        return self.entity["y"]
    
    # Direction, Rotation
    def setRotation(self, rotation=0):
        if self.getRotateMethod() != "free":
            rotation = 0
        self.entity["rotation"] = rotation % 360
    
    def getRotation(self):
        return self.entity["rotation"]
    
    def setDirection(self, direction=0, flippable=None):
        direction = direction % 360

        if self.getRotateMethod() == 'vertical' and not flippable:
            previousIsRight = 0 <= self.direction < 180
            afterIsRight = 0 <= direction < 180
            if previousIsRight != afterIsRight:
                self.flip = not self.flip

        self.entity["direction"] = direction
    
    def getDirection(self):
        return self.entity["direction"]
    
    # Scale
    def setScaleX(self, scaleX):
        self.entity["scaleX"] = scaleX

    def getScaleX(self):
        return self.entity["scaleX"]

    def setScaleY(self, scaleY):
        self.entity["scaleY"] = scaleY

    def getScaleY(self):
        return self.entity["scaleY"]
    
    # Size
    def setSize(self, size):
        scale = max(1, size) / self.getSize()
        self.setScaleX(self.getScaleX() * scale)
        self.setScaleY(self.getScaleY() * scale)

    def resetSize(self):
        self.setScaleX(self.scaleOriginX)
        self.setScaleY(self.scaleOriginY)

    def setXSize(self, size):
        scale = max(1, size) / self.getSize()
        self.setScaleX(self.getScaleX() * scale)

    def setYSize(self, size):
        scale = max(1, size) / self.getSize()
        self.setScaleY(self.getScaleY() * scale)

    def getSize(self):
        value = (
            self.getWidth() * abs(self.getScaleX()) +
            self.getHeight() * abs(self.getScaleY())
        ) / 2
        return value
    
    # Height, Width
    def setWidth(self, width):
        self.entity["width"] = width

    def getWidth(self):
        return self.entity["width"]

    def setHeight(self, height):
        self.entity["height"] = height

    def getHeight(self):
        return self.entity["height"]

    # Rotate Method
    def getRotateMethod(self):
        return self.rotateMethod
    
    # Render
    def render(self):
        pass