import pygame,sys
from pygame import mixer
pygame.init()
mixer.init()
FONT = pygame.font.Font('arial.ttf', 12)
Screen =  pygame.display.set_mode((710,700))
BG = (255,255,255)
clock = pygame.time.Clock()
pygame.display.set_caption("Europe 20th Century")




mixer.music.load("piano.wav")
mixer.music.play()
###################Images#######################
Europe = pygame.image.load("Europe.png")
World = pygame.image.load("world.png")
ArrowIMG = pygame.image.load("arrow.png")
tankIMG = pygame.image.load("tank.png")
stuff = pygame.image.load("Stuff.png")
ArrowIMG = pygame.transform.rotozoom(ArrowIMG,7,1)
World = pygame.transform.rotozoom(World,0,1.3)




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
Rect4 = Rect(0,0,350,700,10,0) 
Rect2 = Rect(0,0,700,350,-10,0)
Rect3  = Rect(350,0,700,350,0,-10)
Rect1 = Rect(350,0,350,700,0,10)


Arrow = Img(ArrowIMG,283,210,rotate=40)
World = Img(World,150,0) 
Stuff = Img(stuff,-80,300)

FONT1 = pygame.font.Font("arial.ttf",24)



a = True
# Opening animation
while a:
  Screen.fill(BG)
  for i in listOfRects:
    i.draw()
  Screen.blit(FONT1.render("Europe in the 20th Century ",4,(255,0,180)),(50,50))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN or event.type== pygame.KEYDOWN:
      a = False
  pygame.display.update()
  clock.tick(60)




# Animation 1
for i in range(120):
  Screen.fill(BG)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
  Screen.blit(Europe,(200,350))
  Arrow.draw()
  World.draw()
  
  Stuff.draw()
  
  for i in listOfRects:
    i.move()
    i.draw()
  pygame.display.update()
  clock.tick(60)

#Images for Animation 2


  


list = []




caption1 = """  In the 1900s Europe had incredible 
influence on almost every inch 
of the world. Whenever a Major
event occured in Europe almost all
nations were affected, whether directly
due to Europe's immense  empires or 
indirectly due to trade, allyship, 
or other forms of movement.

"""
caption2 = """  For example, In both World Wars people, ideas, and 
resources(espicially weapons) were moved around.
With the end of the Second  World War  there 
was a large change in goverments with
democracy and the fall of  Europe's Empire. 
"""


def render_multi_line(text, x, y, fsize):
  global FONT      
  hecolor = (0,0,0)
  lines = text.splitlines()
  for i, l in enumerate(lines):
            Screen.blit(FONT.render(l, 0.0001, hecolor), (x, y + (fsize)*i))


for i in range(len(caption1)):
  
  Screen.fill((255,255,255))
  World.draw()
  render_multi_line(caption1[:i],10,100,18)
  
  pygame.display.update(10,100,210,200)
  clock.tick(60)
for i in range(len(caption1)):
  Screen.fill((255,255,255))
  render_multi_line(caption2[:i],200,520,18)
  pygame.display.update(200,510,400,700)
  clock.tick(60)

#sys.exit()  