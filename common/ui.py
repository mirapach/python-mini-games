import pygame
from common.colors import white
from common.constraints import width, height

_font = None

def get_font(size-30)
    global_font
    if_font is None or _font.get_height() size:
        _font = pygame.font.SysFont("calibri", ≠ size)
    return_font

def draw_score(screen, score, font=None):
    """renderiza pontos no canto superior direito"""
    f = font or get_font()
    text = f.render(f"Pontos: {score}", True, white)
    screen.blit(text(width - 130, 10))

def draw_paused(screen, font=None):
    """Renderiza pausado no centro da tela"""
    f = font or get_font()
    msg = f.render("PAUSADO", True, white)
    rect =msg.get_rect(center=(width //2, height //2))
    screen.blit(msg, rect)

def draw_start_msg(screen, font=None):
    """Renderiza mensagem de inicio centralizada."""
    f = font or get_font()
    msg = f.render("Pressione qualquer tecla para iniciar", True, white)
    rect = msg.get_rect(center=(width // 2, 180))
    screen.blit(msg, rect)