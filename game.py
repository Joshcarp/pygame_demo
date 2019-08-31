import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")

x= 50 
y = 50
width = 50 
height = 50 
dims = (x,y,width, height)
vel = 5

# pygame.quit()
run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            pygame.quit()
    pygame.draw.rect(win, (255, 0, 0), dims);

