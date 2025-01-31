import pygame
import math
from random import randint, choice
import sys

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('resources/graphics/Player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('resources/graphics/Player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('resources/graphics/Player/jump.png').convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound("resources/audio/jump.mp3")
        self.jump_sound.set_volume(0.5)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity

        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'fly':
            fly_frame_1 = pygame.image.load('resources/graphics/Fly/Fly1.png').convert_alpha()
            fly_frame_2 = pygame.image.load('resources/graphics/Fly/Fly2.png').convert_alpha()
            self.frames = [fly_frame_1, fly_frame_2]
            y_pos = 210
        else:
            snail_frame_1 = pygame.image.load('resources/graphics/snail/snail1.png').convert_alpha()
            snail_frame_2 = pygame.image.load('resources/graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_frame_1, snail_frame_2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))
    
    def animation_state(self):
        self.animation_index += 0.1

        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

def display_score():
    current_time = math.floor((pygame.time.get_ticks() - start_time) /1000)
    score_surf = game_font.render(f"Score: {current_time}", False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

# def obstacle_movement(obstacle_list):
#     if obstacle_list:
#         for obstacle_rect in obstacle_list:
#             obstacle_rect.x -= 5

#             if obstacle_rect.bottom == 300:
#                 screen.blit(snail_surf, obstacle_rect)
#             else:
#                 screen.blit(fly_surf, obstacle_rect)

#         obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

#         return obstacle_list
#     else:
#         return []

# def collisions(player, obstacles):
#     if obstacles:
#         for obstacle_rect in obstacles:
#             if player.colliderect(obstacle_rect):
#                 return False
#     return True

# def player_animation():
#     # player walking animation if the player is on floor
#     # display the jump surface when player is not on floor

#     global player_surf, player_index

#     if player_rect.bottom < 300:
#         player_surf = player_jump
#     else:
#         player_index += 0.1
#         if player_index >= len(player_walk):
#             player_index = 0
#         player_surf = player_walk[int(player_index)]

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        player.sprite.gravity = 0
        player.sprite.rect.midbottom = (80, 300)
        return False
    else:
        return True

pygame.init()

screen = pygame.display.set_mode((800, 400))  
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

game_font = pygame.font.Font('resources/font/Pixeltype.ttf', 50)
start_time = 0

# Music
bg_music = pygame.mixer.Sound('resources/audio/music.wav')
bg_music.play(loops = -1)

game_active = False
score = 0
sky_surface = pygame.image.load('resources/graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('resources/graphics/ground.png').convert_alpha()

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

score_surf = game_font.render("Score: ", False, (64, 64, 64))
score_rect = score_surf.get_rect(center = (400, 50))



# Obstacles
#Snail
# snail_frame_1 = pygame.image.load('resources/graphics/snail/snail1.png').convert_alpha()
# snail_frame_2 = pygame.image.load('resources/graphics/snail/snail2.png').convert_alpha()
# snail_frames = [snail_frame_1, snail_frame_2]
# snail_index = 0
# snail_surf = snail_frames[snail_index]

# Fly
# fly_frame_1 = pygame.image.load('resources/graphics/Fly/Fly1.png').convert_alpha()
# fly_frame_2 = pygame.image.load('resources/graphics/Fly/Fly2.png').convert_alpha()
# fly_frames = [fly_frame_1, fly_frame_2]
# fly_index = 0
# fly_surf = fly_frames[fly_index]

# obstacle_rect_list = []

# player_walk_1 = pygame.image.load('resources/graphics/Player/player_walk_1.png').convert_alpha()
# player_walk_2 = pygame.image.load('resources/graphics/Player/player_walk_2.png').convert_alpha()
# player_walk = [player_walk_1, player_walk_2]
# player_index = 0
# player_jump = pygame.image.load('resources/graphics/Player/jump.png').convert_alpha()

# player_surf = player_walk[player_index]
# player_rect = player_surf.get_rect(midbottom = (80, 300))
# player_gravity = 0

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

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)


# main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if game_active:
            pass
        #     if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:
        #         if player_rect.collidepoint(event.pos):
        #             player_gravity = -20
        #     if event.type == pygame.KEYDOWN and player_rect.bottom >= 300:
        #         if event.key == pygame.K_SPACE:
        #             player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                game_active = True
                start_time = pygame.time.get_ticks()

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail',])))
                # if randint(0,2):
                #     obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900, 1100), 300)))
                # else:
            #     #     obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900, 1100), 210)))
            # if event.type == snail_animation_timer:
            #     if snail_index == 0:
            #         snail_index = 1
            #     else:
            #         snail_index = 0
            #     snail_surf = snail_frames[snail_index]

            # if event.type == fly_animation_timer:
            #     if fly_index:
            #         fly_index = 0
            #     else:
            #         fly_index = 1
            #     fly_surf = fly_frames[fly_index]

        


    if game_active:
        # background
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0, 300))
        # pygame.draw.rect(screen, "#c0e8ec", score_rect)
        # screen.blit(score_surf, score_rect)
        score = display_score()


        # Player
        # player_gravity += 1
        # player_rect.y += player_gravity
        # if player_rect.bottom >= 300:
        #     player_rect.bottom = 300
        # player_animation()
        # screen.blit(player_surf, player_rect)

        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        game_active = collision_sprite()

        # Obstacle Movement
        # obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # Collisions
        # game_active = collisions(player_rect, obstacle_rect_list)

    else:
        screen.fill((94, 129, 162))
        score_message = game_font.render(f"Your score: {score}", False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (400, 330))
        # obstacle_rect_list.clear()
        # player_rect.midbottom = (80, 300)
        # player_gravity = 0

        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_title_text, game_over_text_rect)

        if score != 0:
            screen.blit(score_message, score_message_rect)
        else:
            screen.blit(continue_text, continue_text_rect)
    
    pygame.display.update()
    clock.tick(60)
