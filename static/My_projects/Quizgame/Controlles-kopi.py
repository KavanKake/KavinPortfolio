import pygame 
import sys

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (215, 210, 255)

# Set up the display
screen_width = 1662
screen_height = 938

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Who wants to be a millionaire? - Regler")

Regler = pygame.image.load('Regler.jpg')
Regler = pygame.transform.scale(Regler, (screen_width, screen_height))

font = pygame.font.SysFont(None, 60)

# Main menu loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #if play_btn_rect.collidepoint(event.pos):
                running = False  # Exit the loop and start the game

    # Draw background
    screen.blit(Regler, (0, 0))


    # Draw instructions
    instructions_text = font.render("Click anywhere to start", True, WHITE)
    screen.blit(instructions_text, (screen_width // 2 - instructions_text.get_width() // 2, 900))

    pygame.display.flip()

# Quit Pygame
pygame.quit()

