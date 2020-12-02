class Road :
    def __init__(self):
        self.surfaceSize = 96
        self.roadGreen = pygame.image.load('assets/Roads/redim/Green Grass.png')
        self.roadPass = pygame.image.load('assets/Roads/redim/Road_Pass.png')
        self.roadBorder = pygame.image.load('assets/Roads/redim/Road_No Pass Double.png')





def display_road():
    surfaceSize = 96
    roadGreen = pygame.image.load('assets/Roads/redim/Green Grass.png')
    roadPass = pygame.image.load('assets/Roads/redim/Road_Pass.png')
    roadBorder = pygame.image.load('assets/Roads/redim/Road_No Pass Double.png')

    for col in range(0, window_width, surfaceSize):
        for row in range(0, window_height, surfaceSize):
            window_surface.blit(roadGreen, (col, row))

    for col in range(surfaceSize, window_width - surfaceSize, surfaceSize):
        for row in range(0, window_height, surfaceSize):
            if col == surfaceSize * 1 or col == surfaceSize * 4:
                window_surface.blit(roadBorder, (col, row))
            else:
                window_surface.blit(roadPass, (col, row))