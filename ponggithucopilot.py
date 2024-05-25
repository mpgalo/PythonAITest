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
placar.color("white")
placar.penup()
placar.hideturtle()
placar.goto(0, 260)
placar.write("Jogador A: 0  Jogador B: 0", align="center", font=("Courier", 24, "normal"))

# Funções de movimento das raquetes
def raquete_a_up():
    y = raquete_a.ycor()
    if y < 250:
        y += 20
    raquete_a.sety(y)

def raquete_a_down():
    y = raquete_a.ycor()
    if y > -240:
        y -= 20
    raquete_a.sety(y)

def raquete_b_up():
    y = raquete_b.ycor()
    if y < 250:
        y += 20
    raquete_b.sety(y)

def raquete_b_down():
    y = raquete_b.ycor()
    if y > -240:
        y -= 20
    raquete_b.sety(y)

# Associação de teclas às funções de movimento das raquetes
window.onkey(raquete_a_up, "w")
window.onkeyrelease(raquete_a_up, "w")
window.onkey(raquete_a_down, "s")
window.onkeyrelease(raquete_a_down, "s")
window.onkey(raquete_b_up, "Up")
window.onkeyrelease(raquete_b_up, "Up")
window.onkey(raquete_b_down, "Down")
window.onkeyrelease(raquete_b_down, "Down")
window.listen()

# Loop principal do jogo
while True:
    window.update()

    # Movimento da bola
    bola.setx(bola.xcor() + bola.dx)
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