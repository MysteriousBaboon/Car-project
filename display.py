import pygame
import time


# Colors for display.
WHITE, BLACK, GREEN, RED, GRAY = (255, 255, 255), (0, 0, 0), (0, 128, 0), (255, 0, 0), (224, 224, 224)
BROWN = (160, 82, 45)

class Window:
    def __init__(self, width=100, height=100, font="None"):
        self.width = width
        self.height = height
        self.font = font
        self.surface = pygame.display.set_mode((self.width, self.height))
            
    def display_scoreboard(self, init_timer):
        pygame.draw.rect(self.surface, BROWN, pygame.Rect(0, 0, self.width, 100))
        pygame.draw.rect(self.surface, BLACK, pygame.Rect(0, 0, self.width, 100), 2)
        score_txt = self.font.render("Score :", True, BLACK)
        self.surface.blit(score_txt, (100, 50 - score_txt.get_size()[1] / 2))
        score = int((time.time() - init_timer) * 50)
        value_txt = self.font.render(str(score), True, BLACK)
        self.surface.blit(value_txt, (200, 50 - value_txt.get_size()[1] / 2))
        kilo_txt = self.font.render("Km", True, BLACK)
        self.surface.blit(kilo_txt, (250, 50 - value_txt.get_size()[1] / 2))
    
    
    def display(self, game_state, player, list_bot, allVehicles, init_timer, road, score=0):
        global idVehicle
        
        if game_state == "menu":
            self.surface.fill(GREEN)
            cargame_txt = self.font.render("CAR GAME", True, BLACK)
            pressenter_txt = self.font.render("Press Enter to start.", True, BLACK)
            tuto_txt = self.font.render("Use Left and Right.", True, BLACK)
            self.surface.blit(cargame_txt, (self.width / 2 - cargame_txt.get_size()[0] / 2, 100))
            self.surface.blit(tuto_txt, (self.width / 2 - tuto_txt.get_size()[0] / 2, 200))
            self.surface.blit(pressenter_txt, (self.width / 2 - pressenter_txt.get_size()[0] / 2, 300))
    
        elif game_state == "in_game":
            # Color entire window with a certain color.
            self.surface.fill(GREEN)
            #time.time() - init_timer
            road.display(4)
            #window.surface.blit(allVehicles.vehicles[21].image, (player.x * 85 + 100, player.y))
            player.update()
            self.surface.blit(allVehicles.getVehicle(21).image, (player.x, player.y))
            i = 0
            while i < len(list_bot):
                list_bot[i].y += 2
                if list_bot[i].y >= self.height:
                    list_bot.pop(i)
                    i -= 1
                else:
                    self.surface.blit(list_bot[i].image, (list_bot[i].x, list_bot[i].y))
                i += 1
            self.display_scoreboard(init_timer)
    
        elif game_state == "game_over":
            self.surface.fill(GREEN)
            gameover_txt = self.font.render("GAME OVER", True, BLACK)
            pressenter_txt = self.font.render("Press Enter to restart.", True, BLACK)
            score_txt = self.font.render(f"Your score: {str(score)}", True, BLACK)
            self.surface.blit(gameover_txt, (self.width / 2 - gameover_txt.get_size()[0] / 2, 100))
            self.surface.blit(pressenter_txt, (self.width / 2 - pressenter_txt.get_size()[0] / 2, 200))
            self.surface.blit(score_txt, (self.width / 2 - score_txt.get_size()[0] / 2, 300))
    
        # Applies new changes on the display.
        pygame.display.flip()
