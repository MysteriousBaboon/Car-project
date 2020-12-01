import pygame

pygame.init()
pygame.display.set_caption("Autoclicker")
window_width, window_height = 640, 480
window_surface = pygame.display.set_mode((window_width, window_height))

launched = True
clock = pygame.time.Clock()
while launched:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			launched = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				print("clic gauche")
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				print(event.key)
	clock.tick(60)
