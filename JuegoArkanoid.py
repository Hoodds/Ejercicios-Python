import pygame
import sys
import random

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Arkanoid')

# Colores
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# Velocidad del reloj
clock = pygame.time.Clock()
fps = 60

# Raqueta
paddle_width = 100
paddle_height = 10
paddle_speed = 7
paddle = pygame.Rect(screen_width // 2 - paddle_width // 2, screen_height - paddle_height - 10, paddle_width, paddle_height)

# Pelota
ball_radius = 10
ball_speed_x = 4
ball_speed_y = -4
ball = pygame.Rect(screen_width // 2 - ball_radius, screen_height // 2 - ball_radius, ball_radius * 2, ball_radius * 2)

# Ladrillos
brick_rows = 6
brick_cols = 10
brick_width = 75
brick_height = 20
bricks = []

for row in range(brick_rows):
    for col in range(brick_cols):
        brick = pygame.Rect(col * (brick_width + 10) + 35, row * (brick_height + 10) + 50, brick_width, brick_height)
        bricks.append(brick)

# Función para dibujar todo en la pantalla
def draw():
    screen.fill(black)
    pygame.draw.rect(screen, blue, paddle)
    pygame.draw.ellipse(screen, red, ball)
    for brick in bricks:
        pygame.draw.rect(screen, white, brick)
    pygame.display.flip()

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento de la raqueta
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < screen_width:
        paddle.right += paddle_speed

    # Movimiento de la pelota
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Colisiones con la pantalla
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1
    if ball.bottom >= screen_height:
        running = False  # Fin del juego si la pelota toca el fondo

    # Colisiones con la raqueta
    if ball.colliderect(paddle):
        ball_speed_y *= -1

    # Colisiones con los ladrillos
    for brick in bricks[:]:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_speed_y *= -1
            break

    draw()
    clock.tick(fps)
