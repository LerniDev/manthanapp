import flet as ft
import Pages.MainMenu
from flet_navigator import *
#from flet_restyle import *

def main(page: ft.Page):
    #FletReStyle.apply_config(page, FletReStyleConfig())

    #create the pages
    page.Pages={}
    page.Pages["MainMenu"]=Pages.MainMenu.mainmenu


    #call the page
    page.Pages["MainMenu"](page)


ft.app(main)
