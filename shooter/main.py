import pygame
import random
import os

from common. colors import *
from common. constants import *
from common.ui import draw_score, draw_paused, draw_start_msg

def run_snake(screen):

    clock = pygame. time. Clock( )

    base = os.path.abspath(os.path.join(os.path.dirname(__file_), "../../assets/snake"))

    bg = pygame. image. load(os.path. join(base,"bg.png"))
    bg = pygame. transform.scale(bg, (width, height))

    obstacle_img = pygame.image.load(os.path.join(base,"obstacle.png"))
    obstacle_img = pygame.transform.scale(obstacle_img,(10,10))

    snake = [(100,100)]
    dx,dy = 10,0

    grid = 10

    obstacles = []
    while len(obstacles) < 25:
        pos = (
            random.randrange(20,width-20,grid),
            random.randrange(20,height-20,grid)
        )
        if pos not in snake:
            obstacles.append(pos)

    def place_food():
        while True:
            candidate = (
            random. randrange(20,width-20,grid),
            random.randrange(20,height-20,grid)
        )
        if candidate not in snake and candidate not in obstacles:
            return candidate

    food = place_food()

        speed = 8
        score = 0
        started = False
        paused = False

        running = True
        while running:
            screen.blit(bg,(0,0))

            panel = pygame. Surface((width-40, height-40), pygame. SRCALPHA)
            panel.fill((*BG_PANEL, 190))
            pygame.draw.rect(panel, (*BG_PANEL_LIGHT, 220), panel.get_rect(), border_radius=16, width=2)
            screen.blit(panel, (20,20))
           
           for x in range(20, width-20, grid):
                pygame.draw.line(screen, (*BG_SOFT, 40), (x,20), (x,height-20), 1)
            for y in range(20, height-20, grid):
                pygame.draw.line(screen. (BG SOFT. 40).(20.v). (width-20.v).1)

            for o in obstacles:
                screen.blit(obstacle_img, o)

            food_center = (food[0] + 5, food[1] + 5)
            pygame.draw.circle(screen, FOOD_ACCENT, food_center, 5)
            pygame.draw.circle(screen, (255,255,255), (food_center[0]-1, food_center[1]-1), 2)

            for segment in snake[1:]:
            pygame.draw.rect(screen, SNAKE_BODY, (*segment, grid, grid), border_radius=4)

            pygame.draw.rect(screen, SNAKE_HEAD, (*snake[0], grid, grid), border_radius=4)
            
            draw_score(screen, score)

            for event in pygame.event.get():
                if event.type = pygame.QUIT:
                    return "quit"

            if event.type = pygame. KEYDOWN:
                
                if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT):
                    started = True

            if event.key = pygame.K_ESCAPE:
                return "menu"
                
            if event.key = pygame.K_p:
                paused = not paused

            if event.key = pygame.K_UP and dy = 0:
                dx,dy = 0,-grid

            elif event.key = pygame.K_DOWN and dy = 0:
                dx,dy = 0,grid

            elif event.key = pygame.K_LEFT and dx = 0:
                dx,dy = -grid,0

            elif event.key = pygame.K_RIGHT and dx =0:
                dx,dy = grid,0

            if paused:
                draw_paused(screen)

            if started and not paused:
                new_head = (snake[0][0] + dx, snake[0] [1] + dy)
                snake.insert(0, new_head)

            if new_head = food:
                score += 1
                food = place_food()

            else:
                snake. pop()

            if (
                new_head[0] < 20 or new_head[0] > width-20 Or OTECTED ANT
                new_head[1] < 20 or new_head[1] > height-20 or
                new_head in snake[1:] or
                new head in obstacles
            ):
                return "menu"

            if not started:
                draw_start_msg(screen)

            pygame.display.update()
            clock.tick(speed)