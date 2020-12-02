import pygame
import vehicles as vh

def step(key):
    if key == "up":
        allVehicles.vehicles[player_index].y -= 10
    elif key == "down":
         allVehicles.vehicles[player_index].y += 10
    elif key == "right":
        allVehicles.vehicles[player_index].x += 10
    elif key == "left":
        allVehicles.vehicles[player_index].x -= 10

def display():
    # Color entire window with a certain color.
    window_surface.fill(GREEN)

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
    window_surface.blit(allVehicles.getListVehicules()[player_index].getImage(), (allVehicles.vehicles[player_index].x, allVehicles.vehicles[player_index].y))

    # Blit the surface "button_surface" on the main surface (window_surface) on coord x,y = 100,75.
    # For exemple we can control it.

    # Applies new changes on the display.
    pygame.display.flip()


# Colors for display.
WHITE, BLACK, GREEN, RED, GRAY = (255, 255, 255), (0, 0, 0), (0, 128, 0), (255, 0, 0), (224, 224, 224)

# Exemple loading a pic.
button_surface = pygame.image.load('assets/button.png')

pygame.init()
icon_surface = pygame.image.load('assets/icon.ico')
pygame.display.set_icon(icon_surface)

# Creating window. window_surface is the surface we're gonna write on.
window_width, window_height = 1024, 680
pygame.display.set_caption("Car Project")
window_surface = pygame.display.set_mode((window_width, window_height))

# Exemple loading a font for display.
font_lemonmilk = pygame.font.Font('assets/LEMONMILK-Regular.otf', 20)

# Load all vehicles
allVehicles = vh.Vehicles()
for vehicle in allVehicles.getListVehicules():
    print(vehicle)
player_index = 21

# clock is for fps
clock = pygame.time.Clock()

# Allow to hold the same key (arg in ms)
pygame.key.set_repeat(10, 10)

# First display.
display()

# Start mainloop.
launched = True
while launched:

    # Collect and use events for user.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("clic gauche")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print(event.key)
            elif event.key == pygame.K_UP:
                step("up")
            elif event.key == pygame.K_DOWN:
                step("down")
            elif event.key == pygame.K_LEFT:
                step("left")
            elif event.key == pygame.K_RIGHT:
                step("right")
            display()

    # For fps.
    clock.tick(60)

# Force exit program
pygame.display.quit()
