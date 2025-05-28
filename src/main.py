import load
import json
from spriteEntry import *

entFile = load.getEnt("test.ent")
objects = [Sprite(obj) for obj in entFile["objects"]]

print(objects[0].getX())
objects[0].setX(10)
print(objects[0].getX())