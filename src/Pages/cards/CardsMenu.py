import flet as ft
from . import CardsBack

def cardsmenu(page: ft.Page):
    page.clean()


    CreateViewfront        = ft.TextField(label="Front", hint_text="Ex: when jesus was born")
    CreateViewback         = ft.TextField(label="Back", hint_text="Ex: in year 0")
    CreateViewButton       = ft.CupertinoFilledButton("Create")
    CreateViewSwitch       = ft.Switch(value=True)
    CreateViewLabel        = ft.Text("create Card")
    CreateViewName         = ft.TextField(label="Name", hint_text="Science Deck")
    CreateViewDeckSelector = ft.Dropdown(options=[ft.dropdown.Option(value) for value in CardsBack.Decks])

    def CreateCard():
        pass

    def ChangePage(index):
        if index==0:
            page.clean()
            page.add(CreateViewSwitch)

            if CreateViewSwitch.value==False:
                CreateViewLabel.value = "create deck"
                if CreateViewSwitch.value == True:

                    CreateViewLabel.value = "create Card"
                    page.add(
                        CreateViewLabel,
                        CreateViewfront,
                        CreateViewback,
                        CreateViewButton,
                        CreateViewDeckSelector,
                    )
                page.add(CreateViewName)

            if CreateViewSwitch.value==True:

                if CreateViewSwitch == False:
                    CreateViewLabel.value = "create deck"
                    page.add(CreateViewName)

                CreateViewLabel.value = "create Card"
                page.add(
                    CreateViewLabel,
                    CreateViewfront,
                    CreateViewback,
                    CreateViewButton,
                    CreateViewDeckSelector,
            )

        if index==1:
            page.clean()
            page.add(ft.Text("all decks"))

    page.appbar = ft.CupertinoAppBar(
        leading=ft.Icon(ft.Icons.MY_LIBRARY_BOOKS),
        bgcolor=ft.Colors.GREY_900,
        trailing=ft.Icon(ft.Icons.IMAGE),
        middle=ft.Text("Cards Menu"),
    )

    page.navigation_bar=ft.CupertinoNavigationBar(
        bgcolor=ft.Colors.GREY_900,
        inactive_color=ft.Colors.GREY,
        active_color=ft.Colors.BLACK,
        on_change=lambda e:ChangePage(e.control.selected_index),
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.ADD, label="Create"),
            ft.NavigationBarDestination(icon=ft.Icons.BOOK, label="Learn"),
            ft.NavigationBarDestination(icon=ft.Icons.LIST, label="All")
        ]
    )
    page.clean()
    page.add(
        CreateViewfront,
        CreateViewback,
        CreateViewButton,
        CreateViewDeckSelector,
    )