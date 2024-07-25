# views/exercicio_view.py
import flet as ft
from controllers.exercicio_controller import adicionar_exercicio

def exercicio_view(page: ft.Page, treino):
    exercicio_name_input = ft.TextField(label="Nome do Exercício")
    series_input = ft.TextField(label="Séries")
    repeticoes_input = ft.TextField(label="Repetições")

    def adicionar_exercicio_click(e):
        nome = exercicio_name_input.value
        series = series_input.value
        repeticoes = repeticoes_input.value
        if nome and series and repeticoes:
            adicionar_exercicio(treino, nome, series, repeticoes)
            from views.treino_view import treino_view
            page.controls.clear()
            page.add(treino_view(page, treino))
            page.update()

    adicionar_exercicio_button = ft.ElevatedButton(text="Adicionar Exercício", on_click=adicionar_exercicio_click)

    return ft.Column([
        ft.Text("Adicionar Novo Exercício"),
        exercicio_name_input,
        series_input,
        repeticoes_input,
        adicionar_exercicio_button
    ])
