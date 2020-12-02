import pygame


class Vehicle:
    def setName(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        rect = pygame.Rect((self.x, self.y, self.width, self.height))
        self.image = pygame.Surface(rect.size)

    def setLocation(self, xy):
        # print(xy)
        xy = xy.split(",")
        self.x = int(xy[0])
        self.y = int(xy[1])

    def setSize(self, size):
        # print(size)
        hw = size.split(",")
        self.width = int(hw[0])
        self.height = int(hw[1])

    def setImage(self, image):
        self.image = image

    def getImage(self):
        return self.image

    def getRect(self):
        rect = pygame.Rect((self.x, self.y, self.width, self.height))
        return rect

    def __str__(self):
        return f"{self.name} : loc({self.x}, {self.y}), size({self.width}, {self.height})"


class Vehicles:
    def __init__(self):
        """ Constructor. Pass in the file name of the sprite sheet. """
        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load('assets/Cars/cars.png')

        filepath = 'assets/Cars/cars.txt'

        # Using readlines()
        file1 = open(filepath, 'r')
        Lines = file1.readlines()

        self.count = 0
        self.vehicles = []
        newVehicle = Vehicle()
        firstVehicle = True
        # Fetch all vehicles with they params
        for line in Lines:
            self.count += 1
            if line == "":
                # end of file
                # print("Line{}: End")
                # Add new vehicle
                rect = pygame.Rect((newVehicle.x, newVehicle.y, newVehicle.width, newVehicle.height))
                image = pygame.Surface(rect.size)
                image.blit(self.sprite_sheet, (0, 0), rect)
                newVehicle.setImage(image)
                self.vehicles.append(newVehicle)

            elif not line.find(" ") >= 0:
                # New vehicule
                line = line.replace(" ", "")
                # print("Line{}: Name = {}".format(count, line.strip()))
                if not firstVehicle:
                    # Add new vehicle
                    rect = pygame.Rect((newVehicle.x, newVehicle.y, newVehicle.width, newVehicle.height))
                    image = pygame.Surface(rect.size)
                    image.blit(self.sprite_sheet, (0, 0), rect)
                    newVehicle.setImage(image)
                    self.vehicles.append(newVehicle)
                # Save the last vehicle
                newVehicle = Vehicle()
                newVehicle.setName(line)
                firstVehicle = False

            else:
                # Param of vehicle
                line = line.replace(" ", "")
                # print("Line{}: Param = {}".format(count, line.strip()))
                if line.find("xy:") >= 0:
                    newVehicle.setLocation(line.split(":")[1])
                elif line.find("size:") >= 0:
                    newVehicle.setSize(line.split(":")[1])

    def getImage(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """
        # Create a new blank image
        image = pygame.Surface([width, height])
        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        # Return the image
        return image

    def getCountVehicule(self):
        return self.count

    def getListVehicules(self):
        return self.vehicles


def check_all_collisions(player, gameobject_list):
    player_rect = pygame.Rect(player.x, player.y, player.width, player.height)

    for vehicle in gameobject_list:
        vehicle_rect = pygame.Rect(vehicle.x, vehicle.y, vehicle.width, vehicle.height)
        if player_rect.colliderect(vehicle_rect):
            print("CA MARCHE")


def check_collision_border(side, player):
    if side == "Left":
        if player.x < 10:
            return False
        else:
            return True
    elif side == "Right":
        pass
    elif side == "Bottom":
        pass
    elif side == "Top":
        pass