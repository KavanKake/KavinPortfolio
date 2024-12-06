import pygame
import sys
import random
import os

# Initialize Pygame
pygame.init()
pygame.mixer.init()
# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up the screen
WIDTH, HEIGHT = 1662, 938
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Who Wants to Be a Millionaire")

# Load background image and "riktig A" image
background_image = pygame.image.load("Spørsmål.jpg")
riktig_A_image = pygame.image.load("Riktig A.jpg")
riktig_B_image = pygame.image.load("Riktig B.jpg")
riktig_C_image = pygame.image.load("Riktig C.jpg")
riktig_D_image = pygame.image.load("Riktig D.jpg")

feil_A_image = pygame.image.load("Feil A.jpg")
feil_B_image = pygame.image.load("Feil B.jpg")
feil_C_image = pygame.image.load("Feil C.jpg")
feil_D_image = pygame.image.load("Feil D.jpg")

You_lost_image = pygame.image.load("You Lost.jpg")

# Lifeline images
fifty_fifty_image = pygame.image.load("5050.png")
ask_the_audience_image = pygame.image.load("Ask the crowd.png")
call_an_AI_image = pygame.image.load("Call friend.png")

Start_score = pygame.transform.scale(pygame. image.load("Start.png"), (120, 300))
Score1 = pygame.transform.scale(pygame. image.load("1 penger.png"), (120, 300))
Score2 = pygame.transform.scale(pygame. image.load("2 penger.png"), (120, 300))
Score3 = pygame.transform.scale(pygame. image.load("3 penger.png"), (120, 300))
Score4 = pygame.transform.scale(pygame. image.load("4 penger.png"), (120, 300))
Score5 = pygame.transform.scale(pygame. image.load("5 penger.png"), (120, 300))
Score6 = pygame.transform.scale(pygame. image.load("6 penger.png"), (120, 300))
Score7 = pygame.transform.scale(pygame. image.load("7 penger.png"), (120, 300))
Score8 = pygame.transform.scale(pygame. image.load("8 penger.png"), (120, 300))
Score9 = pygame.transform.scale(pygame. image.load("9 penger.png"), (120, 300))
Score10 = pygame.transform.scale(pygame. image.load("10 penger.png"), (120, 300))
Score11 = pygame.transform.scale(pygame. image.load("11 penger.png"), (120, 300))
Score12 = pygame.transform.scale(pygame. image.load("12 penger.png"), (120, 300))
Score13 = pygame.transform.scale(pygame. image.load("13 penger.png"), (120, 300))
Score14 = pygame.transform.scale(pygame. image.load("14 penger.png"), (120, 300))
Score15 = pygame.transform.scale(pygame. image.load("15 penger.png"), (120, 300))
Siste_score = pygame.transform.scale(pygame. image.load("Siste penger.png"), (120, 300))

Quit_image = pygame.image.load("Quit 2.png")

# Define fonts with bigger sizes
question_font = pygame.font.Font(None, 48)  # Increased font size for the question
answer_font = pygame.font.Font(None, 36)    # Increased font size for the answers
result_font = pygame.font.Font(None, 72)    # Adjust as needed

# Define questions and answers
questions = [
    "Which planet is closest to the sun?",
    "What is the capital city of France?",
    "Who wrote the play Romeo and Juliet?",
    "What is the chemical symbol for gold?",
    "Who was the first female Prime Minister of the United Kingdom?",
    "What is the largest mammal on Earth?", 
    "In which year did the United States declare independence from Britain?", 
    "What is the chemical symbol for water?",
    "Who developed the theory of relativity?",
    "What is the capital city of Australia?",
    "What is the largest organ in the human body?",
    "Who painted the Mona Lisa?",
    "What is the world's tallest mountain?", 
    "Who wrote To Kill a Mockingbird?",
    "What is the chemical symbol for iron?",
    "In which year did the Soviet Union collapse?",

    # Add more questions here...
]

answers = [
    ["Venus", "Earth", "Mercury", "Mars"],
    ["London", "Rome", "Paris", "Berlin"],
    ["William Shakespeare", "Charles Dickens", "Jane Austen", "Leo Tolstoy"],
    ["Go", "Gd", "Ag", "Au"],
    [" Margaret Thatcher", "Angela Merkel", "Theresa May", "Indira Gandhi"],
    ["Elephant", "Blue whale", " Giraffe", "Hippopotamus"],
    ["1776", "1789", "1812", "1492"],
    ["W", "Wa", "H2O", " Hy"],
    ["Galileo Galilei",  "Albert Einstein", "Isaac Newton", " Nikola Tesla"],
    ["Sydney", "Canberra", "Melbourne", "Brisbane"],
    ["Liver", "Brain", "Heard", "Skin"],
    ["Vincent van Gogh", "Michelangelo", "Pablo Picasso", "Leonardo da Vinci"],
    ["Mount Kilimanjaro", "Mount Everest", "Mount Fuji", "Mount McKinley"],
    ["Harper Lee", "F. Scott Fitzgerald", "Ernest Hemingway", "John Steinbeck"],
    ["Ir", "Fe", "In", "Io"],
    ["1989", "1993", " 1991", "1979"],
    # Add corresponding answers here...
]

correct_answers = [2, 2, 0, 3, 0, 1, 0, 2, 1, 1, 3, 3, 1, 0, 1, 2]  # Index of correct answers for each question
money_pool = 1000000  # Starting money pool
question_index = 0  # Index of current question



# Define anchor point for the question text
question_anchor = (831, 470)

# Define anchor points for answer options
answer_anchors = [(490, 640), (1160, 640), (490, 795), (1160, 795)]

# Lifelines usage
fifty_fifty_used = False
ask_the_audience_used = False
call_an_AI_used = False

Money_and_leave = pygame.image.load("Money and leave.jpg")


def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def draw_question_and_answers():
    # Render question text with the specified font size at the anchor point
    draw_text(questions[question_index], question_font, WHITE, *question_anchor)
        
    # Render answer options with the default font size
    for i, (answer, anchor) in enumerate(zip(answers[question_index], answer_anchors)):
        draw_text(f"{i+1}. {answer}", answer_font, WHITE, *anchor)

def draw_result(result):
    draw_text(result, result_font, RED if result.startswith("Wrong") else GREEN, WIDTH/2, 300)

def display_lifelines():
    # Display lifeline logos at the top right corner
    if not fifty_fifty_used:
        screen.blit(fifty_fifty_image, (1550, 10))
    if not ask_the_audience_used:
        screen.blit(ask_the_audience_image, (1550, 90))
    if not call_an_AI_used:
        screen.blit(call_an_AI_image, (1550, 170))
    if question_index in [0, 1, 4, 9]:  # Check if it's question 1, 2, 5, or 10: 
        take_money_image = pygame.transform.scale(pygame.image.load("Take money.png"), (100, 75)) 
        screen.blit(pygame.transform.scale(pygame.image.load("Take money.png"), (100, 75)), (10, 10))

Hovedlyd =pygame.mixer.Sound("Hovedlyd.mp3")  # Replace "your_music_file.mp3" with your music file path
pygame.mixer.Channel(0).play(Hovedlyd)

Correct = pygame.mixer.Sound("Riktig lyd.mp3")

Wrong = pygame.mixer.Sound("Feil lyd.mp3")

money = pygame.mixer.Sound("Applause.mp3")

ask_the_audience_sound = pygame.mixer.Sound("Ask.mp3")

Call_the_AI_sound = pygame.mixer.Sound("robot.mp3")




# icons images (resized)
fifty_fifty_image = pygame.transform.scale(pygame.image.load("5050.png"), (100, 75))
ask_the_audience_image = pygame.transform.scale(pygame.image.load("Ask the crowd.png"), (100, 75))
call_an_AI_image = pygame.transform.scale(pygame.image.load("Call friend.png"), (100, 75))




def fifty_fifty():
    global fifty_fifty_used
    if not fifty_fifty_used:
        correct_answer_index = correct_answers[question_index]
        incorrect_answers = [i for i in range(4) if i != correct_answer_index]
        # Shuffle the incorrect answer indices and select two of them
        random.shuffle(incorrect_answers)
        incorrect_answers = incorrect_answers[:2]

        # Hide the two incorrect answers
        for index in incorrect_answers:
            answers[question_index][index] = ""

        fifty_fifty_used = True



def ask_the_audience():
    global ask_the_audience_used
    print(question_index)
    if not ask_the_audience_used:
        if question_index in [2, 4, 6, 13]:
            pygame.time.delay(3000)
            pygame.mixer.Channel(0).pause()
            pygame.mixer.Channel(4).play(ask_the_audience_sound)
            screen.blit(pygame.transform.scale(pygame.image.load("Flertallet A.png"), (284,142.5)),(200,200))
            pygame.display.flip()
            pygame.time.delay(3000)
            pygame.mixer.Channel(4).pause()
            pygame.mixer.Channel(0).play(Hovedlyd)

        elif question_index in [5,8,9, 12, 14]: 
            pygame.time.delay(3000)
            pygame.mixer.Channel(0).pause()
            pygame.mixer.Channel(4).play(ask_the_audience_sound)
            screen.blit(pygame.transform.scale(pygame.image.load("Flertallet B.png"), (284,142.5)),(200,200))
            pygame.display.flip()
            pygame.time.delay(3000)
            pygame.mixer.Channel(4).pause()
            pygame.mixer.Channel(0).play(Hovedlyd)

        elif question_index in [0, 1, 7, 15]: 
            pygame.time.delay(3000)
            pygame.mixer.Channel(0).pause()
            pygame.mixer.Channel(4).play(ask_the_audience_sound)
            screen.blit(pygame.transform.scale(pygame.image.load("Flertallet C.png"), (284,142.5)),(200,200))
            pygame.display.flip()
            pygame.time.delay(3000)
            pygame.mixer.Channel(4).pause()
            pygame.mixer.Channel(0).play(Hovedlyd)

        elif question_index in [3, 10, 11]:
            pygame.time.delay(3000)
            pygame.mixer.Channel(0).pause()
            pygame.mixer.Channel(4).play(ask_the_audience_sound)
            screen.blit(pygame.transform.scale(pygame.image.load("Flertallet D.png"), (284,142.5)),(200,200))
            pygame.display.flip()
            pygame.time.delay(3000)
            pygame.mixer.Channel(4).pause()
            pygame.mixer.Channel(0).play(Hovedlyd)

        ask_the_audience_used = True

def call_an_AI():
    global call_an_AI_used
    print(question_index)
    if not call_an_AI_used:
        if question_index in [2, 4, 6, 13]:
            pygame.time.delay(3000)
            pygame.mixer.Channel(0).pause()
            pygame.mixer.Channel(5).play(Call_the_AI_sound)
            screen.blit(pygame.transform.scale(pygame.image.load("AI A.jpg"), (284,142.5)),(200,200))
            pygame.display.flip()
            pygame.time.delay(3000)
            pygame.mixer.Channel(5).pause()
            pygame.mixer.Channel(0).play(Hovedlyd)


        elif question_index in [5,8,9, 12, 14]: 
            pygame.time.delay(3000)
            pygame.mixer.Channel(0).pause()
            pygame.mixer.Channel(5).play(Call_the_AI_sound)
            screen.blit(pygame.transform.scale(pygame.image.load("AI B.jpg"), (284,142.5)),(200,200))
            pygame.display.flip()
            pygame.time.delay(3000)
            pygame.mixer.Channel(5).pause()
            pygame.mixer.Channel(0).play(Hovedlyd)


        elif question_index in [0, 1, 7, 15]: 
            pygame.time.delay(3000)
            pygame.mixer.Channel(0).pause()
            pygame.mixer.Channel(5).play(Call_the_AI_sound)
            screen.blit(pygame.transform.scale(pygame.image.load("Ai C.jpg"), (284,142.5)),(200,200))
            pygame.display.flip()
            pygame.time.delay(3000)
            pygame.mixer.Channel(5).pause()
            pygame.mixer.Channel(0).play(Hovedlyd)

      
        elif question_index in [3, 10, 11]:
            pygame.time.delay(3000)
            pygame.mixer.Channel(0).pause()
            pygame.mixer.Channel(5).play(Call_the_AI_sound)
            screen.blit(pygame.transform.scale(pygame.image.load("AI D.jpg"), (284,142.5)),(200,200))
            pygame.display.flip()
            pygame.time.delay(3000)
            pygame.mixer.Channel(5).pause()
            pygame.mixer.Channel(0).play(Hovedlyd)



        call_an_AI_used = True

def game_loop():
    global money_pool, question_index, indices_to_remove

    running = True
    while running:
        screen.blit(background_image, (0, 0))  # Draw the background image
        
        # Draw the question and answers with a specified font size
        draw_question_and_answers()
        
        # Display lifelines
        display_lifelines()

    
        if question_index in [0, 1, 4, 9]:  # Check if it's question 1, 2, 5, or 10: 
                    take_money_image = pygame.transform.scale(pygame.image.load("Take money.png"), (100, 75))
                # Option to take money and leave        

        if question_index == 0: 
            screen.blit(Start_score, (1400, 30))
        elif question_index == 1: 
            screen.blit(Score1, (1400, 30))
        elif question_index == 2: 
            screen.blit(Score2, (1400, 30))
        elif question_index == 3: 
            screen.blit(Score3, (1400, 30))
        elif question_index == 4: 
            screen.blit(Score4, (1400, 30))
        elif question_index == 5: 
            screen.blit(Score5, (1400, 30))
        elif question_index == 6: 
            screen.blit(Score6, (1400, 30))
        elif question_index == 7: 
            screen.blit(Score7, (1400, 30))
        elif question_index == 8: 
            screen.blit(Score8, (1400, 30))
        elif question_index == 9: 
            screen.blit(Score9, (1400, 30))
        elif question_index == 10: 
            screen.blit(Score10, (1400, 30))
        elif question_index == 11: 
            screen.blit(Score11, (1400, 30))
        elif question_index == 12: 
            screen.blit(Score12, (1400, 30))
        elif question_index == 13: 
            screen.blit(Score13, (1400, 30))
        elif question_index == 14: 
            screen.blit(Score14, (1400, 30))
        elif question_index == 15: 
            screen.blit(Score15, (1400, 30))
        elif question_index == 16: 
            screen.blit(Quit_image, (0,0))
            pygame.display.flip()


        



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                

                if event.key == pygame.K_1:
                    if correct_answers[question_index] == 0:
                        draw_result("Correct!")
                        pygame.time.delay(2000)  # Delay for 5 seconds
                        pygame.mixer.Channel(0).pause()
                        pygame.mixer.Channel(1).play(Correct)
                        screen.blit(riktig_A_image, (0, 0))  # Display "riktig A" image
                        pygame.display.flip()
                        pygame.time.delay(2000)  # Delay for another 5 seconds
                        question_index += 1  # Go to the next question
                        pygame.mixer.Channel(1).pause()
                        pygame.mixer.Channel(0).play(Hovedlyd)
                    else:
                        draw_result("Wrong!")
                        pygame.time.delay(3000)
                        pygame.mixer.Channel(0).pause()
                        pygame.mixer.Channel(2).play(Wrong)
                        screen.blit(feil_A_image, (0,0))
                        pygame.display.flip()
                        pygame.time.delay(3000)
                        screen.blit(You_lost_image, (0,0))
                        pygame.display.flip()
                        pygame.time.delay(3000)
                        running = False

                elif event.key == pygame.K_2:
                    if correct_answers[question_index] == 1:
                        draw_result("Correct!")
                        pygame.time.delay(2000)  # Delay for 2 seconds
                        pygame.mixer.Channel(0).pause()
                        pygame.mixer.Channel(1).play(Correct)
                        screen.blit(riktig_B_image, (0, 0))  # Display "riktig A" image
                        pygame.display.flip()
                        pygame.time.delay(2000)  # Delay for another 2 seconds
                        question_index += 1  # Go to the next question
                        pygame.mixer.Channel(1).pause()
                        pygame.mixer.Channel(0).play(Hovedlyd)
                    else:
                        draw_result("Wrong!")
                        pygame.time.delay(3000)
                        pygame.mixer.Channel(0).pause()
                        pygame.mixer.Channel(2).play(Wrong)
                        screen.blit(feil_B_image, (0,0))
                        pygame.display.flip()
                        pygame.time.delay(3000)
                        screen.blit(You_lost_image, (0,0))
                        pygame.display.flip()
                        pygame.time.delay(3000)
                        running = False

                elif event.key == pygame.K_3:
                    if correct_answers[question_index] == 2:
                        draw_result("Correct!")
                        pygame.time.delay(2000)  # Delay for 2 seconds
                        pygame.mixer.Channel(0).pause()
                        pygame.mixer.Channel(1).play(Correct)
                        screen.blit(riktig_C_image, (0, 0))  # Display "riktig A" image
                        pygame.display.flip()
                        pygame.time.delay(2000)  # Delay for another 2 seconds
                        question_index += 1  # Go to the next question
                        pygame.mixer.Channel(1).pause()
                        pygame.mixer.Channel(0).play(Hovedlyd)
                    else:
                        draw_result("Wrong!")
                        pygame.time.delay(3000)
                        pygame.mixer.Channel(0).pause()
                        pygame.mixer.Channel(2).play(Wrong)
                        screen.blit(feil_C_image, (0,0))
                        pygame.display.flip()
                        pygame.time.delay(3000)
                        screen.blit(You_lost_image, (0,0))
                        pygame.display.flip()
                        pygame.time.delay(3000)
                        running = False

                elif event.key == pygame.K_4:
                    if correct_answers[question_index] == 3:
                        draw_result("Correct!")
                        pygame.time.delay(2000)  # Delay for 2 seconds
                        pygame.mixer.Channel(0).pause()
                        pygame.mixer.Channel(1).play(Correct)
                        screen.blit(riktig_D_image, (0, 0))  # Display "riktig A" image
                        pygame.display.flip()
                        pygame.time.delay(2000)  # Delay for another 2 seconds
                        question_index += 1  # Go to the next question
                        pygame.mixer.Channel(1).pause()
                        pygame.mixer.Channel(0).play(Hovedlyd)
                        
                    else:
                        draw_result("Wrong!")
                        pygame.time.delay(3000)
                        pygame.mixer.Channel(0).pause()
                        pygame.mixer.Channel(2).play(Wrong)
                        screen.blit(feil_D_image, (0,0))
                        pygame.display.flip()
                        pygame.time.delay(3000)
                        screen.blit(You_lost_image, (0,0))
                        pygame.display.flip()
                        pygame.time.delay(3000)
                        running = False
                
                elif event.key == pygame.K_q:
                    if question_index == 16: 
                        running = False

                # Lifeline usage
                elif event.key == pygame.K_z:
                    ask_the_audience()
                elif event.key == pygame.K_c:
                    call_an_AI()
                elif event.key == pygame.K_x:
                    fifty_fifty()
                
                elif event.key == pygame.K_t:
                    if question_index in [0, 1, 4, 9]:  # Check if it's question 1, 2, 5, or 10
                        pygame.time.delay(3000)
                        pygame.mixer.Channel(0).pause()
                        pygame.mixer.Channel(3).play(money)             
                        screen.blit(Money_and_leave, (0,0))
                        pygame.display.flip()
                        pygame.time.delay(2000)
                        running = False

                

        pygame.display.flip()






game_loop()
