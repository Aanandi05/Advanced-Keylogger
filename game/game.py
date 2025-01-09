#Change the content. Maybe download entirely new background and stuff.Or try resizing the images or align the entire thing in the center withou it covering the entire screen.
import pygame
import pygame.mixer
from sys import exit
from random import randint



def display_score():

    global start_time

    current_time= (pygame.time.get_ticks()//1000) - start_time
    score_surface= font.render( f'Score: {current_time}', False, "pink")
    score_surface_rect = score_surface.get_rect(center = (900, 30))
    screen.blit(score_surface, score_surface_rect)
    return current_time

def obstacle_move(obstacle_list):
    if obstacle_list:
        for obstacle_rect , obstacle_type in obstacle_rect_list:
            obstacle_rect.x -= obstacle_speed

            if obstacle_type == 'bee':
                screen.blit(bee, obstacle_rect)
            elif obstacle_type == 'snake':
                screen.blit(snake, obstacle_rect)
            else:
                screen.blit(tree, obstacle_rect)

        obstacle_list = [(obstacle_rect, obstacle_type) for obstacle_rect, obstacle_type in obstacle_list if obstacle_rect.x > -100]

        return obstacle_list
    else: return []

def collision(cat, obstacle, cat_margin):
    obstacle_margin= 50
    if obstacle:
        for obstacle_rect, obstacle_type in obstacle:
            if cat.inflate(-cat_margin, -cat_margin).colliderect(obstacle_rect.inflate(-obstacle_margin, -obstacle_margin)): return False
    return True

pygame.init()
screen_width = pygame.display.Info().current_w
screen_height = pygame.display.Info().current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

score = 0
start_time = 0


pygame.display.set_caption("Catnner")
clock = pygame.time.Clock()
font= pygame.font.Font("C:/Users/aanan/OneDrive/Desktop/Game-20230801T162858Z-001/Game/Things/DiloWorld-mLJLv.ttf", 50)
game_active= False

cat_margin = 60

OBSTACLESPEED = 5



sky= pygame.image.load("C:/Users/aanan/OneDrive/Desktop/Game-20230801T162858Z-001/Game/Things/sky.png").convert()
ground= pygame.image.load("C:/Users/aanan/OneDrive/Desktop/Game-20230801T162858Z-001/Game/Things/ground.png").convert()


#Obstacles

tree= pygame.image.load("C:/Users/aanan/OneDrive/Desktop/Game-20230801T162858Z-001/Game/Things/tree-removebg-preview.png").convert_alpha()
bee = pygame.image.load("C:/Users/aanan/OneDrive/Desktop/Game-20230801T162858Z-001/Game/Things/bee-removebg-preview.png").convert_alpha()
snake = pygame.image.load("C:/Users/aanan/OneDrive/Desktop/Game-20230801T162858Z-001/Game/Things/snake-removebg-preview.png").convert_alpha()

obstacle_rect_list = []


cat= pygame.image.load("C:/Users/aanan/OneDrive/Desktop/Game-20230801T162858Z-001/Game/Things/cat-removebg-preview.png").convert_alpha()
cat_rect= cat.get_rect(bottomleft = (80, 500 ))
cat_gravity = 0

close_button_image = pygame.image.load("C:/Users/aanan/OneDrive/Desktop/Game-20230801T162858Z-001/Game/Things/Button-removebg-preview .png").convert_alpha()
close_button_rect = close_button_image.get_rect(bottomleft=( 1870, 30))


#intro
player_stand = pygame.image.load("C:/Users/aanan/OneDrive/Desktop/Game-20230801T162858Z-001/Game/Things/cat_stand-removebg-preview.png").convert_alpha()
player_stand = pygame.transform.scale(player_stand,(400, 400))
player_stand_rect= player_stand.get_rect(center= (900, 500))

game_name = font.render('R u n n e r   C a t', False, "pink")
game_name_rect = game_name.get_rect(center = (900, 200))

game_message = font.render("P r e s s   s p a c e   t o   r u n  !", False, "magenta")
game_message_rect= game_message.get_rect(center = (900, 750))

#Timer
obstacle_timer = pygame.USEREVENT + 5
pygame.time.set_timer(obstacle_timer, 900)

#Audios
pygame.mixer.init()
background_sound = pygame.mixer.Sound("C:/Users/aanan/OneDrive/Desktop/Game-20230801T162858Z-001/Game/Things/Space-Jazz.mp3")
background_sound.set_volume(2.0)
jump_sound = pygame.mixer.Sound("C:/Users/aanan/OneDrive/Desktop/Game-20230801T162858Z-001/Game/Things/TunePocket-Basketball-Ball-Bounce-Single-1-Preview.mp3")
jump_sound.set_volume(5.0)
jump_channel = pygame.mixer.Channel(1)

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and cat_rect.bottom >= 715 :
                    jump_channel.play(jump_sound)
                    cat_gravity = -13

        if event.type == pygame.MOUSEBUTTONDOWN:
            if close_button_rect.collidepoint(event.pos):
                pygame.quit()
                exit()


        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if not game_active:
                    game_active = True
                    start_time = pygame.time.get_ticks()//1000

        if event.type == obstacle_timer and game_active:
            if randint (0, 4)==0:
                obstacle_rect_list.append((snake.get_rect(topleft=(randint(900, 1100 ), 670)), 'snake'))
            elif randint(0, 1):
                obstacle_rect_list.append((bee.get_rect(bottomleft = (randint(900, 1100), 670)), 'bee'))
            else:
                obstacle_rect_list.append((tree.get_rect(topleft = (randint(900, 1100), 695)), 'tree'))

    if game_active:
        screen.blit(sky, (0, 0))
        screen.blit(ground, (0,770 ))


        score= display_score()


        #Cat
        cat_gravity +=1
        cat_rect.y += cat_gravity
        if cat_rect.bottom >= 760 : cat_rect.bottom = 760
        screen.blit(cat,cat_rect)


        #obstacle spped
        current_time = pygame.time.get_ticks() // 1000 -start_time
        obstacle_speed = OBSTACLESPEED + current_time // 5




        game_active = collision(cat_rect, obstacle_rect_list, cat_margin)

        #obstacle move
        obstacle_rect_list = obstacle_move(obstacle_rect_list)

        background_sound.play(-1)

    else:
        screen.fill("#301934")
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()

        score_message = font.render(f'Your Score: {score}', False, "pink")
        score_message_rect = score_message.get_rect(center=(900, 800))
        screen.blit(game_name, game_name_rect)
        background_sound.stop()
        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:

            screen.blit(score_message, score_message_rect)
    screen.blit(close_button_image, close_button_rect)
    pygame.display.update()
    clock.tick(60)

