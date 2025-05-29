from .load import *
import json
from .spriteEntry import *
import pygame

def playentry(path):
    entFile = getEnt(path)
    objects = {obj["id"]: Sprite(obj) for obj in entFile["objects"]}

    print(objects["7y0y"].getSize())
    objects["7y0y"].setXSize(objects["7y0y"].getSize() + 10)
    print(objects["7y0y"].getSize())

if __name__ == "__main__":
    playentry("test.ent")