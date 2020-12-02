import pygame


class Player:
    def __init__(self, speed=1, life=1, coordinates=(0, 0), size=(0, 0)):
        self.hp = life
        self.speed = speed

        self.x = coordinates[0]
        self.y = coordinates[1]

        self.width = size[0]
        self.height = size[1]

        self.index = 0

    def move(self, key):
        if key == "Left":
            if self.index > 0:
                self.index -= 1
        if key == "Right":
            if self.index < 2:
                self.index += 1

        if self.index == 0:
            self.x = 100
        elif self.index == 1:
            self.x = 200
        elif self.index == 2:
            self.x = 300

    def check_all_collisions(self,gameobject_list):
        player_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        for vehicle in gameobject_list:
            vehicle_rect = pygame.Rect(vehicle.x, vehicle.y, vehicle.width, vehicle.height)
            if player_rect.colliderect(vehicle_rect):
                print("CA MARCHE")

