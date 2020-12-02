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
        if key == "Left":
            if self.x > 1:
                self.x -= 1
        if key == "Right":
            if self.x < 3:
                self.x += 1

    def check_all_collisions(self, list_bot):
        player_rect = pygame.Rect(self.x, self.y, 1, self.height)
        #print("player_rect = ", player_rect)
        if len(list_bot) == 0:
            return False
        for vehicle in list_bot:
            vehicle_rect = pygame.Rect(vehicle.x, vehicle.y, 1, vehicle.height)
            #print("vehicule_rect = ", vehicle_rect)
            if player_rect.colliderect(vehicle_rect):
                self.hp -= 1
                return True
        return False

