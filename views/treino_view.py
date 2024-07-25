import flet as ft
from models.usuario import Usuario

def treino_view(page: ft.Page, usuario: Usuario, selecionar_treino):
    treino_name_input = ft.TextField(label="Nome do Treino")
    treinos_list_view = ft.ListView()

    def criar_treino(e):
        nome_treino = treino_name_input.value
        if nome_treino:
            treino = usuario.criar_treino(nome_treino)
            treinos_list_view.controls.append(ft.TextButton(f"Treino: {treino.nome}", on_click=lambda e, treino=treino: selecionar_treino(treino)))
            treino_name_input.value = ""
            page.update()

    criar_treino_button = ft.ElevatedButton(text="Criar Treino", on_click=criar_treino)

    return ft.Column([
        treino_name_input,
        criar_treino_button,
        treinos_list_view
    ])