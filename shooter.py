import os
import sys
from random import randint, uniform
import pygame

pygame.init()

screen_width, screen_height = 1280, 960  # Размер игрового окна
screen = pygame.display.set_mode((screen_width, screen_height))  # Создание игрового окна


def sound_path(file):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, file)
    return os.path.join(os.getcwd(),'sounds', file)


bg_sound = pygame.mixer.Sound(sound_path('sound.mp3'))
explosion_sound = pygame.mixer.Sound(sound_path('explosion.mp3'))
fire_up_sound = pygame.mixer.Sound(sound_path('fire_up.mp3'))
life_up_sound = pygame.mixer.Sound(sound_path('life_up.mp3'))
lose_sound = pygame.mixer.Sound(sound_path('lose.mp3'))
gun_sound = pygame.mixer.Sound(sound_path('gun.mp3'))
bonus_sound = pygame.mixer.Sound(sound_path('bonus.mp3'))

bg_sound.set_volume(1.1)
explosion_sound.set_volume(1.1)
lose_sound.set_volume(1.1)
bonus_sound.set_volume(1.1)


def font_path(file):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, file)
    return os.path.join(os.getcwd(),'fonts', file)


game_over_font = pygame.font.Font(font_path('Roboto-Black.ttf'), 80)
point_game_font = pygame.font.Font(font_path('Roboto-Black.ttf'), 40)
game_score_font = pygame.font.Font(font_path('Roboto-Black.ttf'), 25)


def recurse_path(file):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, file)
    return os.path.join(os.getcwd(),'images', file)


icon = pygame.image.load(recurse_path('icon.png'))
pygame.display.set_icon(icon)

asteroid = pygame.image.load(recurse_path('asteroid.png')).convert_alpha()
asteroid2 = pygame.image.load(recurse_path('asteroid2.png')).convert_alpha()
asteroid3 = pygame.image.load(recurse_path('asteroid3.png')).convert_alpha()
asteroid4 = pygame.image.load(recurse_path('asteroid4.png')).convert_alpha()
asteroid5 = pygame.image.load(recurse_path('asteroid5.png')).convert_alpha()
asteroid6 = pygame.image.load(recurse_path('asteroid6.png')).convert_alpha()
asteroid7 = pygame.image.load(recurse_path('asteroid7.png')).convert_alpha()
asteroid8 = pygame.image.load(recurse_path('asteroid8.png')).convert_alpha()

angle = uniform(0.01, 0.1)
ast_x = randint(0, 1280)
ast_y = - 40
ast_step = uniform(0.25, 0.5)

angle2 = uniform(0.01, 0.1)
ast2_x = randint(30, 1250)
ast2_y = ast_y
ast_step2 = uniform(0.25, 0.5)

angle3 = uniform(0.01, 0.1)
ast3_x = randint(30, 1250)
ast3_y = ast_y
ast_step3 = uniform(0.25, 0.5)

angle4 = uniform(0.01, 0.1)
ast4_x = randint(30, 1250)
ast4_y = ast_y
ast_step4 = uniform(0.25, 0.5)

angle_zero = uniform(-0.01, -0.1)
ast5_x = randint(30, 1250)
ast5_y = ast_y
ast_step5 = uniform(0.25, 0.5)

angle_zero2 = uniform(-0.01, -0.1)
ast6_x = randint(30, 1250)
ast6_y = ast_y
ast_step6 = uniform(0.25, 0.5)

angle_zero3 = uniform(-0.01, -0.1)
ast7_x = randint(30, 1250)
ast7_y = ast_y
ast_step7 = uniform(0.25, 0.5)

angle_zero4 = uniform(-0.01, -0.1)
ast8_x = randint(30, 1250)
ast8_y = ast_y
ast_step8 = uniform(0.25, 0.5)

lives = [pygame.image.load(recurse_path('life.png')).convert_alpha(),
         pygame.image.load(recurse_path('life.png')).convert_alpha(),
         pygame.image.load(recurse_path('life.png')).convert_alpha(),
         ]

bg = pygame.image.load(recurse_path('screen.jpg')).convert_alpha()
bg_y = 0

pygame.display.set_caption("Awesome Shooter game")  # Создание заголовка

PLAYER_STEP = 1  # Размер шага перемещения корабля
player_speed = PLAYER_STEP
player = pygame.image.load(recurse_path('fighter.png')).convert_alpha()  # Создание корабля ГГ
player_width, player_height = player.get_size()  # Получение размеров ГГ
player_x = screen_width / 2 - player_width / 2
player_y = screen_height - player_height
player_is_moving_left, player_is_moving_right = False, False

ALIEN_STEP = 0.7
alien_speed = ALIEN_STEP

aliens = [pygame.image.load(recurse_path('alien_1.png')).convert_alpha(),
          pygame.image.load(recurse_path('alien_2.png')).convert_alpha(),
          pygame.image.load(recurse_path('alien_3.png')).convert_alpha(),
          ]  # Создание корабля противника

alien_v = 0
alien_width, alien_height = aliens[alien_v].get_size()  # Получение размеров корабля противника
alien_x = randint(0 + alien_width * 2, screen_width - alien_width * 2)
alien_y = 0 - alien_height

FIRE_STEP = 0.7
fire_speed = FIRE_STEP
fire_image = pygame.image.load(recurse_path('fire.png')).convert_alpha()
fire_width, fire_height = fire_image.get_size()  # Получение размеров ракеты
fire_x = 0
fire_y = 0
fires = []

explosion_image = pygame.image.load(recurse_path('explosion.png')).convert_alpha()
explosion_width, explosion_height = fire_image.get_size()  # Получение размеров ракеты

game_score = 0
score = 0
level = 1
gameplay = True
alien_death = False
game_is_running = True

ast_timer: int = pygame.USEREVENT + 1
pygame.time.set_timer(ast_timer, 1000)

bg_sound.play(-1)

while game_is_running:

    if gameplay:

        if player_is_moving_left and player_x >= PLAYER_STEP:
            player_x -= player_speed
        if player_is_moving_right and player_x <= screen_width - player_width - PLAYER_STEP:
            player_x += player_speed

        alien_y += alien_speed

        screen.blit(bg, (0, bg_y))  # Добавление фона
        screen.blit(bg, (0, bg_y - 960))  # Добавление фона

        screen.blit(asteroid, (ast_x, ast_y))
        screen.blit(asteroid2, (ast2_x, ast2_y))
        screen.blit(asteroid3, (ast3_x, ast3_y))
        screen.blit(asteroid4, (ast4_x, ast4_y))
        screen.blit(asteroid5, (ast5_x, ast5_y))
        screen.blit(asteroid6, (ast6_x, ast6_y))
        screen.blit(asteroid7, (ast7_x, ast7_y))
        screen.blit(asteroid8, (ast8_x, ast8_y))

        ast_y += ast_step
        ast2_y += ast_step2
        ast3_y += ast_step3
        ast4_y += ast_step4
        ast5_y += ast_step5
        ast6_y += ast_step6
        ast7_y += ast_step7
        ast8_y += ast_step8

        ast_x += angle
        ast2_x += angle2
        ast3_x += angle3
        ast4_x += angle4
        ast5_x += angle_zero
        ast6_x += angle_zero2
        ast7_x += angle_zero3
        ast8_x += angle_zero4

        if ast_y > 1000 or ast_x > 1320 or ast_x < - 40:
            ast_x = randint(30, 1250)
            ast_y = - 68
            ast_y += 0.25
            ast_x += angle

        if ast2_y > 1000 or ast2_x > 1320 or ast2_x < - 40:
            ast2_x = randint(30, 1250)
            ast2_y = - 60
            ast2_y += 0.25
            ast2_x += angle2

        if ast3_y > 1000 or ast3_x > 1320 or ast3_x < - 40:
            ast3_x = randint(30, 1250)
            ast3_y = - 59
            ast3_y += 0.25
            ast3_x += angle3

        if ast4_y > 1000 or ast4_x > 1320 or ast4_x < - 40:
            ast4_x = randint(30, 1250)
            ast4_y = - 49
            ast4_y += 0.25
            ast4_x += angle4

        if ast5_y > 1000 or ast5_x > 1320 or ast5_x < - 40:
            ast5_x = randint(30, 1250)
            ast5_y = - 55
            ast5_y += 0.25
            ast5_x += angle_zero

        if ast6_y > 1000 or ast6_x > 1320 or ast6_x < - 40:
            ast6_x = randint(30, 1250)
            ast6_y = - 40
            ast6_y += 0.25
            ast6_x += angle_zero2

        if ast7_y > 1000 or ast7_x > 1320 or ast7_x < - 40:
            ast7_x = randint(30, 1250)
            ast7_y = - 45
            ast7_y += 0.25
            ast7_x += angle_zero3

        if ast8_y > 1000 or ast8_x > 1320 or ast8_x < - 40:
            ast8_x = randint(30, 1250)
            ast8_y = - 50
            ast8_y += 0.25
            ast8_x += angle_zero4

        screen.blit(aliens[alien_v], (alien_x, alien_y))  # Добавление корабля противника в координаты

        life_x = 1030
        for live in lives:
            screen.blit(live, (life_x, 20))
            life_x += 80

        fire_x = player_x + player_width / 2 - fire_width / 2 + 4
        fire_y = player_y - fire_height / 2

        fire_rect = fire_image.get_rect(topleft=(fire_x, fire_y))

        alien_rect = aliens[alien_v].get_rect(topleft=(alien_x, alien_y))

        if fires:
            if level == 1:
                for i, el in enumerate(fires):
                    screen.blit(fire_image, (el.x, el.y))  # Добавления снаряда выстрела
                    el.y -= FIRE_STEP
                    if alien_rect.colliderect(el):
                        alien_death = True

            if level == 2:
                for i, el in enumerate(fires):
                    screen.blit(fire_image, (el.x + fire_width / 2, el.y))  # Добавления снаряда выстрела
                    screen.blit(fire_image, (el.x - fire_width / 2, el.y))  # Добавления снаряда выстрела
                    el.y -= FIRE_STEP
                    if alien_rect.colliderect(el):
                        alien_death = True

            if level == 3:
                for i, el in enumerate(fires):
                    screen.blit(fire_image, (el.x + fire_width / 1.1, el.y))  # Добавления снаряда выстрела
                    screen.blit(fire_image, (el.x, el.y))  # Добавления снаряда выстрела
                    screen.blit(fire_image, (el.x - fire_width / 1.1, el.y))  # Добавления снаряда выстрела
                    el.y -= FIRE_STEP
                    if alien_rect.colliderect(el):
                        alien_death = True

            if alien_death:
                explosion_sound.play()
                try:
                    if level == 1:
                        fires.pop(i)
                    if level == 2:
                        fires.pop(i)
                        fires.pop(i - 1)
                    if level == 3:
                        fires.pop(i)
                        fires.pop(i - 1)
                        fires.pop(i - 2)
                except IndexError:
                    fires.clear()
                screen.blit(explosion_image, (alien_x, alien_y))
                pygame.display.update()
                pygame.time.wait(40)
                alien_x = randint(0 + alien_width * 2, screen_width - alien_width * 2)
                alien_y = 0 - alien_height
                if level == 1:
                    game_score += 1
                    score += 1
                if level == 2:
                    game_score += 2
                    score += 2
                if level == 3:
                    game_score += 3
                    score += 3
                alien_death = False
                if game_score % 2 == 0:  # 265
                    if alien_speed <= 2.5:
                        alien_speed += 0.025
                        player_speed += 0.020
                        ast_step += 0.025
                        ast_step2 += 0.025
                        ast_step3 += 0.025
                        ast_step4 += 0.025
                        ast_step5 += 0.025
                        ast_step6 += 0.025
                        ast_step7 += 0.025
                        ast_step8 += 0.025
                    else:
                        alien_speed += 0.0010
                        player_speed += 0.0005
                        ast_step += 0.01
                        ast_step2 += 0.01
                        ast_step3 += 0.01
                        ast_step4 += 0.01
                        ast_step5 += 0.01
                        ast_step6 += 0.01
                        ast_step7 += 0.01
                        ast_step8 += 0.01
                if level == 1:
                    if game_score % 40 == 0:
                        fire_up_sound.play()
                        level += 1
                if level == 2:
                    if game_score % 150 == 0:
                        fire_up_sound.play()
                        level += 1
                if game_score % 60 == 0 and len(lives) < 3:
                    life_up_sound.play()
                    lives.append(pygame.image.load(recurse_path('life.png')).convert_alpha())
                if level == 2:
                    alien_v = randint(0, 1)
                if level == 3:
                    alien_v = randint(0, 2)
                if score >= 100:
                    bonus_sound.play()
                    score -= 100

        screen.blit(player, (player_x, player_y))  # Добавление корабля в координаты

        game_score_text = game_score_font.render(f"Your Score is: {game_score}", True, "White")
        screen.blit(game_score_text, (20, 20))

        if alien_y + alien_height > screen_height:
            alien_x = randint(0 + alien_width * 2, screen_width - alien_width * 2)
            alien_y = 0 - alien_height
            if level > 1:
                level -= 1
            elif len(lives) > 0:
                lives.pop()
            else:
                bg_sound.stop()
                lose_sound.play()
                gameplay = False

        if bg_y > 960:
            bg_y = 0
        else:
            bg_y += alien_speed

    else:
        gameplay = False
        screen.blit(bg, (0, bg_y))

        game_over_text = game_over_font.render("Game Over", True, 'Red')
        end_game_text = point_game_font.render(f"Your Record is: {game_score}", True, "White")
        restart = point_game_font.render("Продолжить", True, "White")

        game_over_rectangle = game_over_text.get_rect()
        game_over_rectangle.center = (screen_width / 2, screen_height / 2)
        screen.blit(game_over_text, game_over_rectangle)

        end_game_rectangle = end_game_text.get_rect()
        end_game_rectangle.center = (screen_width / 2, screen_height / 1.7)
        screen.blit(end_game_text, end_game_rectangle)

        restart_rect = restart.get_rect(topleft=(screen_width / 2 - 120, screen_height / 1.6))
        screen.blit(restart, restart_rect)

        mouse = pygame.mouse.get_pos()

        if restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            alien_speed = ALIEN_STEP
            player_speed = PLAYER_STEP
            fire_speed = FIRE_STEP
            level = 1
            game_score = 0
            alien_v = 0
            score = 0
            gameplay = True
            ast_step = uniform(0.25, 0.5)
            ast_step2 = uniform(0.25, 0.5)
            ast_step3 = uniform(0.25, 0.5)
            ast_step4 = uniform(0.25, 0.5)
            ast_step5 = uniform(0.25, 0.5)
            ast_step6 = uniform(0.25, 0.5)
            ast_step7 = uniform(0.25, 0.5)
            ast_step8 = uniform(0.25, 0.5)
            fires.clear()
            bg_sound.play(-1)
            lives = [pygame.image.load(recurse_path('life.png')).convert_alpha(),
                     pygame.image.load(recurse_path('life.png')).convert_alpha(),
                     pygame.image.load(recurse_path('life.png')).convert_alpha(),
                     ]

    for event in pygame.event.get():  # Получение всех событие, и перебор их в цикле
        if event.type == pygame.QUIT:  # Проверка на нажатие крестика
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.KSCAN_X:
                sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_is_moving_left = True
            if event.key == pygame.K_RIGHT:
                player_is_moving_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_is_moving_left = False
            if event.key == pygame.K_RIGHT:
                player_is_moving_right = False
            if event.key == pygame.K_SPACE:
                gun_sound.play()
                if level == 1:
                    fires.append(fire_rect)
                if level == 2:
                    fires.append(fire_rect)
                    fires.append(fire_rect)
                if level == 3:
                    fires.append(fire_rect)
                    fires.append(fire_rect)
                    fires.append(fire_rect)
    pygame.display.update()
