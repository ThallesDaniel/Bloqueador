import flet as ft
from views.main_view import MainView

def main(page):
    page.title = "Gerenciador de Bloqueio de Sites"
    page.add(MainView())

ft.app(target=main)
