import pygame
import time


class Window:
    def __init__(self, width=100, height=100, font="None"):
        self.width = width
        self.height = height
        self.font = font
        self.surface = pygame.display.set_mode((self.width, self.height))


# Colors for display.
WHITE, BLACK, GREEN, RED, GRAY = (255, 255, 255), (0, 0, 0), (0, 128, 0), (255, 0, 0), (224, 224, 224)
BROWN = (160, 82, 45)


def display_scoreboard(window, init_timer):
    pygame.draw.rect(window.surface, BROWN, pygame.Rect(0, 0, window.width, 100))
    pygame.draw.rect(window.surface, BLACK, pygame.Rect(0, 0, window.width, 100), 2)
    score_txt = window.font.render("Score :", True, BLACK)
    window.surface.blit(score_txt, (100, 50 - score_txt.get_size()[1] / 2))
    score = int((time.time() - init_timer) * 50)
    value_txt = window.font.render(str(score), True, BLACK)
    window.surface.blit(value_txt, (200, 50 - value_txt.get_size()[1] / 2))
    kilo_txt = window.font.render("Km", True, BLACK)
    window.surface.blit(kilo_txt, (250, 50 - value_txt.get_size()[1] / 2))


def display(game_state, window, player, list_bot, allVehicles, init_timer, road, score=0):
    if game_state == "menu":
        window.surface.fill(GREEN)
        cargame_txt = window.font.render("CAR GAME", True, BLACK)
        pressenter_txt = window.font.render("Press Enter to start.", True, BLACK)
        tuto_txt = window.font.render("Use Left and Right.", True, BLACK)
        window.surface.blit(cargame_txt, (window.width / 2 - cargame_txt.get_size()[0] / 2, 100))
        window.surface.blit(tuto_txt, (window.width / 2 - tuto_txt.get_size()[0] / 2, 200))
        window.surface.blit(pressenter_txt, (window.width / 2 - pressenter_txt.get_size()[0] / 2, 300))

    elif game_state == "in_game":
        # Color entire window with a certain color.
        window.surface.fill(GREEN)
        #time.time() - init_timer
        road.display(4)
        window.surface.blit(allVehicles.vehicles[21].image, (player.x * 85 + 100, player.y))
        i = 0
        while i < len(list_bot):
            list_bot[i].y += 2
            if list_bot[i].y >= window.height:
                list_bot.pop(i)
                i -= 1
            else:
                window.surface.blit(list_bot[i].image, (list_bot[i].x * 85 + 100, list_bot[i].y))
            i += 1
        display_scoreboard(window, init_timer)

    elif game_state == "game_over":
        window.surface.fill(GREEN)
        gameover_txt = window.font.render("GAME OVER", True, BLACK)
        pressenter_txt = window.font.render("Press Enter to restart.", True, BLACK)
        score_txt = window.font.render(f"Your score: {str(score)}", True, BLACK)
        window.surface.blit(gameover_txt, (window.width / 2 - gameover_txt.get_size()[0] / 2, 100))
        window.surface.blit(pressenter_txt, (window.width / 2 - pressenter_txt.get_size()[0] / 2, 200))
        window.surface.blit(score_txt, (window.width / 2 - score_txt.get_size()[0] / 2, 300))

    # Applies new changes on the display.
    pygame.display.flip()
