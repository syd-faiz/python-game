import pygame
from pygame.locals import *
import time
import random

BACKGROUND =(255,255,255)
SIZE = 13

class apple:
    def __init__(self,parent_screen):
        self.parent_screen= parent_screen
        self.image=pygame.image.load("resourses/apple.png").convert()  
        self.x=SIZE * 3
        self.y=SIZE * 3

    def draw(self):
        self.parent_screen.blit(self.image,(self.x,self.y))
        pygame.display.flip()
    def move(self):
        self.x = random.randint(0,22) * SIZE
        self.y = random.randint(0,17) * SIZE


class Snake:
     def __init__(self,parent_screen,  length):
        self.length = length
        self.parent_screen= parent_screen
        self.block=pygame.image.load("resourses/block.png").convert()
        self.x=[SIZE] * length
        self.y=[SIZE] * length
        self.direction ='down'

     def increase_length(self):
         self.length+=1
         self.x.append(-1)
         self.y.append(-1)
        

     def draw(self):
          self.parent_screen.fill((255,255,255))
          for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
          pygame.display.flip()

     def move_left(self):
         self.direction ='left'
       
     def move_right(self):
         self.direction='right'
         
     def move_up(self):
         self.direction = 'up'
          
     def move_down(self):
         self.direction = 'down'

     def walk(self):
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]          
        if(self.direction == 'left'):
            self.x[0] -=SIZE
        if(self.direction == 'right'):
            self.x[0] +=SIZE
        if(self.direction == 'up'):
            self.y[0] -=SIZE
        if(self.direction == 'down'):
            self.y[0]+=SIZE

        self.draw()
class Game:
     def __init__(self):
          pygame.init()
          self.surface=pygame.display.set_mode((1000,800))
          self.surface.fill(BACKGROUND)
          self.snake=Snake(self.surface,10)
          self.snake.draw()
          self.apple =apple(self.surface)
          self.apple.draw()
    
     def reset(self):
        self.snake = Snake(self.surface)
        self.apple = apple(self.surface)

     def is_collision(self,x1,y1,x2,y2):
          if(x1>=x2 and x1 < x2 +SIZE):
             if(y1>=y2 and y1 < y2 +SIZE):
                 return True
          return False

              
         
     def play(self):
         self.snake.walk()
         self.apple.draw()
         self.display_score()
         pygame.display.flip()
         #with apple
         if self.is_collision(self.snake.x[0],self.snake.y[0], self.apple.x,self.apple.y):
             self.snake.increase_length()
             self.apple.move()
         #with itself
         for i in range(3,self.snake.length):
             if self.is_collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                 raise "gameover"
                 


     def display_score(self):
         font = pygame.font.SysFont('calibri',30)
         score = font.render(f"Score:{self.snake.length-6}",True,(0,0,0))  
         self.surface.blit(score,(800,10))
    
     def show_game_over(self):
         self.surface.fill((BACKGROUND))
         font = pygame.font.SysFont('calibri',30)
         line1 = font.render(f" Your Score:{self.snake.length-6}",True,(0,0,0))  
         self.surface.blit(line1,(200,300))
         line2 = font.render("Press Enter to play again.Esc to exit",True,(0,0,0))  
         self.surface.blit(line2,(200,350))
         pygame.display.flip()

       


     def run(self):

          
          running=True
          while running:
              for event in pygame.event.get():
                  if event.type==KEYDOWN:
                     if event.key==K_ESCAPE:
                        running=False
                     if event.key==K_UP:
                         self.snake.move_up()
                     if event.key==K_DOWN:
                         self.snake.move_down()
                     if event.key==K_LEFT:
                         self.snake.move_left()
                     if event.key==K_RIGHT:
                         self.snake.move_right()

        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pause = False

                    if not pause:
                        if event.key == K_LEFT:
                            self.snake.move_left()

                        if event.key == K_RIGHT:
                            self.snake.move_right()

                        if event.key == K_UP:
                            self.snake.move_up()

                        if event.key == K_DOWN:
                            self.snake.move_down()

                elif event.type == QUIT:
                    running = False
            try:

                if not pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(.30)


if __name__=="__main__":
    game=Game()
    game.run()
    

   


