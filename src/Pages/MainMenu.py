import flet as ft
from .cards.CardsMenu import cardsmenu


def mainmenu(page: ft.Page):

    def callCardsMenu(ObligatedArgument):
        cardsmenu(page)

    page.add(ft.CupertinoFilledButton("Cards Menu", on_click=callCardsMenu, alignment=ft.alignment.center))

