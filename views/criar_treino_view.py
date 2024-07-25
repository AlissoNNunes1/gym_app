# views/criar_treino_view.py

import flet as ft

def criar_treino_view(page: ft.Page, usuario):
    treino_name_input = ft.TextField(label="Nome do Treino")
    grupos_musculares_input = ft.TextField(label="Grupos Musculares")

    def criar_treino(e):
        nome_treino = treino_name_input.value
        grupos_musculares = grupos_musculares_input.value
        if nome_treino and grupos_musculares:
            usuario.criar_treino(nome_treino, grupos_musculares)
            from views.lista_treinos_view import lista_treinos_view
            page.controls.clear()
            page.add(lista_treinos_view(page, usuario))
            page.update()

    criar_treino_button = ft.ElevatedButton(text="Criar Treino", on_click=criar_treino)

    return ft.Column([
        ft.Text("Criar Novo Treino"),
        treino_name_input,
        grupos_musculares_input,
        criar_treino_button
    ])
