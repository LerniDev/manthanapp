import flet as ft

Decks={
    "Default": {}
}

class Cards(ft.Column):
    def __init__(self, front, back):
        super().__init__()
        self.controls=[front, back]


