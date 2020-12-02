import pygame

class Road:
    def setLocation(self, xy):
    # print(xy)
    xy = xy.split(",")
    self.x = int(xy[0])
    self.y = int(xy[1])
