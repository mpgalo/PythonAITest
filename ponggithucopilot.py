import turtle

# Configuração da janela
window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Placar
placar_a = 0
placar_b = 0

# Raquete A
raquete_a = turtle.Turtle()
raquete_a.speed(0)
raquete_a.shape("square")
raquete_a.color("white")
raquete_a.shapesize(stretch_wid=6, stretch_len=1)
raquete_a.penup()
raquete_a.goto(-350, 0)

# Raquete B
raquete_b = turtle.Turtle()
raquete_b.speed(0)
raquete_b.shape("square")
raquete_b.color("white")
raquete_b.shapesize(stretch_wid=6, stretch_len=1)
raquete_b.penup()
raquete_b.goto(350, 0)

# Bola
bola = turtle.Turtle()
bola.speed(40)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.2
bola.dy = -0.2

# Placar
placar = turtle.Turtle()
placar.speed(0)
# Configuração do placar
placar.color("white")  # Define a cor do placar como branca
placar.penup()  # Desliga o desenho do placar
placar.hideturtle()  # Esconde o placar
placar.goto(0, 260)  # Posiciona o placar na posição (0, 260)
placar.write("Jogador A: 0  Jogador B: 0", align="center", font=("Courier", 24, "normal"))  # Escreve o placar inicial

# Funções de movimento das raquetes
def raquete_a_up():
    y = raquete_a.ycor()  # Obtém a coordenada y atual da raquete A
    if y < 250:  # Verifica se a raquete A não está no topo da tela
        y += 20  # Move a raquete A para cima
    raquete_a.sety(y)  # Atualiza a posição y da raquete A

def raquete_a_down():
    y = raquete_a.ycor()  # Obtém a coordenada y atual da raquete A
    if y > -240:  # Verifica se a raquete A não está na parte inferior da tela
        y -= 20  # Move a raquete A para baixo
    raquete_a.sety(y)  # Atualiza a posição y da raquete A

def raquete_b_up():
    y = raquete_b.ycor()  # Obtém a coordenada y atual da raquete B
    if y < 250:  # Verifica se a raquete B não está no topo da tela
        y += 20  # Move a raquete B para cima
    raquete_b.sety(y)  # Atualiza a posição y da raquete B

def raquete_b_down():
    y = raquete_b.ycor()  # Obtém a coordenada y atual da raquete B
    if y > -240:  # Verifica se a raquete B não está na parte inferior da tela
        y -= 20  # Move a raquete B para baixo
    raquete_b.sety(y)  # Atualiza a posição y da raquete B

# Associação de teclas às funções de movimento das raquetes
window.onkey(raquete_a_up, "w")  # Associa a tecla "w" à função raquete_a_up
window.onkeyrelease(raquete_a_up, "w")  # Associa a liberação da tecla "w" à função raquete_a_up
window.onkey(raquete_a_down, "s")  # Associa a tecla "s" à função raquete_a_down
window.onkeyrelease(raquete_a_down, "s")  # Associa a liberação da tecla "s" à função raquete_a_down
window.onkey(raquete_b_up, "Up")  # Associa a tecla "Up" à função raquete_b_up
window.onkeyrelease(raquete_b_up, "Up")  # Associa a liberação da tecla "Up" à função raquete_b_up
window.onkey(raquete_b_down, "Down")  # Associa a tecla "Down" à função raquete_b_down
window.onkeyrelease(raquete_b_down, "Down")  # Associa a liberação da tecla "Down" à função raquete_b_down
window.listen()  # Faz a janela começar a ouvir eventos de teclado

# Loop principal do jogo
while True:
    window.update()  # Atualiza a janela

    # Movimento da bola
    bola.setx(bola.xcor() + bola.dx)  # Move a bola horizontalmente
    bola.sety(bola.ycor() + bola.dy)

    # Verificação de colisão com as bordas
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        placar_a += 1
        placar.clear()
        placar.write("Jogador A: {}  Jogador B: {}".format(placar_a, placar_b), align="center", font=("Courier", 24, "normal"))

    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        placar_b += 1
        placar.clear()
        placar.write("Jogador A: {}  Jogador B: {}".format(placar_a, placar_b), align="center", font=("Courier", 24, "normal"))

    # Verificação de colisão com as raquetes
    if (bola.dx > 0) and (350 > bola.xcor() > 340) and (raquete_b.ycor() + 50 > bola.ycor() > raquete_b.ycor() - 50):
        bola.color("blue")
        bola.setx(340)
        bola.dx *= -1

    if (bola.dx < 0) and (-350 < bola.xcor() < -340) and (raquete_a.ycor() + 50 > bola.ycor() > raquete_a.ycor() - 50):
        bola.color("red")
        bola.setx(-340)
        bola.dx *= -1

    # Ajustar a velocidade de atualização da janela
    window.delay(0.01)