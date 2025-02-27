import flet as ft
from .cards.CardsMenu import cardsmenu
from .LearnSheet.learnSheets import *


def mainmenu(page: ft.Page):
    page.horizontal_alignment = "center"

    page.clean()
    page.appbar = ft.CupertinoAppBar(
        leading=ft.Icon(ft.Icons.SMART_BUTTON),
        bgcolor=ft.Colors.GREY_900,
        trailing=ft.Icon(ft.Icons.LIST),
        middle=ft.Text("Main Menu"),
    )

    def callCardsMenu(ObligatedArgument):
        cardsmenu(page)

    def callRevisionSheetsMenu(ObligatedArgument):
        learnSheetMenu(page)

    page.add(ft.Container(content=ft.CupertinoFilledButton("Cards Menu", on_click=callCardsMenu, alignment=ft.alignment.center), width=page.window.width))
    page.add(ft.Container(content=ft.CupertinoFilledButton("LearnSheet Menu", on_click=callRevisionSheetsMenu, alignment=ft.alignment.center),width=page.window.width))

