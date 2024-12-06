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
pygame.display.set_caption("Who wants to be a millionaire? - Homepage")

background_img = pygame.image.load('forside.png')
background_img = pygame.transform.scale(background_img, (screen_width, screen_height))

play_btn_img = pygame.image.load('Play1.png')

# Define button dimensions and position
play_btn_size = (300, 300)  # Change the size of the button here
play_btn_img = pygame.transform.scale(play_btn_img, play_btn_size)
play_btn_rect = play_btn_img.get_rect()
play_btn_rect.center = (screen_width // 2, screen_height // 2 + 100)

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
    screen.blit(background_img, (0, 0))




    

    # Draw instructions
    instructions_text = font.render("Click anywhere to start", True, WHITE)
    screen.blit(instructions_text, (screen_width // 2 - instructions_text.get_width() // 2, 800))

    pygame.display.flip()

# Quit Pygame
pygame.quit()