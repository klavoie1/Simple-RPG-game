import pygame

class Game():
    def __init__(self, settings):
        self.settings = settings
        self.screen = pygame.display.set_mode((self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT))
        pygame.display.set_caption("RPG Game")
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(self.settings.FPS)
        
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass # Game logic and updates

    def draw(self):
        self.screen.fill(self.settings.BG_COLOR)
        # Draw Game Objects here

        pygame.display.flip()