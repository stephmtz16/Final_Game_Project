#libraries and stuff
import pygame
import math 
pygame.init()

#screen
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Pro Hockey")

#exit condition
doExit=False
#reset
reset = False
#refresh rate
clock = pygame.time.Clock()

#variables
p2Score=0
p1Score=0
#paddles
p1x=20
p1y=200
p2x=660
p2y=200
#player velocity
p1Vx = 0
p1Vy = 0
p2Vx = 0
p2Vy = 0
#puck
bx=350
by=250
#puck velocity
bVx=0
bVy=0

collision = False

#loop
while not doExit:

  #FPS
      clock.tick(90)

      for event in pygame.event.get():#checks if the user did something
        if event.type ==pygame.QUIT:#check if the user clicked close
          doExit=True #exit variable now true
      #game logic----

        if event.type == pygame.MOUSEMOTION: #check if mouse moved
            mousePos = event.pos #refreshes mouse position
            print("mouse position: (",mousePos[0]," , ",mousePos[1], ")")      
          
      ##########first player
      keys = pygame.key.get_pressed()
      if keys[pygame.K_w]:
        p1Vy=-5
      elif keys[pygame.K_s]:
        p1Vy=5
      else:
        p1Vy = 0

      if keys[pygame.K_a]:
        p1Vx=-5

      elif keys[pygame.K_d]:
        p1Vx=5
      else:
        p1Vx = 0

    ###########second player
      if keys[pygame.K_LEFT]:
        p2Vx =-5
      if keys[pygame.K_RIGHT]:
        p2Vx=5
      if keys [pygame.K_UP]:
        p2Vy=-5
      if keys[pygame.K_DOWN]:
        p2Vy=5
        
      
    #physics section------------------------------------------------    
     #update paddle position
      p1x += p1Vx
      p1y += p1Vy
      p2x += p2Vx
      p2y += p2Vy
      
      #update puck position  
      bx += bVx*.4
      by += bVy*.4

      if bx+20 < 0:#left wall 
        bx=21
        bVx *= -1
        #p1Score+=1
      if bx + 20 > 700:#right wall
        bx = 679
        bVx *=-1
        #p2Score+=1

      if by < 0:#top wall
        by =  20
        bVy *= -1
      if by + 20 > 500:#bottom wall
        by = 480
        bVy *= -1
      

      #if p1y <30 or p1y +40 >500: #or p1x >30 or p1x <670:#keeps player from going off-screen
       # p1y *=-1
      if p1y + 30>500:
          p1y = 500-30
      if p1y <30:
          p1y = 30
          
      #if by + 12>500:
          #by = 500-12
          
      #if by <12:
          #by = 12

      if p2y + 30>500:
          p2y = 500-30
      if p2y <30:
          p2y = 30
          
          #------------------------------
      if p2y + 30>500:
          p2y = 500-30
      if p2y <30:
          p2y = 30

      if p2x<380:
          p2x = 380

      if p1x-30< 0:
        p1x = 30
          
      if p2x +30> 700:
        p2x = 670
      #stop player 1 from crossing midpoint
      if p1x>320:
        p1x = 320
        


      ###############collision determines angle it was hit 


    #CIRCULAR collision between puck and paddle
      if (math.sqrt((p1x - bx)*(p1x -bx)+(p1y - by)*(p1y-by)))<32:
        bVx = p1Vx*3
        bVy = p1Vy*3
        #print ("collide")
        
      if (math.sqrt((p2x - bx)*(p2x -bx)+(p2y - by)*(p2y-by)))<32:
        bVx = p2Vx*3
        bVy = p2Vy*3
        #angle = acos((ra^2+rb^2-c^2)/(2*ra*rb)) 
      
      #condition to reset after you score
      #if bx
      #rendering----
      screen.fill((0,0,255))#wipe screen black
      pygame.draw.line(screen, (255,255,255),[349,0],[349,500],10)
      #pygame.draw.rect(screen, (255,255,255),(p1x,p1y,30,30))#player1
      pygame.draw.circle(screen, (0,255,0),[p1x,p1y],30)#new player 1
      pygame.draw.circle(screen, (0,255,0),[p2x,p2y],30)#new player2
      
      pygame.draw.rect(screen, (255, 255, 255), (-110, 170, 150, 150),10)#left goal
      pygame.draw.line(screen, (0,0,0),[0,175],[0,313],20)#actual goal
      
      pygame.draw.rect(screen, (255, 255, 255), (660, 170, 150, 150),10)#right goal
      pygame.draw.line(screen, (0,0,0),[695,175],[695,313],10)#actual goal
      
      pygame.draw.circle(screen,(255,255,255),(350,250),60,10)
      #pygame.draw.rect(screen, (255,255,255),(p2x,p2y,30,30))#player2

      pygame.draw.circle(screen, (0,0,0),(int(bx),int(by)),12)#puck
      
      
      font = pygame.font.Font(None, 74)
      text = font.render(str(p1Score),1,(255,255,255))
      screen.blit(text,(250,10))
      text = font.render(str(p2Score),1,(255,255,255))
      screen.blit(text,(420,10))
      pygame.display.flip()#updates game
pygame.quit()#closes "game"