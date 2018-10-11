import pygame
from game import askQuestion
pygame.init()

window_len = 1280
window_width = 720
win = pygame.display.set_mode((window_len, window_width))
pygame.display.set_caption("Halloween Math")
char = pygame.image.load('undertale.png')
bg = pygame.image.load('graveyard(1280x720).png')

lives = 3
font = pygame.font.SysFont('comicsans', 30, True)

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
    pygame.display.update()

#main loop
run = True
while lives >= 0:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    question = 'what is 1 + 2?'
    if question == False:
        lives -= 1
    if question == True: 
        x += 10
       
    redrawGameWindow()

