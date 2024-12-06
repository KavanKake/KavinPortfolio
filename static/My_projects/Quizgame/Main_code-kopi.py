import pygame
import Frontpage as Homepage
import Controlles as Controlles
import WhoWantsToBeAMillionare as Spillet

def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen_width = 1080
    screen_height = 768
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("EcoPant")

    # Run the homepage
    Homepage.run(screen)

    # Run the controlles
    Controlles.run(screen)

    # Run the controlles
    Spillet.run(screen)

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
