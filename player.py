import pygame
class Player:
    def __init__(self, speed=1, life=1, coordinates=(0, 0), size=(0, 0)):
        self.hp = life
        self.speed = speed

        self.x = coordinates[0]
        self.y = coordinates[1]

        self.width = size[0]
        self.height = size[1]

    def move(self, key):
        if key == "up":
            self.y -= self.speed
        elif key == "down":
            self.y += self.speed
        elif key == "right":
            self.x += self.speed
        elif key == "left":
            self.x -= self.speed

    def check_all_collisions(self,gameobject_list):
        player_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        for vehicle in gameobject_list:
            vehicle_rect = pygame.Rect(vehicle.x, vehicle.y, vehicle.width, vehicle.height)
            if player_rect.colliderect(vehicle_rect):
                print("CA MARCHE")


    def check_collision_border(self, side):
        if side == "Left":
            if self.x < 10:
                return False
            else:
                return True
        elif side == "Right":
            pass
        elif side == "Bottom":
            pass
        elif side == "Top":
            pass