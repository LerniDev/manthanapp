import flet as ft
import Pages.MainMenu
#from flet_navigator import *
#from flet_restyle import *

def main(page: ft.Page):
    # FletReStyle.apply_config(page, FletReStyleConfig())

    page.appbar = ft.CupertinoAppBar(
        leading=ft.Icon(ft.Icons.MY_LIBRARY_BOOKS),
        bgcolor=ft.Colors.GREY_900,
        trailing=ft.Icon(ft.Icons.IMAGE),
        middle=ft.Text("ManthanApp"),
    )

    #create the pages
    page.Pages={}
    page.Pages["MainMenu"]=Pages.MainMenu.mainmenu


    #call the page
    page.Pages["MainMenu"](page)


ft.app(main)
