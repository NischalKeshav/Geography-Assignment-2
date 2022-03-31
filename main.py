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



class Img:
  def __init__(self,img,x,y,rotate = 0):
    self.img = img
    self.pos = (x,y)
    pygame.transform.rotate(self.img,rotate)
  def draw(self):
    Screen.blit(self.img,self.pos)



  
    
#images for animation 1
Rect1 = Rect(0,0,300,600,7,0) 
Rect2 = Rect(0,0,600,300,0,7)
Rect3 = Rect(300,0,300,600,-7,0)
Rect4  = Rect(0,300,600,300,0,-7)



# Animation 1
for i in range(300):
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
# Arrow = Img(ArrowIMG,300,200,rotate=270)
# World = Img(World,200,80) 








# for i in range(500):
#   Screen.fill(BG)
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       sys.exit()
#   Arrow.draw()
#   World.draw
#   Screen.blit
#   pygame.display.update()














sys.exit()
  
  
  