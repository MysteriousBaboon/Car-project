import pygame
import vehicles as vh
import player as pl


def display_road():
    pass


def display_scoreboard():
    pygame.draw.rect(window_surface, BROWN, pygame.Rect(0, 0, window_width, 100))
    pygame.draw.rect(window_surface, BLACK, pygame.Rect(0, 0, window_width, 100), 2)
    score_txt = font_lemonmilk.render("Score :", True, BLACK)
    window_surface.blit(score_txt, (100, 50 - score_txt.get_size()[1] / 2))
    score = 10000
    value_txt = font_lemonmilk.render(str(score), True, BLACK)
    window_surface.blit(value_txt, (200, 50 - value_txt.get_size()[1] / 2))


def display(game_state):
    if game_state == "menu":
        window_surface.fill(GREEN)
        cargame_txt = font_lemonmilk.render("CAR GAME", True, BLACK)
        pressenter_txt = font_lemonmilk.render("Press K_BACKSPACE to start.", True, BLACK)

        window_surface.blit(cargame_txt, (window_width / 2 - cargame_txt.get_size()[0] / 2, 100))
        window_surface.blit(pressenter_txt, (window_width / 2 - pressenter_txt.get_size()[0] / 2, 200))

    elif game_state == "in_game":
        # Color entire window with a certain color.
        window_surface.fill(GREEN)

        display_road()
        #display_vehicules()

        # Loading new texts.
        example_txt = font_lemonmilk.render("Example", True, BLACK)
        size_example_txt = font_lemonmilk.render("size of example : " + str(example_txt.get_size()), True, BLACK)
        manuel_txt = font_lemonmilk.render("Use UP DOWN LEFT RIGHT key", True, BLACK)
        # Blit new texts.
        window_surface.blit(example_txt, (100, 175))
        window_surface.blit(size_example_txt, (100, 225))
        window_surface.blit(manuel_txt, (100, 275))
        # Load one vehicule
        # Blit the users car. (Bumblebee)
        window_surface.blit(allVehicles.vehicles[player_index].image,
                            (player.x, player.y))
        display_scoreboard()

    # Blit the surface "button_surface" on the main surface (window_surface) on coord x,y = 100,75.
    # For exemple we can control it.

    # Applies new changes on the display.
    pygame.display.flip()


# Colors for display.
WHITE, BLACK, GREEN, RED, GRAY = (255, 255, 255), (0, 0, 0), (0, 128, 0), (255, 0, 0), (224, 224, 224)
BROWN = (160, 82, 45)

# Exemple loading a pic.
button_surface = pygame.image.load('assets/button.png')

pygame.init()
icon_surface = pygame.image.load('assets/icon.ico')
pygame.display.set_icon(icon_surface)

# Creating window. window_surface is the surface we're gonna write on.
window_width, window_height = 480, 680
pygame.display.set_caption("Car Project")
window_surface = pygame.display.set_mode((window_width, window_height))

# Loading a font.
font_lemonmilk = pygame.font.Font('assets/LEMONMILK-Regular.otf', 20)

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
pygame.key.set_repeat(1, 1)

game_state = "menu"

# First display.
display(game_state)

# Will store all GameObject
gameObject_list = {}
player = pl.Player(speed=1, life=3, coordinates=(window_width / 2 - allVehicles.vehicles[player_index].width / 2, \
        window_height - 50 - allVehicles.vehicles[player_index].height), \
        size=(allVehicles.vehicles[player_index].width, allVehicles.vehicles[player_index].height))

# Start mainloop.
launched = True
while launched:

    # Collect and use events for user.
    # Collect and use events for user.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("clic gauche")
        elif event.type == pygame.KEYDOWN:
            if game_state == "menu":
                if event.key == pygame.K_BACKSPACE:
                    game_state = "in_game"

            elif game_state == "in_game":
                if event.key == pygame.K_UP and player.check_collision_border("Top", 0):
                    player.move('up')
                elif event.key == pygame.K_DOWN and player.check_collision_border("Bottom", window_height):
                    player.move('down')
                elif event.key == pygame.K_LEFT and player.check_collision_border("Left", 0):
                    player.move('left')
                elif event.key == pygame.K_RIGHT and player.check_collision_border("Right", window_width):
                    player.move('right')
    player.check_all_collisions(gameObject_list)


    display(game_state)

    # For fps.
    clock.tick(60)

# Force exit program
pygame.display.quit()
