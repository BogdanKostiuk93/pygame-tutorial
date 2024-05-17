import pygame
pygame.init()

FPS = 60
pygame.display.set_mode((600,400), pygame.RESIZABLE | pygame.HWSURFACE)
pygame.display.set_caption("My first programm")
pygame.display.set_icon(pygame.image.load('logo.bmp')) #only bmp works
clock = pygame.time.Clock()

flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            # pygame.quit()
            # flRunning =False

    clock.tick(FPS)



