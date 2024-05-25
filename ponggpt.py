import pygame
import sys

# Inicializar o Pygame
pygame.init()

# Definir cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definir as dimensões da janela
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Definir as dimensões e a velocidade da bola
BALL_WIDTH = 20
BALL_HEIGHT = 20
ball_x = WINDOW_WIDTH // 2 - BALL_WIDTH // 2
ball_y = WINDOW_HEIGHT // 2 - BALL_HEIGHT // 2
ball_speed_x = 4
ball_speed_y = 4
speed_increment = 0.5

# Definir as dimensões e a velocidade das raquetes
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
paddle_speed = 6

# Posição inicial das raquetes
paddle1_x = 50
paddle1_y = WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2

paddle2_x = WINDOW_WIDTH - 50 - PADDLE_WIDTH
paddle2_y = WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2

# Variáveis de pontuação
score1 = 0
score2 = 0

# Criar a janela do jogo
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Pong')

# Fonte para o placar
font = pygame.font.Font(None, 74)

# Controle de frames
clock = pygame.time.Clock()

# Função para mover a raquete controlada pelo computador
def move_computer_paddle():
    global paddle2_y
    if paddle2_y + PADDLE_HEIGHT / 2 < ball_y:
        paddle2_y += paddle_speed
    elif paddle2_y + PADDLE_HEIGHT / 2 > ball_y:
        paddle2_y -= paddle_speed

    # Manter a raquete do computador dentro da tela
    if paddle2_y < 0:
        paddle2_y = 0
    if paddle2_y > WINDOW_HEIGHT - PADDLE_HEIGHT:
        paddle2_y = WINDOW_HEIGHT - PADDLE_HEIGHT

while True:
    # Evento de saída
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s] and paddle1_y < WINDOW_HEIGHT - PADDLE_HEIGHT:
        paddle1_y += paddle_speed

    # Movimento da raquete do computador
    move_computer_paddle()

    # Movimento da bola
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Colisões com as bordas superiores e inferiores
    if ball_y <= 0 or ball_y >= WINDOW_HEIGHT - BALL_HEIGHT:
        ball_speed_y = -ball_speed_y

    # Colisões com as raquetes
    if (ball_x <= paddle1_x + PADDLE_WIDTH and paddle1_y < ball_y < paddle1_y + PADDLE_HEIGHT) or \
       (ball_x >= paddle2_x - BALL_WIDTH and paddle2_y < ball_y < paddle2_y + PADDLE_HEIGHT):
        ball_speed_x = -ball_speed_x

        # Aumentar a velocidade da bola
        if ball_speed_x > 0:
            ball_speed_x += speed_increment
        else:
            ball_speed_x -= speed_increment

        if ball_speed_y > 0:
            ball_speed_y += speed_increment
        else:
            ball_speed_y -= speed_increment

    # Colisão com as bordas laterais (pontuação)
    if ball_x <= 0:
        score2 += 1
        ball_x = WINDOW_WIDTH // 2 - BALL_WIDTH // 2
        ball_y = WINDOW_HEIGHT // 2 - BALL_HEIGHT // 2
        ball_speed_x = -4
        ball_speed_y = 4
    if ball_x >= WINDOW_WIDTH - BALL_WIDTH:
        score1 += 1
        ball_x = WINDOW_WIDTH // 2 - BALL_WIDTH // 2
        ball_y = WINDOW_HEIGHT // 2 - BALL_HEIGHT // 2
        ball_speed_x = 4
        ball_speed_y = 4

    # Atualizar a tela
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (paddle1_x, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (paddle2_x, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_WIDTH, BALL_HEIGHT))
    pygame.draw.aaline(screen, WHITE, (WINDOW_WIDTH // 2, 0), (WINDOW_WIDTH // 2, WINDOW_HEIGHT))

    # Desenhar o placar
    score_text = font.render(f"{score1}  {score2}", True, WHITE)
    screen.blit(score_text, (WINDOW_WIDTH // 2 - score_text.get_width() // 2, 10))

    pygame.display.flip()
    clock.tick(60)
