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
    #create animated frames for movement

#input box rect
#will become area for inputz
input_box = pygame.Rect(540, 250, 100, 32)
text = ''
active = False
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive

bg = pygame.image.load('graveyard(1280x720).png')
    #TODO
    #add 10 headstones to work as progress markers
progress = 0
    #TODO
    #if progress = 10 make it so game is over and halloween candy flies around or somthing
lives = 3
    #TODO
    #create graphics for lives
    #can use for i in lives draw(life.png) x + 50

font = pygame.font.SysFont('comicsans', 30, True)

    #TODO 
    #create class for user
x = 100
y = 560
char_width = 64
char_height = 64


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
    win.blit(char, (x, y, char_width, char_height))
    #update
    answer_txt = font.render(text, True, (255, 255, 255))
    width = max(200, answer_txt.get_width()+10)
    input_box.w = width
    win.blit(answer_txt, (input_box.x+5, input_box.y+5))
    pygame.draw.rect(win, (255, 100, 0), input_box, 2)
    #TODO
    #create input box for answers

    pygame.display.update()

#main loop
run = True
while 1:
    #make somthing so that a screen apears when lives are less than 0
    pygame.time.delay(100)
    done = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        #TODO
        #store input and compare once random questions is working
        #will need to try/except incase anyone tries to use letters
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print(text)
                text = ''
                done = True
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode
    #TODO
    #use game.py to get random questions
    question = 'what is 1 + 2?'
    if done == True:
        answr = False
        if text == 3:
            answr = True
            x += 105
            progress += 1
        else:
            lives -= 1
    text = str(text)
    
    
       
       
    redrawGameWindow()

