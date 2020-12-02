import pygame

import vehicles as vh
import player as pl
import display as ds
import bot
import time
import Roads


def init_game():
    player = pl.Player(speed=1, life=1, coordinates=(2,window_height - 50 - allVehicles.vehicles[player_index].height), \
                   size=(allVehicles.vehicles[player_index].width, allVehicles.vehicles[player_index].height))
    tmp_bot = bot.OneBot(vehicles=allVehicles.vehicles)
    list_bot = []
    list_bot.append(tmp_bot)
    init_timer = time.time()
    return init_timer, player, list_bot

# Exemple loading a pic.
pygame.init()
button_surface = pygame.image.load('assets/button.png')

# Loading a font.
font_lemonmilk = pygame.font.Font('assets/LEMONMILK-Regular.otf', 20)

icon_surface = pygame.image.load('assets/icon.ico')
pygame.display.set_icon(icon_surface)

# Creating window. window_surface is the surface we're gonna write on.
window_width, window_height = 480, 680
pygame.display.set_caption("Car Project")
window_surface = pygame.display.set_mode((window_width, window_height))

# Load all vehicles
allVehicles = vh.Vehicles()
i = 0
while i < 55:
    if i != 21:
        allVehicles.vehicles[i].image = pygame.transform.rotate(allVehicles.vehicles[i].image, 180)
    i += 1
player_index = 21

# clock is for fps
clock = pygame.time.Clock()

# Allow to hold the same key (arg in ms)
pygame.key.set_repeat(1000, 1)

game_state = "menu"
init_timer, player, list_bot = init_game()
score = init_timer
road = Roads.Roads(window_surface, window_width, window_height)
# First display.
ds.display(game_state, window_surface,window_width,window_height, player, list_bot, font_lemonmilk, allVehicles, init_timer, road)

# Start mainloop.
launched = True
while launched:

    # Collect and use events for user.
    # Collect and use events for user.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.KEYDOWN:
            if game_state == "menu" or game_state == "game_over":
                if event.key == pygame.K_RETURN:
                    init_timer, player, list_bot = init_game()
                    game_state = "in_game"
            elif game_state == "in_game":
                if event.key == pygame.K_LEFT:
                    player.move('Left')
                elif event.key == pygame.K_RIGHT:
                    player.move('Right')

    if game_state == "in_game":
        list_bot = bot.add_bot(list_bot, allVehicles.vehicles)
        if player.check_all_collisions(list_bot) == True:
            if player.hp <= 1:
                score = int((time.time() - init_timer) * 1000)
                game_state = "game_over"
    ds.display(game_state, window_surface, window_width,
               window_height, player, list_bot, font_lemonmilk, allVehicles, init_timer, road, score=score)

    # For fps.
    clock.tick(60)

# Force exit program
pygame.display.quit()
