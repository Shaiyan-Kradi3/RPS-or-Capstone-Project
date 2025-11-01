import pygame
import random
import sys

# Initial Setup
pygame.init()

# Screen size and title
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎮 Rock Paper Scissors")

# Colors (RPG Format)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 120, 255)
GRAY = (220, 220, 220)

# Fonts
font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 48)

# Load Images
rock_img =pygame.image.load("rock.png")
paper_img =pygame.image.load("paper.png")
scissors_img =pygame.image.load("scissors.png")

# Resize all images to fit buttons
rock_img = pygame.transform.scale(rock_img, (100, 100))
paper_img = pygame.transform.scale(paper_img, (100, 100))
scissors_img = pygame.transform.scale(scissors_img, (100, 100))

# Choices and their images
choices = {
    'Rock': rock_img,
    'Paper': paper_img,
    'Scissors': scissors_img
}

#Button Positions
buttons = {
    'Rock': pygame.Rect(60, 280, 100, 100),
    'Paper': pygame.Rect(250, 280, 100, 100),
    'Scissors': pygame.Rect(440, 280, 100, 100),
}

# Game state Variables
player_choice = None
computer_choice = None
result = ""

# Function to decide Winner
def decide_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return "You win!"
    else:
        return "You Lose!"

# Main Game Loop
running = True
while running:
    screen.fill(WHITE)

    #Title
    title_text = big_font.render("Rock Paper Scissors", True, BLUE)
    screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 20))

    # Show instruction
    info_text = font.render("Choose your move:", True, BLACK)
    screen.blit(info_text, (WIDTH//2 - info_text.get_width()//2, 60))

    # Display player and computer choices
    if player_choice:
        # PLayer side
        screen.blit(choices[player_choice], (120, 150))
        player_label = font.render("You", True, BLACK)
        screen.blit(player_label, (160, 250))
    if computer_choice:
        # Computer side
        screen.blit(choices[computer_choice], (380, 150))
        comp_label = font.render("Computer", True, BLACK)
        screen.blit(comp_label, (380, 250))

    # Display result
    if result:
        result_text = big_font.render(result, True, BLACK)
        screen.blit(result_text, (WIDTH//2 - result_text.get_width()//2, 100))

    # Draw buttons (Image as buttons)
    for name, rect in buttons.items():
        pygame.draw.rect(screen, GRAY, rect, border_radius=12)
        screen.blit(choices[name], (rect.x, rect.y))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exitt()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if any button was clicked
            for name, rect in buttons.items():
                if rect.collidepoint(event.pos):
                    player_choice = name
                    computer_choice = random.choice(list(choices.keys()))
                    result = decide_winner(player_choice, computer_choice)

    # Update display
    pygame.display.flip()