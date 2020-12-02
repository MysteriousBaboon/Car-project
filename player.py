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
            self.y -= 10
        elif key == "down":
            self.y += 10
        elif key == "right":
            self.x += 10
        elif key == "left":
            self.y -= 10
