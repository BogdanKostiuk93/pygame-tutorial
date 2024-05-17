import pygame
pygame.init()

FPS = 60
W, H = 600, 400

sc = pygame.display.set_mode((W,H))
pygame.display.set_caption("Drawing")
pygame.display.set_icon(pygame.image.load('logo.bmp')) #only bmp works

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# We draw on the BACK side. For a user to see - we need to flip it
pygame.draw.rect(sc, WHITE, (20,20,100,100))
pygame.draw.rect(sc, BLUE, (200,20,300,100),2)

pygame.draw.line(sc, GREEN, (10,150),(160,200),5)
pygame.draw.aaline(sc, GREEN, (10,170),(160,220)) #for a smoothed lines

pygame.draw.polygon(sc, WHITE, [[150,150],[300,190], [300,290],[200,260]])
pygame.draw.polygon(sc, WHITE, [[350,150],[500,190], [500,290],[400,260]],5)

pygame.draw.circle(sc, BLUE, (100,300),40)
pygame.draw.ellipse(sc, BLUE, (300,300,100,50), 1)

# pygame.display.flip()
# Alternativelly you can use pygame.display.update() - we can pass a specific area to be updated
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()





