import pygame
import random

# Initialize Pygame
pygame.init()

# Width and height of map
width = 1080
height = 768
clock = pygame.time.Clock()

# Create game display window
game_display = pygame.display.set_mode((1080, 768))
pygame.display.set_caption("EcoPant")

# Load and scale the walking images
# Load and scale the walking images
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png')]
Right_width, Right_height = walkRight[0].get_size()
Right_scale_factor = 4  # Adjust the scale factor as needed
walkRight = [pygame.transform.scale(img, (Right_width * Right_scale_factor, Right_height * Right_scale_factor)) for img in walkRight]

walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png')]
left_width, left_height = walkLeft[0].get_size()
left_scale_factor = 4  # Adjust the scale factor as needed
walkLeft = [pygame.transform.scale(img, (left_width * left_scale_factor, left_height * left_scale_factor)) for img in walkLeft]

# Load bottle images
flaske_images = [pygame.image.load('Fanta orange flaske.png'), pygame.image.load('Cola flaske.png'), pygame.image.load('Sprite flaske.png'), pygame.image.load('Solo flaske.png')]

# Load initial background
bg1 = pygame.image.load('map 1.png')

# Load and scale character image
char = pygame.image.load('standing.png')
char_width, char_height = char.get_size()
char_scale_factor = 4 # Adjust the scale factor as needed
char = pygame.transform.scale(char, (char_width * char_scale_factor, char_height * char_scale_factor))

# Load and scale chest image
chest = pygame.image.load('Panteposen.png')
chest_width, chest_height = chest.get_size()    
chest_scale_factor = 2 # Adjust the scale factor as needed
chest = pygame.transform.scale(chest, (chest_width * chest_scale_factor, chest_height * chest_scale_factor))

# Load and scale vending machine image
vending_machine_img = pygame.image.load('P1.png')
vending_machine_width, vending_machine_height = vending_machine_img.get_size()
vending_machine_scale_factor = 4  # Adjust the scale factor as needed
vending_machine_img = pygame.transform.scale(vending_machine_img, (vending_machine_width * vending_machine_scale_factor, vending_machine_height * vending_machine_scale_factor))

# Initial character position
x = 200
y = 545

# Initial chest position (offset from character)
chest_offset_x = -5
chest_offset_y = 50

# Initial vending machine position
vending_machine_x = 135
vending_machine_y = 545 

# Variable to store the current background
current_bg = 'map 1.png'

# List to store bottle objects
bottles = []

# List to store collected bottles
collected_bottles = []

# Initialize flags and variables
# Initialize flags and variables
left_flag = False 
right_flag = False
walkcount = 0
chest_visible = False
picked_bottles = 0
coins = 0
spawn_rate = 0
vending_machine_visible = True # Define and set vending machine visibility to True initially


# Function to spawn bottles randomly
def spawn_bottles():
    global bottles
    # Clear the list of bottles
    bottles = []
   
    # Specify the range of x and y coordinates for bottle spawning
    x_range = range(200, 1000)
    y_range = 668

    # Ensure that there are enough positions to sample from
    if len(x_range) >= spawn_rate >= spawn_rate:
        # Randomly select positions from the ranges and create bottle objects
        for _ in range(spawn_rate):
            x_pos = random.choice(x_range)
            y_pos = 668
            bottle = Bottle(x_pos, y_pos, random.choice(flaske_images))
            bottles.append(bottle)
    else:
        # Handle the case where there are not enough positions to sample from
        print("Not enough positions to spawn bottles.")

# Function to spawn vending machine on map 1
def spawn_vending_machine():
    global vending_machine_img, vending_machine_x, vending_machine_y
    vending_machine_img = pygame.transform.scale(vending_machine_img, (vending_machine_width * vending_machine_scale_factor, vending_machine_height * vending_machine_scale_factor))
    vending_machine_x = 500
    vending_machine_y = 400

# Class for bottles
class Bottle:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.picked_up = False

    def draw(self, screen):
        if not self.picked_up:
            screen.blit(self.image, self.rect)

# Function to check collision between player and bottles
# Function to check collision between player and bottles
def check_collision():
    global picked_bottles
    for bottle in bottles:
        if not bottle.picked_up and pygame.Rect(x, y, char_width * char_scale_factor, char_height * char_scale_factor).colliderect(bottle.rect):
            if chest_visible:  # Check if the chest is visible
                bottle.picked_up = True
                picked_bottles += 1
                collected_bottles.append(bottle)


# Function to check collision between player and vending machine
def check_vending_machine_collision():
    global coins, collected_bottles, bottles
    vending_machine_rect = pygame.Rect(vending_machine_x, vending_machine_y, vending_machine_width * vending_machine_scale_factor, vending_machine_height * vending_machine_scale_factor)
    player_rect = pygame.Rect(x, y, char_width * char_scale_factor, char_height * char_scale_factor)
    if player_rect.colliderect(vending_machine_rect):
        # Calculate total coins based on the number of bottles
        coins += len(collected_bottles * 2)
        collected_bottles = []  # Empty the collected bottles list after exchange

# Load next background function
def load_next_background():
    global current_bg, x, y, spawn_rate, vending_machine_visible
    if current_bg == 'map 1.png':
        current_bg = 'M2.png'
        x = 20
        spawn_rate += 2
        vending_machine_visible = False
    elif current_bg == "M2.png": 
        current_bg = "M3.png"
        x = 20
        spawn_rate += 2
        vending_machine_visible = False
    elif current_bg == "M3.png": 
        current_bg = "M4.png"
        x = 20
        spawn_rate += 2
        vending_machine_visible = False
    else:
        current_bg = 'map 1.png'
        x = width - (char_width * char_scale_factor) - 20
        vending_machine_visible = True  # Set vending machine visibility to False for subsequent maps
    y = 545
    spawn_bottles()  # Call to spawn bottles for the new background


def load_previous_background():
    global current_bg, x, y, spawn_rate, vending_machine_visible
    if current_bg == "M3.png": 
        current_bg = "M2.png"
        x = width - (char_width * char_scale_factor) - 20
        spawn_rate += 2  
        vending_machine_visible = False
    elif current_bg == "M4.png": 
        current_bg = "M3.png"
        x = width - (char_width * char_scale_factor) - 20
        spawn_rate += 2  
        vending_machine_visible = False
    elif current_bg == "M2.png": 
        current_bg = "map 1.png"
        x = width - (char_width * char_scale_factor) - 20
        vending_machine_visible = True

    else:
        current_bg = 'map 1.png'
        x = width - (char_width * char_scale_factor) - 20
        vending_machine_visible = True  # Only spawn vending machine if it's currently visible
        
            
    y = 545
    spawn_bottles()  # Call to spawn bottles for the previous background


# Function to redraw the game window
def redraw_game_window():
    global walkcount 
    # Draw background 
    game_display.blit(pygame.image.load(current_bg), (0, 0))

    # Draw bottles
    for bottle in bottles:
        bottle.draw(game_display)

    if chest_visible:
        game_display.blit(chest, (x + chest_offset_x, y + chest_offset_y))


    # Draw vending machine
    if vending_machine_visible:
        game_display.blit(vending_machine_img, (vending_machine_x, vending_machine_y))

    # Draw character
    if walkcount + 1 >= 12: 
        walkcount = 0 

    if left_flag: 
        game_display.blit(walkLeft[walkcount//3], (x, y))
        walkcount += 1
    elif right_flag: 
        game_display.blit(walkRight[walkcount//3], (x, y))
        walkcount += 1
    else: 
        game_display.blit(char, (x, y))
    
    # Draw bottles picked up counter
    font = pygame.font.SysFont(None, 36)  # Choose font and size
    text = font.render("Bottles Picked: " + str(picked_bottles), True, (255, 255, 255))  # Render text
    game_display.blit(text, (10, 10))  # Blit text onto the screen at position (10, 10)

    # Draw coins collected counter
    coins_text = font.render("Coins: " + str(coins), True, (255, 255, 255))  # Render text
    game_display.blit(coins_text, (10, 50))  # Blit text onto the screen at position (10, 50)

    # Update display
    pygame.display.update()

# Main game loop
quit_game = False
while not quit_game:
    clock.tick(45)
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

        # Toggle chest visibility when 'e' key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                chest_visible = not chest_visible

    # Handle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if current_bg != 'map 1.png' or (current_bg == 'map 1.png' and x > 200):
            x -= 6  # Move left
            left_flag = True
            right_flag = False
            while chest_offset_x < 100:
                chest_offset_x += 6
            if chest_offset_x == 100:
                chest_offset_x -= 0.1

            # Check if the character is moving out of the screen on the left
            if x <= 0:
                load_previous_background()

    elif keys[pygame.K_d]:
        if current_bg != 'M4.png' or (current_bg == 'M4.png' and x < 950):
            x += 6  # Move right
            right_flag = True
            left_flag = False
            while chest_offset_x > -50:
                chest_offset_x -= 6
            if chest_offset_x == -50:
                chest_offset_x -= 0.1

            # Check if the character is moving out of the screen on the right
            if x + char_width * char_scale_factor >= width:
                load_next_background()

    else:
        right_flag = False
        left_flag = False
        walkcount = 0

    check_collision()  # Check collision between player and bottles
    redraw_game_window()
    if current_bg == "map 1.png":
        check_vending_machine_collision()
    # Spawn bottles if there are none on the ground
    if not bottles:
        spawn_bottles()

# Quit Pygame
pygame.quit()
