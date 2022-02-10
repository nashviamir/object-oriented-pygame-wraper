import pygame

class Engine:
    

    def __init__(self, dimensions, running=True, fps=60):
        self.running = running
        self.fps = fps
        self.screen = pygame.display.set_mode(dimensions)
        GameObject.screen = self.screen

    def run(self):
        pygame.init()
        #instantiate clock object
        clock = pygame.time.Clock()

        #main loop
        while self.running:
            #sets events as a class attribute to GameObject class
            GameObject.events = pygame.event.get()

            #fill screen with black
            self.screen.fill((0, 0, 0))

            #handles quit event
            for event in GameObject.events:
                if event.type == pygame.QUIT:
                    self.running = False
      
            #updates all game objects
            for obj in GameObject.objects:
                obj.update()

            #limit the frame rate
            GameObject.delta_time = clock.tick(self.fps)
            pygame.display.update()


        pygame.quit()


class GameObject:
    objects = []
    _image = None


    def __init__(self, position, height=None, width=None):
        self.position = position
        self.height = height
        self.width = width
        self.set_image()
        self.start()
        GameObject.objects.append(self)


    def set_image(self):
        if self._image:
            if self.width or self.height:
                pygame.transform.scale(self._image, (self.width, self.height))

            else:
                self.image = self._image
                self.height = self.image.get_height()
                self.width = self.image.get_width()


    def start(self):
        pass
    

    def update(self):
        self.handle_event()
        self.move()
        self.screen.blit(self.image, self.position)
        

    def handle_event(self):
        pass


    def move(self):
        pass


    def remove(self):
        GameObject.objects.remove(self)

    
    @property
    def middle(self):
        x, y = self.position
        return (x + (self.width // 2), y + (self.width // 2))


    @middle.setter
    def middle(self, position):
        x, y = position
        self.position = (x - (self.width // 2), y - (self.width // 2))