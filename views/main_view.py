import flet as ft
from models.usuario import Usuario
from treino_view import treino_view
from exercicio_view import exercicio_view
from timer_view import cronometro_view

def main_view(page: ft.Page):
    usuario = Usuario()
    page.title = "Gym App"
    
    treino_selecionado = None

    def selecionar_treino(treino):
        nonlocal treino_selecionado
        treino_selecionado = treino
        exercicios_list_view.controls.clear()
        for exercicio in treino.exercicios:
            exercicios_list_view.controls.append(ft.Text(f"Exercício: {exercicio.nome}, Séries: {exercicio.series}, Repetições: {exercicio.repeticoes}"))
        page.update()

    treino_section = treino_view(page, usuario, selecionar_treino)
    exercicio_section = exercicio_view(page, treino_selecionado)
    cronometro_section = cronometro_view(page)

    page.add(
        ft.Column([
            treino_section,
            exercicio_section,
            cronometro_section
        ])
    )