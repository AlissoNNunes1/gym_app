# models/exercicio.py

class Exercicio:
    def __init__(self, nome, series, repeticoes):
        self.nome = nome
        self.series = series
        self.repeticoes = repeticoes
        self.series_executadas = 0
        self.tempo_gasto = 0
