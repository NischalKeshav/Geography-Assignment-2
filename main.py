import pygame,sys
pygame.init()


Screen =  pygame.display.set_mode((600,600))
BG = (255,255,255)
clock = pygame.time.Clock()



###################Images#######################
Europe = pygame.image.load("Europe.png")
World = pygame.image.load("world.png")
Arrow = pygame.image.load("arrow.png")

listOfRects = []
class Rect:
  def __init__ (self,x,y,width,height,ymove,xmove):
    global listOfRects
    self.x = x
    self.y = y
    self.width = width
    self.height = height 
    self.Move = (xmove,ymove)
    print(self)
    listOfRects.append(self)
  def draw(self):
    pygame.draw.rect(Screen,(150,255,200),(self.x-1,self.y-1,self.x+self.width-1,self.y+self.height-1))
    pygame.draw.rect(Screen,(0,0,00),(self.x,self.y,self.x+self.width,self.y+self.height),3)
    

  def move(self):
    self.x += self.Move[0]
    self.y +=self.Move[1]







class arrow:
  def __init__(x,y):
    global Arrow
    self.img = Arrow
    self.x = x
    self.y = y

    

Rect1 = Rect(0,0,300,600,7,0) 
Rect2 = Rect(0,0,600,300,0,7)
Rect3 = Rect(300,0,300,600,-7,0)
Rect4  = Rect(0,300,600,300,0,-7)




for i in range(400):
  Screen.fill(BG)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
  
  Screen.blit(Europe,(200,350))
  for i in listOfRects:
    i.move()
    i.draw()
  pygame.display.update()
  clock.tick(60)


while 1:
  









sys.exit()
  
  
  