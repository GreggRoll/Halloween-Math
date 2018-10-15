import random
import operator
import pygame


def randomCalc():
    ops = {'+':operator.add,
           '-':operator.sub,
           '*':operator.mul,}
    num1 = random.randint(0,10)
    num2 = random.randint(1,10)
    op = random.choice(list(ops.keys()))
    nums = [num1, op, num2]
    return nums

def questionText(nums):
    return f"{nums[0]} {nums[1]} {nums[2]}"


def getAnswer(nums):
    if nums[1] == '+':
        answer = nums[0] + nums[2]
    if nums[1] == '-':
        answer = nums[0] - nums[2]
    if nums[1] == '*':
        answer = nums[0] * nums[2]
    return answer

class button(): 
    def __init__(self, color, x,y,width,height, text=''): 
        self.color = color 
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height 
        self.text = text 
        self.isclicked = False
    
    def draw(self,win,outline=None): 
        #Call this method to draw the button on the screen 
        if outline: 
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0) 
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0) 
        
        if self.text != '': 
            font = pygame.font.SysFont('comicsans', 60) 
            text = font.render(self.text, 1, (0,0,0)) 
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
            
    def isOver(self, pos): 
        #Pos is the mouse position or a tuple of (x,y) coordinates 
        if pos[0] > self.x and pos[0] < self.x + self.width: 
            if pos[1] > self.y and pos[1] < self.y + self.height: 
                self.isclicked = True
                return True 
            
            return False

