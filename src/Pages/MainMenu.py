import flet as ft
from .cards.CardsMenu import cardsmenu


def mainmenu(page: ft.Page):

    page.clean()
    page.appbar = ft.CupertinoAppBar(
        leading=ft.Icon(ft.Icons.SMART_BUTTON),
        bgcolor=ft.Colors.GREY_900,
        trailing=ft.Icon(ft.Icons.LIST),
        middle=ft.Text("Main Menu"),
    )

    def callCardsMenu(ObligatedArgument):
        cardsmenu(page)

    page.add(ft.Container(content=ft.CupertinoFilledButton("Cards Menu", on_click=callCardsMenu, alignment=ft.alignment.center), width=page.window.width))

