# views/lista_treinos_view.py

import flet as ft
from views.criar_treino_view import criar_treino_view
from views.treino_view import treino_view

def lista_treinos_view(page: ft.Page, usuario):
    def abrir_criar_treino(e):
        page.controls.clear()
        page.add(criar_treino_view(page, usuario))
        page.update()

    def selecionar_treino(treino):
        page.controls.clear()
        page.add(treino_view(page, treino))
        page.update()

    lista_treinos = ft.ListView()
    for treino in usuario.treinos:
        lista_treinos.controls.append(ft.TextButton(f"Treino: {treino.nome}", on_click=lambda e, treino=treino: selecionar_treino(treino)))

    criar_treino_button = ft.ElevatedButton(text="Criar Treino", on_click=abrir_criar_treino)

    return ft.Column([
        ft.Text("Seus Treinos"),
        lista_treinos,
        criar_treino_button
    ])
