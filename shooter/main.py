import pygame
import random
import os

from common.colors import *
from common.constants import *
from common.ui import draw_score, draw_paused, draw_start_msg

def run_shooter(screen):

  clock = pygame.time.Clock()

  base = os.path.abspath(os.path.join(os.path.dirname(_file_), " .. / .. /assets/shooter"))

  bg = pygame.image.load(os.path.join(base,"bg.png")).convert()
  bg = pygame. transform.smoothscale(bg,(width,height))

  player_img = pygame. image.load(os.path.join(base,"player.png")).convert_alpha()
  player_img = pygame. transform.smoothscale(player_img,(40,40))

  bullet_img = pygame. image. load(os.path.join(base,"bullet.png")).convert_alpha()
  bullet_img = pygame. transform.smoothscale(bullet_img,(10,20))

  enemy1 = pygame. image. load(os.path. join(base,"enemy1.png")).convert_alpha()
  enemy1 = pygame.transform.smoothscale(enemy1,(40,40))

  enemy2 = pygame. image. load(os.path. join(base,"enemy2.png")).convert_alpha()
  enemy2 = pygame.transform.smoothscale(enemy2,(40,40))

  player_x = width//2
  player_y = height - 40

  bullets = []
  enemies = []

  speed = 0.8
  timer = 0
  score = 0
  started = False
  pauses = False

  while len(enemies) < 2:
    img = enemy1 if random.randint(0,1)=0 else enemy2
    enemies.append([random.randint(0,width-40),0,img])

running = True
  while running:
    screen.blit(bg(0,0))

for event in pygame.event.get():
  if event.typw = pygame.QUIT:
      return "quit"

  if event.type = pygame. KEYDOWN:
      started = True

  if event.key = pygame.K_ESCAPE:
      return "menu"

  if event.key = pygame.K_p:
      paused = not paused

  if event.key = pygame.K_SPACE and not paused:
      bullets.append([player_x+15,player_y])

  if paused:
      draw_paused(screen)

  if started and not paused:
      keys = pygame.key.get_pressed()

  




  
