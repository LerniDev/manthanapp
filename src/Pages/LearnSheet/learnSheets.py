import flet as ft

def learnSheetMenu(page:ft.Page):
    page.clean()

    page.appbar = ft.CupertinoAppBar(
        leading=ft.Icon(ft.Icons.MY_LIBRARY_BOOKS),
        bgcolor=ft.Colors.GREY_900,
        trailing=ft.Icon(ft.Icons.IMAGE),
        middle=ft.Text("LearnSheet Menu"),
    )

    page.navigation_bar = ft.CupertinoNavigationBar(
        bgcolor=ft.Colors.GREY_900,
        inactive_color=ft.Colors.GREY,
        active_color=ft.Colors.BLACK,
        on_change=lambda e: ChangePage(e.control.selected_index),
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.ADD, label="Create Mind Map"),
            ft.NavigationBarDestination(icon=ft.Icons.STACKED_BAR_CHART, label="Create Column LearnSheet"),
            ft.NavigationBarDestination(icon=ft.Icons.BOOK, label="view LearnSheets"),
            ft.NavigationBarDestination(icon=ft.Icons.LIST, label="MainMenu")
        ]
    )

    #to have no warning on pycharm
    page.Pages={}


    def ChangePage(index):
        if index==0:
            pass
        if index==1:
            pass
        if index==2:
            pass
        if index==3:
            page.Pages["MainMenu"](page)



