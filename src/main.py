import pygame
import math
from random import randint
import sys

def display_score():
    current_time = math.floor((pygame.time.get_ticks() - start_time) /1000)
    score_surf = game_font.render(f"Score: {current_time}", False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

pygame.init()

screen = pygame.display.set_mode((800, 400))  
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

game_font = pygame.font.Font('resources/font/Pixeltype.ttf', 50)
start_time = 0

game_active = False
score = 0
sky_surface = pygame.image.load('resources/graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('resources/graphics/ground.png').convert_alpha()

score_surf = game_font.render("Score: ", False, (64, 64, 64))
score_rect = score_surf.get_rect(center = (400, 50))

# Obstacles
snail_surf = pygame.image.load('resources/graphics/snail/snail1.png').convert_alpha()
fly_surf = pygame.image.load('resources/graphics/Fly/Fly1.png').convert_alpha()

obstacle_rect_list = []

player_surf = pygame.image.load('resources/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0

player_stand = pygame.image.load('resources/graphics/Player/player_stand.png')
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

game_title_text = game_font.render("PIXEL RUNNER", False, (111,196, 169))
game_over_text_rect = game_title_text.get_rect(center = (400, 50))
continue_text = game_font.render("Press any keyboard key to start!", False, (111,196, 169))
continue_text_rect = continue_text.get_rect(center = (400, 350))

# Timer
obstacle_timer = pygame.USEREVENT + 1

pygame.time.set_timer(obstacle_timer, 900)

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
            if event.type == pygame.KEYDOWN and player_rect.bottom >= 300:
                if event.key == pygame.K_SPACE:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                game_active = True
                start_time = pygame.time.get_ticks()

        if event.type == obstacle_timer and game_active:
            if randint(0,2):
                obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900,1100), 300)))
            else:
                obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900,1100), 210)))

    if game_active:
        # background
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0, 300))
        # pygame.draw.rect(screen, "#c0e8ec", score_rect)
        # screen.blit(score_surf, score_rect)
        score = display_score()


        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # Obstacle Movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # Collisions
        game_active = collisions(player_rect, obstacle_rect_list)

    else:
        screen.fill((94, 129, 162))
        score_message = game_font.render(f"Your score: {score}", False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (400, 330))
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0

        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_title_text, game_over_text_rect)

        if score != 0:
            screen.blit(score_message, score_message_rect)
        else:
            screen.blit(continue_text, continue_text_rect)
    
    pygame.display.update()
    clock.tick(60)
