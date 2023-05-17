import pygame

WIDTH, HEIGHT = 1000, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

def main():
    clock = pygame.time.Clock()
    running = True
    while(running):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()