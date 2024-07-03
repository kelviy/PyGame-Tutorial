import pygame


def main():
    pygame.init()

    screen = pygame.display.set_mode((1240, 720))
    pygame.display.set_caption("Runner")
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()