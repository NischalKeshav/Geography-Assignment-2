import pygame,sys
pygame.init()


Screen =  pygame.display.set_mode((600,600))
BG = (0,0,0)
clock = pygame.time.Clock()



###################Images#######################
Europe = pygame.image.load("Europe.png")
World = pygame.image.load("world.png")




while 1:
  Screen.fill(BG)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
  
  Screen.blit(Europe,(100,100))
  pygame.display.update()
  clock.tick(120)
  
  