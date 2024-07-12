import pygame
import math

pygame.init()

screen = pygame.display.set_mode((800, 400))  
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

game_font = pygame.font.Font('resources/font/Pixeltype.ttf', 50)
start_time = 0

def display_score():
    current_time = math.floor((pygame.time.get_ticks() - start_time) /1000)
    score_surf = game_font.render(f"Score: {current_time}", False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def main():

    game_active = False
    global score
    score = 0
    sky_surface = pygame.image.load('resources/graphics/Sky.png').convert_alpha()
    ground_surface = pygame.image.load('resources/graphics/ground.png').convert_alpha()
    
    score_surf = game_font.render("Score: ", False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))

    snail_surf = pygame.image.load('resources/graphics/snail/snail1.png').convert_alpha()
    snail_rect = snail_surf.get_rect(bottomleft = (800, 300))

    player_surf = pygame.image.load('resources/graphics/Player/player_walk_1.png').convert_alpha()
    player_rect = player_surf.get_rect(midbottom = (80, 300))
    player_gravity = 0

    player_stand = pygame.image.load('resources/graphics/Player/player_stand.png')
    player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
    player_stand_rect = player_stand.get_rect(center = (400, 200))

    game_title_text = game_font.render("PIXEL RUNNER", False, (111,196, 169))
    game_over_text_rect = game_title_text.get_rect(center = (400, 50))
    continue_text = game_font.render("Press any keyboard key to restart!", False, (111,196, 169))
    continue_text_rect = continue_text.get_rect(center = (400, 350))

    # main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if game_active:
                if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:
                    if player_rect.collidepoint(event.pos):
                        player_gravity = -20
                if event.type == pygame.KEYDOWN and player_rect.bottom >= 300:
                    if event.key == pygame.K_SPACE:
                        player_gravity = -20
            else:
                if event.type == pygame.KEYDOWN:
                    snail_rect.left = 800
                    game_active = True
                    global start_time
                    start_time = pygame.time.get_ticks()

        if game_active:
            # background
            screen.blit(sky_surface, (0,0))
            screen.blit(ground_surface, (0, 300))
            # pygame.draw.rect(screen, "#c0e8ec", score_rect)
            # screen.blit(score_surf, score_rect)
            score = display_score()

            snail_rect.x -= 4
            if snail_rect.right <= 0:
                snail_rect.left = 800
            
            screen.blit(snail_surf, snail_rect)

            # Player
            player_gravity += 1
            player_rect.y += player_gravity
            if player_rect.bottom >= 300:
                player_rect.bottom = 300
            screen.blit(player_surf, player_rect)

            # Collisions
            if snail_rect.colliderect(player_rect):
                game_active = False
        else:
            screen.fill((94, 129, 162))
            score_message = game_font.render(f"Your score: {score}", False, (111, 196, 169))
            score_message_rect = score_message.get_rect(center = (400, 330))

            screen.blit(player_stand, player_stand_rect)
            screen.blit(game_title_text, game_over_text_rect)

            if score != 0:
                screen.blit(score_message, score_message_rect)
            else:
                screen.blit(continue_text, continue_text_rect)
        
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()