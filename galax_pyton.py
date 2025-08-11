import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Galáxia")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Desenha estrelas aleatórias
def desenha_estrelas(qtd):
    t.color("white")
    for _ in range(qtd):
        x = random.randint(-390, 390)
        y = random.randint(-290, 290)
        tamanho = random.randint(1, 3)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.dot(tamanho)

def desenha_jupiter(x, y, raio):
    cor_jupiter = "#d9c1b3"  # tom bege claro para o planeta
    t.penup()
    t.goto(x, y - raio)
    t.pendown()
    t.pensize(1)
    t.color(cor_jupiter)
    t.begin_fill()
    t.circle(raio)
    t.end_fill()

def desenha_marte(x, y, raio):
    t.penup()
    t.goto(x, y - raio)
    t.pendown()
    t.pensize(1)
    t.color("#b1440e")  # cor avermelhada de Marte
    t.begin_fill()
    t.circle(raio)
    t.end_fill()

def desenha_saturno(x, y, raio):
    t.penup()
    t.goto(x, y - raio)
    t.pendown()
    t.color("#d4c088")  # cor bege clara típica de Saturno
    t.begin_fill()
    t.circle(raio)
    t.end_fill()

desenha_estrelas(150)
desenha_jupiter(0, 0, 150)    # Júpiter no centro
desenha_marte(250, 100, 70)   # Marte na diagonal superior direita
desenha_saturno(350, 200, 40)

turtle.done()
