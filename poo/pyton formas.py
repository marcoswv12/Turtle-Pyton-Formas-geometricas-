import turtle

# Classe base para todas as figuras
class Figura:
    def __init__(self, cor):
        self.t = turtle.Turtle()
        self.t.pensize(5)
        self.t.pencolor(cor)
        self.t.speed(3)

    def desenhar(self):
        pass  # Será sobrescrito nas subclasses

# Classe Quadrado
class Quadrado(Figura):
    def desenhar(self):
        #desenha a forma
        for _ in range(4):
            self.t.forward(100)
            self.t.left(90)

# Classe Triangulo
class Triangulo(Figura):
    def desenhar(self):
        #desenha a forma
        for _ in range(3):
            self.t.forward(100)
            self.t.left(120)

# Classe Circulo
class Circulo(Figura):
    def desenhar(self):
        #desenha a forma
        self.t.circle(60)

# Classe Hexagono
class Hexagono(Figura):
    def desenhar(self):
        #desenha a forma
        for _ in range(6):
            self.t.forward(70)
            self.t.left(60)

# Pede a figura desejada ao usuário
forma = input("Digite a forma (quadrado, triangulo, circulo, hexagono): ").lower()

# Pede a cor desejada ao usuário
cor = input("Qual a cor da sua figura? (yellow, blue, green, red, orange): ").lower()

# Cria objeto conforme escolha e desenha
figura = None

if forma == "quadrado":
    figura = Quadrado(cor)
elif forma == "triangulo":
    figura = Triangulo(cor)
elif forma == "circulo":
    figura = Circulo(cor)
elif forma == "hexagono":
    figura = Hexagono(cor)
else:
    print("Forma inválida! Digite uma forma válida.")

if figura:
    figura.desenhar()

turtle.done()
