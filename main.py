import time

import pygame

import vehicles as vh
import player as pl
import display as ds
import bot
import Roads

# Init the framework Pygame
pygame.init()


#  Initialize a Player instance, create an enemy bot
def init_game():
    instance = pl.Player(speedX=4, speedY=1, life=1,
                         coordinates=(2, window.height - 50 - allVehicles.getVehicle(player_index).height),
                         size=(allVehicles.getVehicle(player_index).width, allVehicles.getVehicle(player_index).height))
    tmp_bot = bot.OneBot(allVehicles)
    list_bot = [tmp_bot]
    init_timer = time.time()
    index_row = 0
    last_row = -1
    return init_timer, instance, list_bot, index_row, last_row


# Example loading a pic, an icon.
button_surface = pygame.image.load('assets/button.png')
icon_surface = pygame.image.load('assets/icon.ico')

# Attribute the precedently loaded icon as our game icon and the name of the window as Car Project
pygame.display.set_icon(icon_surface)
pygame.display.set_caption("Car Project")


# Creating an object Window that will store our data necessary
window = ds.Window(width=6*96, height=7*96, font=pygame.font.Font('assets/LEMONMILK-Regular.otf', 20))

# Load all vehicles
allVehicles = vh.Vehicles()
player_index = 21

# clock is for fps
clock = pygame.time.Clock()

# Init of all game related variables
game_state = "menu"
init_timer, player, list_bot, index_row, last_row = init_game()
score = init_timer
road = Roads.Roads(window.surface, window.width, window.height)

# First display.
window.display(game_state, player, list_bot, allVehicles, init_timer, road)

# Start mainloop.
launched = True

# To avoid key retention
lockKey = False
countLock = 10
while launched:
    # Collect and use events for user.
    if lockKey:
        countLock -= 1
        if countLock <= 0 :
            lockKey = False
            countLock = 10
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.KEYDOWN:  # If a key is down
            if game_state == "in_game":
                if event.key == pygame.K_LEFT:  # If the key down is the left arrow
                    if not lockKey: # To avoid key retention
                        player.move('Left')
                        lockKey = True
                elif event.key == pygame.K_RIGHT:  # If the key down is the right arrow
                    if not lockKey: # To avoid key retention
                        player.move('Right')
                        lockKey = True
            elif game_state == "menu" or game_state == "game_over":
                if event.key == pygame.K_RETURN:
                    init_timer, player, list_bot, index_row, last_row = init_game()
                    game_state = "in_game"

    if game_state == "in_game":
        index_row += 4
        list_bot, last_row = bot.rand_add_bot(list_bot, allVehicles, int(index_row / 96), last_row)
        if player.check_all_collisions(list_bot):
            if player.hp <= 1:
                score = int((time.time() - init_timer) * 50)
                game_state = "game_over"

    window.display(game_state, player, list_bot, allVehicles, init_timer, road, score=score)

    # For fps.
    clock.tick(60)

# Force exit program
pygame.display.quit()
