import os
import pygame
import math
import random

#setup display
pygame.init()
WIDTH, HEIGHT = 1000, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)

#load images
images = []
for i in range(1,8):
    image = pygame.image.load("hangmanPic/hangman" + str(i) + ".png")
    images.append(image)

#game variables
wordBank = ("objective", "bias", "evidence", "curiosity", "perspective", "marginalized","potential","opinion","information", "justice","networking", "communication", "relationships", "background", "authentic", "indigenous", "resilience", "scholarship")
hangman_status = 0
guessed = []
word = random.choice(wordBank).upper()

# colours
WHITE = (255,255,255)
BLACK = (0,0,0)
BUTTON = (85,91,110)
WORD = (46, 147, 60)

#setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True

def draw():
    win.fill(WHITE)

    #draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, WORD)
    win.blit(text,(400, 200))
    
    #draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BUTTON , (x,y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BUTTON)
            win.blit(text, (x - text.get_width()/2, y -text.get_height()/2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


while run: 
    clock.tick(FPS)

    draw()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x,y,ltr,visible = letter
                if visible:
                    dis = math.sqrt((x-m_x)**2 + (y-m_y)**2)
                    if dis < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break
    if won:
        win.fill(WHITE)
        text = WORD_FONT.render("YOU WON!!", 1, BLACK)
        win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(3000)
        break

    if hangman_status == 7:
        win.fill(WHITE)
        text = WORD_FONT.render("YOU LOST :(", 1, BLACK)
        win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(3000)
        break
            
pygame.quit()
