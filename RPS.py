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
Computer_choise = None
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