import pygame
from game import Game
from setting import Settings

def main():
    pygame.init()
    settings = Settings()
    game = Game(settings)
    game.run()

if __name__ == "__main__":
    main()