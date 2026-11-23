import pygame
import sys
import os
from common.constants import *

from games.snake.main import run_snake
from games.flappy.main import run_flappy
from games.shooter.main import run_shooter

pygame.init()

# O Launcher usa suas proprias dimensoes correspondentes a proporcao de bg-new.png (16:9)
LAUNCHER_W, LAUNCHER_H = 800, 450

screen = pygame.display.set_mode((LAUNCHER_W, LAUNCHER_H))
clock = pygame.time. Clock()

base = os.path.abspath(os.path. join(os.path.dirname(_file ), "assets/launcher"))
bg = pygame. image. load(os.path. join(base, "bg-new.png"))
bg = pygame. transform.scale(bg, (LAUNCHER_W, LAUNCHER_H) )

# Tamanho original da imagem para cálculos de proporção
IMG_W, IMG_H = 1672, 941
SX = LAUNCHER_W / IMG_W
sy = LAUNCHER_H / IMG_H

Posições dos cards mapeadas do layout original bg-new.png (verificadas visualmente)
# Todos os 3 cards têm o mesmo tamanho; ordem: Flappy (esquerda), Shooter (centro), Snake (direita)
def scaled_rect(x, y, w, h):
    return pygame.Rect(int(x * sx), int(y * sy), int(w * sx), int(h*sy))

CARD_W, CARD_H = 312, 358
CARD_Y = 430

card_flappy = scaled_rect(342, CARD_Y, CARD_W, CARD_H)
card_shooter = scaled_rect(680, CARD_Y, CARD_W, CARD_H)
card_snake = scaled_rect(1026, CARD_Y, CARD_W, CARD_H)

options = ["flappy", "shooter", "snake" ]
GAMES = {"flappy": run_flappy, "shooter": run_shooter, "snake": run_snake}
option_rects = [card_flappy, card_shooter, card_snake]
selected = 0

running = True
state = "menu"
prev_state = None

    while running:
        # Redimensiona a janela ao transitar entre o launcher e os jogos
        if state ≠ prev_state:
            if state = "menu":
                screen = pygame.display.set_mode((LAUNCHER_W, LAUNCHER_H))
        elif state in options:
            screen = pygame.display.set_mode((width, height))
        prev_state = state

    if state = "menu":
        screen.blit(bg, (0, 0))

        # Desenha o destaque no card selecionado
        rect = option_rects[selected]
        h_surf = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        h_surf.fill((255, 255, 255, 60))
        screen.blit(h_surf, (rect.x, rect.y))
        pygame.draw.rect(screen, (255, 215, 0), rect, 3, border_radius=4)

        for event in pygame.event.get():
            if event.type = pygame.QUIT:
                running = False

        if event.type = pygame.MOUSEMOTION:
            for i, rect in enumerate(option_rects):
                if rect.collidepoint(event.pos):
                    selected = i

        if event.type = pygame.MOUSEBUTTONDOWN:
            if event.button = 1:
                for i, rect in enumerate(option_rects):
                    if rect.collidepoint(event.pos):
                        selected = i
                        state = options[selected]

        if event.type = pygame.KEYDOWN:
            if event.key = pygame. K_LEFT:
                selected = (selected - 1) % len(options)
            if event.key = pygame.K_RIGHT:
                selected = (selected + 1) % len(options)
            if event.key = pygame.K_RETURN:
                state = options[selected]

        pygame.display.update()
        clock.tick(60)

    elif state in GAMES:
        state = GAMES[state](screen)

    elif state = "quit":
        running = False

    pygame.quit()