import pygame
pygame.init()

FPS = 60
clock = pygame.time.Clock()
W, H = 600, 400

sc = pygame.display.set_mode((W,H))
pygame.display.set_caption("Mouse")
pygame.display.set_icon(pygame.image.load('logo.bmp')) #only bmp works


WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

sc.fill(WHITE)
sp = ep = None
flStartDraw = False
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    pressed = pygame.mouse.get_pressed()

    if pressed[0]:
        pos = pygame.mouse.get_pos()

        if sp is None:
            sp = pos
        
        width = pos[0] - sp[0]
        height = pos[1] - sp[1]

        sc.fill(WHITE)
        pygame.draw.rect(sc,BLUE,(sp[0],sp[1],width,height))
        pygame.display.update()

    else:
        sp = None
        
        # elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        #     flStartDraw = True
        #     sp = event.pos

        # elif event.type == pygame.MOUSEMOTION and flStartDraw:
        #     pos = event.pos
        #     sc.fill(WHITE)
        #     pygame.draw.rect(sc, BLUE, (sp[0],sp[1],pos[0] - sp[0],pos[1]-sp[1]))
        #     pygame.display.update()

        # elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        #     flStartDraw = False


        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     print(f'Нажата кнопка: {event.button}')
        
        # elif event.type == pygame.MOUSEMOTION:
        #     print(f'Абсолютная позиция мыши: {event.pos}')
        #     print(f'Относительная позиция мыши: {event.rel}')

        


    clock.tick(FPS)




