import pygame

def step():
	pass

def display():
	# Color entire window with a certain color.
	window_surface.fill((255, 255, 255))

	# Blit the surface "button_surface" on the main surface (window_surface) on coord x,y = 100,75.
	window_surface.blit(button_surface, (100, 75))
	# Loading new texts.
	example_txt = font_lemonmilk.render("Example", True, BLACK)
	size_example_txt = font_lemonmilk.render("size of example : " + str(example_txt.get_size()), True, BLACK)
	# Blit new texts.
	window_surface.blit(example_txt, (100, 175))
	window_surface.blit(size_example_txt, (100, 275))

	# Applies new changes on the display.
	pygame.display.flip()
	

# Colors for display.
WHITE, BLACK, GREEN, RED, GRAY  = (255, 255, 255), (0, 0, 0), (0,128,0), (255,0,0), (224, 224, 224)

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

# clock is for fps
clock = pygame.time.Clock()

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

	# Do things.
	step()
	display()

	# For fps.
	clock.tick(60)
