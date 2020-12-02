import random

class OneBot(object):
    """docstring for OneBot"""

    def __init__(self, vehicles, x=-1):
        super(OneBot, self).__init__()
        if x == -1:
            self.x = random.randint(1, 3)
        else:
            self.x = x
        self.y = 0
        rand = 21
        while rand == 21:
            rand = random.randint(0, 54)
        self.image = vehicles[rand].image

        self.width = self.image.get_size()[0]
        self.height = self.image.get_size()[1]

def add_bot(list_bot, vehicles):
    if len(list_bot) < 3:
        done = False
        while done == False:
            rand = random.randint(1, 3)
            done = True
            for i in list_bot:
                if i.x == rand and i.y <= 100:
                    done = False
                    break
            if done == True:
                list_bot.append(OneBot(vehicles, x=rand))
    return list_bot