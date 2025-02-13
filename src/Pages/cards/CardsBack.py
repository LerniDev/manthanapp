import flet as ft
import json
Decks={
    "Default": {},
}

class Cards(ft.Column):
    def __init__(self, front, back, page: ft.Page, deck):
        super().__init__()
        self.page=page
        Decks[deck][front]=self
        self.controls=[front, back]


        try:
            Decks[deck][front] = self
        except:
            Decks[deck]={}
            Decks[deck][front] = self

    def read(self):
        self.page.clean()
        self.page.add(self)

def updateDecksJson():
    with open("decks.json", "w", encoding="utf-8") as f:
        json.dump(Decks, f, indent=4)