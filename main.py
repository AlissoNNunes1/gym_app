# main.py

from flet import app, Page
from views.main_view import main_view

def main(page: Page):
    main_view(page)

app(target=main)
