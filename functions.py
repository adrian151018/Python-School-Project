import pygame

def get_score(window, font, score):
    score_img = font.render("Score: " + str(round(score)), True, (0, 0, 0))
    window.blit(score_img, (0, 0))