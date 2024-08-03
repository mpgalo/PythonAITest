# Sugestão de código para o pong usando o Gemini
import pygame
import random

# Inicialização do Pygame
pygame.init()

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Dimensões da tela
WIDTH = 800
HEIGHT = 600

# Criar a tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Configurações do jogador
player_width = 10
player_height = 60
player_speed = 5
player1_y = HEIGHT // 2 - player_height // 2
player2_y = HEIGHT // 2 - player_height // 2

# Configurações da bola
ball_radius = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 5

# Configurações do jogo
game_over = False
player1_score = 0
player2_score = 0
font = pygame.font.Font(None, 36)

# Função para desenhar o jogador
def draw_player(x, y, width, height):
    pygame.draw.rect(screen, WHITE, (x, y, width, height))

# Função para desenhar a bola
def draw_ball(x, y, radius):
    pygame.draw.circle(screen, WHITE, (x, y), radius)

# Função para atualizar a posição da bola
def update_ball():
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    global player1_score, player2_score

    # Verificar colisões com os jogadores
    if ball_x - ball_radius <= player_width and ball_y >= player1_y and ball_y <= player1_y + player_height:
        ball_speed_x *= -1
        # Adicionar um pouco de aleatoriedade à direção vertical da bola
        ball_speed_y += random.randint(-2, 2)
    elif ball_x + ball_radius >= WIDTH - player_width and ball_y >= player2_y and ball_y <= player2_y + player_height:
        ball_speed_x *= -1
        # Adicionar um pouco de aleatoriedade à direção vertical da bola
        ball_speed_y += random.randint(-2, 2)

    # Atualizar a posição da bola
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Verificar colisões com as bordas superior e inferior
    if ball_y + ball_radius >= HEIGHT or ball_y - ball_radius <= 0:
        ball_speed_y *= -1

    # Verificar se a bola saiu da tela
    if ball_x + ball_radius < 0:
        player2_score += 1
        reset_ball()
    elif ball_x - ball_radius > WIDTH:
        player1_score += 1
        reset_ball()

# Função para reiniciar a bola
def reset_ball():
    global ball_x, ball_y, ball_speed_x, ball_speed_y

    ball_x = WIDTH // 2
    ball_y = HEIGHT // 2
    ball_speed_x = random.choice([-5, 5])
    ball_speed_y = random.choice([-5, 5])

# Função para atualizar a posição do jogador
def update_player(player_y, direction):
    if player_y + direction * player_speed >= 0 and player_y + player_height + direction * player_speed <= HEIGHT:
        player_y += direction * player_speed
    return player_y

# Loop principal do jogo
running = True
while running:
    # Tratar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obter entrada do usuário
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1_y = update_player(player1_y, -1)
    if keys[pygame.K_s]:
        player1_y = update_player(player1_y, 1)
    if keys[pygame.K_UP]:
        player2_y = update_player(player2_y, -1)
    if keys[pygame.K_DOWN]:
        player2_y = update_player(player2_y, 1)

    # Atualizar a posição da bola
    update_ball()

    # Desenhar a tela
    screen.fill(BLACK)
    draw_player(0, player1_y, player_width, player_height)
    draw_player(WIDTH - player_width, player2_y, player_width, player_height)
    draw_ball(ball_x, ball_y, ball_radius)

    # Desenhar o placar
    score_text = font.render(f"{player1_score} - {player2_score}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))

    # Atualizar a tela
    pygame.display.flip()

# Finalizar o Pygame
pygame.quit()
