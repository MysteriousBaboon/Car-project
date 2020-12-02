import pygame
import vehicles as vh

def step(key):
    if key == "up":
        allVehicles.vehicles[index[0]].y -= 10
    elif key == "down":
         allVehicles.vehicles[index[0]].y += 10
    elif key == "right":
        allVehicles.vehicles[index[0]].x += 10
    elif key == "left":
        allVehicles.vehicles[index[0]].x -= 10
    if key == "+index[0]":
    	index[0] += 1
    	print(index[0])
    elif key == "-index[0]":
    	index[0] -= 1
    	print(index[0])

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
    window_surface.blit(allVehicles.getListVehicules()[index[0]].getImage(), (allVehicles.vehicles[index[0]].x, allVehicles.vehicles[index[0]].y))
    window_surface.blit(allVehicles.sprite_sheet, (0, 0))

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
index = [0]

# clock is for fps
clock = pygame.time.Clock()

# Allow to hold the same key (arg in ms)
pygame.key.set_repeat(1000, 1000)

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
            elif event.key == pygame.K_c:
                step("+index[0]")
            elif event.key == pygame.K_v:
                step("-index[0]")
            display()

    # For fps.
    clock.tick(60)

# Force exit program
pygame.display.quit()
