import pygame
import sys
from constants import *

def main():
    pygame.init()
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    CLOCK = pygame.time.Clock()
    pygame.display.set_caption("Work timer")

    background = pygame.image.load("assets/3headeddrag.jpg")
    Red_circle = pygame.image.load("assets/backdrop.png")
    white_button = pygame.image.load("assets/button.png")



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        SCREEN.fill("#ba4949")

        pygame.display.update()

        CLOCK.tick(60) # limit to 60 dps




if __name__ == "__main__":
    main()