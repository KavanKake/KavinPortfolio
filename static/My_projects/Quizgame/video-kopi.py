import pygame
import sys

pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pygame Video Player')

# Load the video file
video_file = 'winning scene.mp4'  # Change this to the path of your video file
pygame.display.init()
movie = pygame.movie.Movie(video_file)

# Set up a clock to control frame rate
clock = pygame.time.Clock()

# Play the video
movie_screen = pygame.Surface(movie.get_size()).convert()
movie.set_display(movie_screen)
movie.play()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Blit the video frame to the screen
    screen.blit(movie_screen, (0, 0))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Clean up
pygame.quit()
sys.exit()
