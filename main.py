import pygame
import sys
import random

#inicial sets
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("snake game")
mainClock = pygame.time.Clock()
FPS = 400
GRAY = (100, 100, 100)
BLACK = (0,0,0)
WHITE = (255,255,255)
screen.fill("white")
font = pygame.font.SysFont("arial", 25, True, False)
list_snake = []
list_snake3 = []
score = 0
cor_x = (random.randint(8,24))*25
cor_y = (random.randint(8,24))*25
apple_x = (random.randint(8,24))*25
apple_y = (random.randint(8,24))*25
direction = (random.randint(1,4))

def gameover():
    print("GAMEOVER")
    print(score)
    pygame.quit()
    sys.exit()

destroyer = pygame.draw.rect(screen,WHITE,(-25,-25,25,25))
apple = pygame.draw.rect(screen,BLACK,(apple_x,apple_y,25,25))

borda1 = pygame.draw.rect(screen, BLACK, (0,0,25,800))
borda2 = pygame.draw.rect(screen, BLACK, (0,0,800,25))
borda3 = pygame.draw.rect(screen, BLACK, (775,0,25,800))
borda4 = pygame.draw.rect(screen, BLACK, (0,775,800,25))

snake_length = 3

#bug_solver
bug_solver23124 = 20
bug_solver23124_cor_x = cor_x
bug_solver23124_cor_y = cor_y

while True:
    #bug_solver
    if bug_solver23124 > 0:
        bug_solver23124 -= 1
        pygame.draw.rect(screen,WHITE,(bug_solver23124_cor_x,bug_solver23124_cor_y,25,25))

    player = pygame.draw.rect(screen,BLACK,(cor_x,cor_y,25,25))

    #direction
    key = pygame.key.get_pressed()
    if key [pygame.K_s]:
        if direction == 3:
            direction = (3)
        else:    
            direction = (1)         
    if key [pygame.K_a]:
        if direction == 4:
            direction = (4)
        else:    
            direction = (2)   
    if key [pygame.K_w]:
        if direction == 1:
            direction = (1)
        else:    
            direction = (3)
    if key [pygame.K_d]:
        if direction == 2:
            direction = (2)
        else:    
            direction = (4)
        
    #apple things
    if apple.colliderect(player):
        apple_x = (random.randint(1,30))*25
        apple_y = (random.randint(1,30))*25
        score += 1
        pygame.draw.rect(screen,WHITE,(25,25,200,50))
        snake_length += 1

    apple = pygame.draw.rect(screen,BLACK,(apple_x,apple_y,25,25))

    mainClock.tick(FPS)
    if direction == 1:
        pygame.time.wait(100)
        cor_y += 25
    if direction == 2:
        pygame.time.wait(100)
        cor_x -= 25
    if direction == 3:
        pygame.time.wait(100)
        cor_y -= 25
    if direction == 4:
        pygame.time.wait(100)
        cor_x += 25

    list_snake.append(cor_x)
    list_snake.append(cor_y)
    list_snake2 = []
    list_snake2.append(cor_x)
    list_snake2.append(cor_y)
    list_snake3.append(list_snake2)

    if list_snake3.count(list_snake2) > 1:
        gameover()

    if len(list_snake) > (snake_length*2)+2:
        destroyer = pygame.draw.rect(screen,WHITE,(list_snake[0], list_snake[1],25,25))
        del list_snake[1]
        del list_snake[0]

    if len(list_snake3) > (snake_length):
        del list_snake3[0]

    #gameover colisions
    if player.colliderect(borda1):
        gameover()
    if player.colliderect(borda2):
        gameover()
    if player.colliderect(borda3):
        gameover()
    if player.colliderect(borda4):
        gameover()
    if player.colliderect(destroyer):
        gameover()

    #canvas 
    mensagem = f"score: {score}"
    screen.blit((font.render(mensagem, True, GRAY)), (35, 35))

    #if event == quit, pygame.quit, sys.exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    mainClock.tick(FPS)
    pygame.display.update()

