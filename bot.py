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
    done = False
    count = 0
    while done == False and count <= 100:
        rand = random.randint(1, 3)
        done = True
        for i in list_bot:
            if i.x == rand and i.y <= 100:
                done = False
                break
        if done == True:
            list_bot.append(OneBot(vehicles, x=rand))
        count += 1
    return list_bot

def rand_add_bot(list_bot, vehicles, index_row, last_row):

    if last_row == index_row:
        return list_bot, index_row

    for i in list_bot:
        if i.y / 96 < 1:
            return list_bot, index_row

    if random.randint(0, 2) == 0:
        if len(list_bot) < 10:
            list_bot = add_bot(list_bot, vehicles)
        return list_bot, index_row
    else:
        return list_bot, index_row
