class Sprite:
    def __init__(self, object):
        for key, value in object.items():
            setattr(self, key, value)
    def setX(self, x):
        if type(x) != int:
            return
        self.entity["x"] = x
    def getX(self):
        return self.entity["x"]