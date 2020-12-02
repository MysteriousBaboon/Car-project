import random

class OneBot(object):
    """docstring for OneBot"""

    def __init__(self, vehicles):
        super(OneBot, self).__init__()
        self.x = random.randint(1, 3)
        self.y = 0
        rand = 21
        while rand == 21:
            rand = random.randint(0, 54)
        self.image = vehicles[rand].image

        self.width = self.image.get_size()[0]
        self.height = self.image.get_size()[1]

