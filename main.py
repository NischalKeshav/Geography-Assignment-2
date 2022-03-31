import pygame,sys
pygame.init()


Screen =  pygame.display.set_mode((600,600))
BG = (255,255,255)
clock = pygame.time.Clock()



###################Images#######################
Europe = pygame.image.load("Europe.png")
World = pygame.image.load("world.png")
ArrowIMG = pygame.image.load("arrow.png")
tankIMG = pygame.image.load("tank.png")
stuff = pygame.image.load("Stuff.png")
ArrowIMG = pygame.transform.rotozoom(ArrowIMG,50,.8)


listOfRects = []
class Rect:
  def __init__ (self,x,y,width,height,ymove,xmove):
    global listOfRects
    self.x = x
    self.y = y
    self.width = width
    self.height = height 
    self.Move = (xmove,ymove)

    listOfRects.append(self)
  def draw(self):
    pygame.draw.rect(Screen,(150,255,200),(self.x-1,self.y-1,self.x+self.width-1,self.y+self.height-1))
    pygame.draw.rect(Screen,(0,0,00),(self.x,self.y,self.x+self.width,self.y+self.height),3)
    

  def move(self):
    self.x += self.Move[0]
    self.y +=self.Move[1]



class Img:
  def __init__(self,img,x,y,rotate = 0):
    self.img = img
    self.pos = (x,y)
    
    self.img = img
  def draw(self):
    Screen.blit(self.img,self.pos)



  
    
#images for animation 1
Rect1 = Rect(0,0,300,600,7,0) 
Rect2 = Rect(0,0,600,300,0,7)
Rect3 = Rect(300,0,300,600,-7,0)
Rect4  = Rect(0,300,600,300,0,-7)



# Animation 1
for i in range(120):
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

#Images for Animation 2


  
Arrow = Img(ArrowIMG,300,270,rotate=90)
World = Img(World,150,80) 
Stuff = Img(stuff,-100,100)

list = []




for i in range(1000):
  Screen.fill(BG)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

  Screen.blit(Europe,(200,350))
  Arrow.draw()
  World.draw()
  
  Stuff.draw()
  pygame.display.update()
  clock.tick(60)


#sys.exit()
  
  
  