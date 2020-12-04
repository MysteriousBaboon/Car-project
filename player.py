import pygame


# Class player handling all player's related task (like moving, dying) and data (like size, health, size)
class Player:
    def __init__(self, speedX=1, speedY=2, life=1, coordinates=(0, 0), size=(0, 0)):
        self.hp = life
        self.speedX = speedX
        self.speedY = speedY

        self.positionX = coordinates[0]
        self.x = coordinates[0] *85 +100
        self.y = coordinates[1]

        self.offsetX = 0
        self.gotoX = self.x
                
        self.width = size[0]
        self.height = size[1]

    def move(self, key):
        if key == "Left":
            if self.positionX > 1:
                self.positionX -=1
                self.gotoX = self.positionX*85+100 
                self.offsetX = (self.x - self.gotoX)
        if key == "Right":
            if self.positionX < 3:
                self.positionX +=1
                self.gotoX = self.positionX*85+100 
                self.offsetX = -(self.gotoX - self.x)
        
        self.x = self.gotoX + self.offsetX

    def update(self):
        if self.offsetX > 0:
            self.offsetX -= self.speedX #Vitesse de déplacement latérale
            if self.offsetX < 0:
                self.offsetX = 0 #Trop loin, fin du déplacement
        elif self.offsetX < 0:
            self.offsetX += self.speedX #Vitesse de déplacement latérale
            if self.offsetX > 0:
                self.offsetX = 0 #Trop loin, fin du déplacement
            
        self.x = self.gotoX + self.offsetX
        
    def check_all_collisions(self, list_bot):
        if len(list_bot) == 0:
            return False

        player_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        for vehicle in list_bot:
            vehicle_rect = pygame.Rect(vehicle.x, vehicle.y, self.width, vehicle.height)
            if player_rect.colliderect(vehicle_rect):
                self.hp -= 1
                return True
            else:
                False
