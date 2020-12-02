import pygame
import vehicles as vh


def step(pos, key):
    if key == "up":
        pos[1] -= 10
    elif key == "down":
        pos[1] += 10
    elif key == "right":
        pos[0] += 10
    elif key == "left":
        pos[0] -= 10
    return pos


def display(pos):
    # Color entire window with a certain color.
    window_surface.fill((255, 255, 255))

    # Loading new texts.
    example_txt = font_lemonmilk.render("Example", True, BLACK)
    size_example_txt = font_lemonmilk.render("size of example : " + str(example_txt.get_size()), True, BLACK)
    manuel_txt = font_lemonmilk.render("Use UP DOWN LEFT RIGHT key", True, BLACK)
    # Blit new texts.
    window_surface.blit(example_txt, (100, 175))
    window_surface.blit(size_example_txt, (100, 225))
    window_surface.blit(manuel_txt, (100, 275))
    # Load one vehicule
    window_surface.blit(allVehicles.getListVehicules()[0].getImage(), (0, 0),
                        allVehicles.getListVehicules()[0].getRect())

    # Blit the surface "button_surface" on the main surface (window_surface) on coord x,y = 100,75.
    # For exemple we can control it.
    window_surface.blit(button_surface, (pos[0], pos[1]))

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

# clock is for fps
clock = pygame.time.Clock()

# Allow to hold the same key (arg in ms)
pygame.key.set_repeat(1, 1)

# Pos of button for example
pos = [0, 0]

# First display.
display(pos)

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
                pos = step(pos, "up")
            elif event.key == pygame.K_DOWN:
                pos = step(pos, "down")
            elif event.key == pygame.K_LEFT:
                pos = step(pos, "left")
            elif event.key == pygame.K_RIGHT:
                pos = step(pos, "right")
            display(pos)

    # For fps.
    clock.tick(60)

# Force exit program
pygame.display.quit()
