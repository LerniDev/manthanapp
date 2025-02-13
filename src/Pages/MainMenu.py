import flet as ft
from CardsMenu import cardsmenu


def mainmenu(page: ft.Page):
    page.add(ft.ElevatedButton("Cards Menu", on_click=cardsmenu(page)))