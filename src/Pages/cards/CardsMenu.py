import flet as ft
from . import CardsBack

def cardsmenu(page: ft.Page):
    page.clean()

    def CreateCard(RrequiredArgument, CreateViewfront, CreateViewback, CreateViewDeckSelector):
        CardsBack.Cards(ft.Text(CreateViewfront.value), ft.Text(CreateViewback.value), page, CreateViewDeckSelector.value)
        print(CardsBack.Decks)
        # print(CardsBack.Decks[CreateViewfront.value])
        # CardsBack.updateDecksJson()

    def CreateDeck(RrequiredArgument, CreateDeckViewName):
        CardsBack.Decks[CreateDeckViewName.value]={}
        print(CardsBack.Decks)
        # CardsBack.updateDecksJson()

    elements={}

    CreateViewfront        = ft.TextField(label="Front", hint_text="Ex: when jesus was born")
    CreateViewback         = ft.TextField(label="Back", hint_text="Ex: in year 0")
    CreateViewLabel        = ft.Text("create Card")
    CreateDeckViewName     = ft.TextField(label="Name", hint_text="ex: Science Deck")
    elements["CreateViewDeckSelector"] = ft.Dropdown(label="Deck",options=[ft.dropdown.Option(value) for value in CardsBack.Decks], expand=True)
    CreateViewDeckButton   = ft.CupertinoFilledButton("Create Deck", on_click= lambda _: CreateDeck(_, CreateDeckViewName))
    CreateViewButton       = ft.CupertinoFilledButton("Create", on_click=lambda _:CreateCard(_, CreateViewfront, CreateViewback, elements["CreateViewDeckSelector"]))

    def ChangePage(index):
        elements["CreateViewDeckSelector"] = ft.Dropdown(label="Deck", options=[ft.dropdown.Option(value) for value in
                                                                                CardsBack.Decks])
        if index==0:
            page.clean()

            CreateViewLabel.value = "create Card"
            page.add(
                CreateViewLabel,
                CreateViewfront,
                CreateViewback,
                elements["CreateViewDeckSelector"],
                CreateViewButton,
            )

        if index==1:
            page.clean()
            page.add(
                CreateDeckViewName,
                CreateViewDeckButton,
            )


        if index==2:
            """page.clean()
            for deck in CardsBack.Decks:
                page.add(ft.CupertinoFilledButton(deck, on_click=lambda _:CardsBack.Learn(deck)))"""
            CardsBack.Learn("Default", page)

        if index==3:
            page.navigation_bar = None
            page.Pages["MainMenu"](page)

    page.appbar = ft.CupertinoAppBar(
        leading=ft.Icon(ft.Icons.MY_LIBRARY_BOOKS),
        bgcolor=ft.Colors.GREY_900,
        trailing=ft.Icon(ft.Icons.IMAGE),
        middle=ft.Text("ManthanApp"),
    )

    page.navigation_bar=ft.CupertinoNavigationBar(
        bgcolor=ft.Colors.GREY_900,
        inactive_color=ft.Colors.GREY,
        active_color=ft.Colors.BLACK,
        on_change=lambda e:ChangePage(e.control.selected_index),
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.ADD, label="Create card"),
            ft.NavigationBarDestination(icon=ft.Icons.STACKED_BAR_CHART, label="Create deck"),
            ft.NavigationBarDestination(icon=ft.Icons.BOOK, label="Learn"),
            ft.NavigationBarDestination(icon=ft.Icons.LIST, label="MainMenu")
        ]
    )
    page.clean()
    page.add(
        CreateViewfront,
        CreateViewback,
        elements["CreateViewDeckSelector"],
        CreateViewButton,
    )