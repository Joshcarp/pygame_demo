import pygame
from pygame.locals import *
 
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.position = [0,0]
 
    def on_init(self):
        pygame.init()
        
        self._display_surf = pygame.display.set_mode((350,350), pygame.HWSURFACE)
        self._running = True
        self._image_surf = pygame.image.load("ball.png").convert()
        self._display_surf.fill((0,0,0))
        
    
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.position = [self.position[0]-10, self.position[1]]
            if event.key == pygame.K_RIGHT:
                self.position = [self.position[0]+10, self.position[1]]
            if event.key == pygame.K_DOWN:
                self.position = [self.position[0], self.position[1]+10]
            if event.key == pygame.K_UP:
                self.position = [self.position[0], self.position[1]-10]
    def on_loop(self):
        pass
    def on_render(self):
        # pygame.display.flip()
        self._display_surf.blit(self._image_surf,self.position)
        pygame.display.flip()
        self._display_surf.fill((0,0,0))
        # pygame.display.update()

    
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
