import flet as ft

Decks={
    "Default": {},
    "French": {},
}

class Cards(ft.Column):
    def __init__(self, front, back, page: ft.Page):
        super().__init__()
        self.page=page
        self.controls=[front, back]

    def read(self):
        self.page.clean()
        self.page.add(self)