import flet as ft

def cardsmenu(page: ft.Page):
    page.clean()

    def ChangePage(index):
        if index==0:
            page.clean()
            page.add(
                ft.TextField(label="Front", hint_text="Ex: when jesus was born"),
                ft.TextField(label="Back", hint_text="Ex: in year 0")
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
        ft.TextField(label="Front", hint_text="Ex: when jesus was born"),
        ft.TextField(label="Back", hint_text="Ex: in year 0")
    )