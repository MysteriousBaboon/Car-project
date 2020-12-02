import pygame


class Roads:

    def __init__(self, window_width, window_height):
        self.surfaceSize = 96
        self.window_width = window_width
        self.window_height = window_height
        self.roadGreen = pygame.image.load('assets/Roads/Green.jpg')
        self.roadPass = pygame.image.load('assets/Roads/RoadPass.jpg')
        self.roadBorder = pygame.image.load('assets/Roads/RoadNoPass.jpg')



    def display(self, speed):

        for col in range(0, self.window_width, self.surfaceSize):
            for row in range(0, self.window_height, self.surfaceSize):
                self.window_surface.blit(self.roadGreen, (col, row))

        for col in range(self.surfaceSize, self.window_width - self.surfaceSize, self.surfaceSize):
            for row in range(0, window_height, self.surfaceSize):
                if col == self.surfaceSize * 1 or col == self.surfaceSize * 4:
                    self.window_height.blit(roadBorder, (col, row))
                else:
                    window_surface.blit(roadPass, (col, row))


roads = Roads(800, 600)