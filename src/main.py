import flet as ft
from Pages import MainMenu
from flet_navigator import *

def main(page: ft.Page):


    #create the pages
    page.Pages={}
    page.Pages["MainMenu"]=MainMenu.mainmenu(page)


    #set the current page
    page.CurrentPage="MainMenu"


    #call the page
    page.Pages[page.CurrentPage]()


ft.app(main)
