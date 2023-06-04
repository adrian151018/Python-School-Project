import pygame

def game_over(screen, font, score):
    game_over_surface = pygame.Surface((600, 300))
    game_over_surface.fill((255, 0, 0))  # Red color for the game over rectangle

    game_over_text = font.render("Game Over", True, (255, 255, 255))  # White color for the text
    game_over_text_rect = game_over_text.get_rect(center = (game_over_surface.get_width() // 2, game_over_surface.get_height() // 2 - 50))

    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    score_text_rect = score_text.get_rect(center = (game_over_surface.get_width() // 2, game_over_surface.get_height() // 2 + 50))

    game_over_surface.blit(game_over_text, game_over_text_rect)
    game_over_surface.blit(score_text, score_text_rect)

    screen.blit(game_over_surface, (200, 100))
    pygame.display.update()

def get_score(window, font, score):
    score_img = font.render("Score: " + str(score), True, (0, 0, 0))
    window.blit(score_img, (0, 0))