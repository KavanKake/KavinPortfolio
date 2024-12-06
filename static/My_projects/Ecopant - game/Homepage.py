import pygame
import sys

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (215, 210, 255)

# Set up the display
screen_width = 1080
screen_height = 768
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("EcoPant - Homepage")

# Load background image
background_img = pygame.image.load('Ecopant forside.png')
background_img = pygame.transform.scale(background_img, (screen_width, screen_height))

# Load logo image
# Load logo image and adjust its size
logo_img = pygame.image.load('Ecopant logo.png')
logo_size = (100, 100)  # Change the size of the logo here
logo_img = pygame.transform.scale(logo_img, logo_size)


# Load play button image
play_btn_img = pygame.image.load('start.png')

# Define button dimensions and position
play_btn_size = (300, 300)  # Change the size of the button here
play_btn_img = pygame.transform.scale(play_btn_img, play_btn_size)
play_btn_rect = play_btn_img.get_rect()
play_btn_rect.center = (screen_width // 2, screen_height // 2 + 100)

# Define font
font = pygame.font.SysFont(None, 60)

# Main menu loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_btn_rect.collidepoint(event.pos):
                running = False  # Exit the loop and start the game

    # Draw background
    screen.blit(background_img, (0, 0))

    # Draw logo
    screen.blit(logo_img, (50, 20))

    # Draw play button
    screen.blit(play_btn_img, play_btn_rect)

    # Draw title text
    title_text = font.render("Welcome to EcoPant", True, BLACK)
    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 300))

    # Draw instructions
    instructions_text = font.render("Click PLAY to start", True, BLACK)
    screen.blit(instructions_text, (screen_width // 2 - instructions_text.get_width() // 2, 400))

    pygame.display.flip()

# Quit Pygame
pygame.quit()
