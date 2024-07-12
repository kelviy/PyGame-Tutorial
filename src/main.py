import pygame


def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 400))  
    pygame.display.set_caption("Runner")
    clock = pygame.time.Clock()
    game_font = pygame.font.Font('resources/font/Pixeltype.ttf', 50)

    sky_surface = pygame.image.load('resources/graphics/Sky.png').convert_alpha()
    ground_surface = pygame.image.load('resources/graphics/ground.png').convert_alpha()
    
    score_surf = game_font.render("My game", False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))

    snail_surf = pygame.image.load('resources/graphics/snail/snail1.png').convert_alpha()
    snail_rect = snail_surf.get_rect(midbottom = (600, 300))

    player_surf = pygame.image.load('resources/graphics/Player/player_walk_1.png').convert_alpha()
    player_rect = player_surf.get_rect(midbottom = (80, 300))
    player_gravity = 0

    # main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
            if event.type == pygame.KEYDOWN and player_rect.bottom >= 300:
                if event.key == pygame.K_SPACE:
                    player_gravity = -20
        # background
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0, 300))
        pygame.draw.rect(screen, "#c0e8ec", score_rect)
        screen.blit(score_surf, score_rect)

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
            pygame.quit()
            return

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()