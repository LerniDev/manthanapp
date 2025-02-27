import flet as ft
import json
Day=0
Decks={
    "Default": {},
}


class Cards(ft.Column):
    def __init__(self, front, back, page: ft.Page, deck, LearningStage=1, LastSeen=0):
        super().__init__()
        self.page=page
        self.LastSeen=LastSeen
        self.LearningStage=LearningStage
        self.SliderValue=2
        self.controls=[
            front,
            back,
            ft.Slider(min=0, max=100, divisions=10, label="{value}%")
        ]


        try:
            Decks[deck][front.value] = self
        except:
            Decks[deck]={}
            Decks[deck][front.value] = self

    def read(self):
        self.page.clean()
        self.page.add(self)

    def ChangeSliderValue(self):
        self.SliderValue=self.controls[3].value
        self.controls[2].value=str(self.SliderValue)

def updateDecksJson():
    with open("decks.json", "w", encoding="utf-8") as f:
        json.dump(Decks, f, indent=4)

def Learn(deck,page: ft.Page, TempList=[]):
    print(deck)
    keys = list(Decks[deck].keys())

    for i in Decks[deck].values():
        if i.LearningStage == 1:
            TempList.append(i)

    for i in TempList:
        page.clean()
        page.add(i)





















