import pygame

# Colors for display.
WHITE, BLACK, GREEN, RED, GRAY = (255, 255, 255), (0, 0, 0), (0, 128, 0), (255, 0, 0), (224, 224, 224)
BROWN = (160, 82, 45)

def display_road():
    pass


def display_scoreboard(window_surface,window_width, font):
    pygame.draw.rect(window_surface, BROWN, pygame.Rect(0, 0, window_width, 100))
    pygame.draw.rect(window_surface, BLACK, pygame.Rect(0, 0, window_width, 100), 2)
    score_txt = font.render("Score :", True, BLACK)
    window_surface.blit(score_txt, (100, 50 - score_txt.get_size()[1] / 2))
    score = 10000
    value_txt = font.render(str(score), True, BLACK)
    window_surface.blit(value_txt, (200, 50 - value_txt.get_size()[1] / 2))


def display(game_state, window_surface,window_width, window_height, player, list_bot, font, allVehicles):
    if game_state == "menu":
        window_surface.fill(GREEN)
        cargame_txt = font.render("CAR GAME", True, BLACK)
        pressenter_txt = font.render("Press K_BACKSPACE to start.", True, BLACK)

        window_surface.blit(cargame_txt, (window_width / 2 - cargame_txt.get_size()[0] / 2, 100))
        window_surface.blit(pressenter_txt, (window_width / 2 - pressenter_txt.get_size()[0] / 2, 200))

    elif game_state == "in_game":
        # Color entire window with a certain color.
        window_surface.fill(GREEN)

        display_road()
        # display_vehicules()

        # Loading new texts.
        example_txt = font.render("Example", True, BLACK)
        size_example_txt = font.render("size of example : " + str(example_txt.get_size()), True, BLACK)
        manuel_txt = font.render("Use UP DOWN LEFT RIGHT key", True, BLACK)
        # Blit new texts.
        window_surface.blit(example_txt, (100, 175))
        window_surface.blit(size_example_txt, (100, 225))
        window_surface.blit(manuel_txt, (100, 275))
        # Load one vehicule
        # Blit the users car. (Bumblebee)
        window_surface.blit(allVehicles.vehicles[21].image,
                            (player.x, player.y))
        i = 0
        while i < len(list_bot):
            list_bot[i].y += 2
            if list_bot[i].y >= window_height:
                list_bot.pop(i)
                i -= 1
            else:
                window_surface.blit(list_bot[i].image, (list_bot[i].x, list_bot[i].y))
            i += 1
        display_scoreboard(window_surface,window_width, font)

    # Blit the surface "button_surface" on the main surface (window_surface) on coord x,y = 100,75.
    # For exemple we can control it.

    # Applies new changes on the display.
    pygame.display.flip()