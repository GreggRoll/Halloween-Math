import pygame
from game import askQuestion
pygame.init()

window_len = 1280
window_width = 720
win = pygame.display.set_mode((window_len, window_width))
pygame.display.set_caption("Halloween Math")
char = pygame.image.load('undertale.png')
    #TODO
    #crop out whitespace on undertale
    #create animation frames for movement
bg = pygame.image.load('graveyard(1280x720).png')
    #TODO
    #add 10 headstones to work as progress markers

lives = 3
    #TODO
    #create graphics for lives
    #can use for i in lives draw(life.png) x + 50

font = pygame.font.SysFont('comicsans', 30, True)

    #TODO 
    #create class for user
x = 100
y = 560
width = 64
height = 64


def redrawGameWindow():
    #draw background
    win.blit(bg, (0,0))
    #draw health with background
    health = font.render(f'lives: {lives} ', 1, (255,255,255))#81x21
    pygame.draw.rect(win,(160,160,160), (589.5, 90, 105, 41))
    win.blit(health, (599.5, 100))
    #draw question
    question_text = font.render(question, 1, (255,255,255))
    pygame.draw.rect(win,(160,160,160), (547, 190, 186, 41))
    win.blit(question_text, (557, 200))#166, 21
    #draw sprite
    win.blit(char, (x, y, width, height))
    #update
    #TODO
    #create input box for answers

    pygame.display.update()

#main loop
run = True
while lives >= 0:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    #TODO
    #use game.py to get random questions
    question = 'what is 1 + 2?'
    if question == False:
        lives -= 1
    if question == True: 
        x += 10
       
    redrawGameWindow()

