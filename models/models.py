# models.py

class Exercicio:
    def __init__(self, nome, series, repeticoes):
        self.nome = nome
        self.series = series
        self.repeticoes = repeticoes
        self.series_executadas = 0
        self.tempo_gasto = 0

class Treino:
    def __init__(self, nome):
        self.nome = nome
        self.exercicios = []

    def adicionar_exercicio(self, exercicio):
        self.exercicios.append(exercicio)

class Usuario:
    def __init__(self):
        self.treinos = []

    def criar_treino(self, nome):
        treino = Treino(nome)
        self.treinos.append(treino)
        return treino
