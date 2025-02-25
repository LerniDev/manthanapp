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
        Decks[deck][front]=self
        self.controls=[
            front,
            back,
            ft.Slider(min=0, max=100, divisions=10, label="{value}%")
        ]


        try:
            Decks[deck][front] = self
        except:
            Decks[deck]={}
            Decks[deck][front] = self

    def read(self):
        self.page.clean()
        self.page.add(self)

    def ChangeSliderValue(self):
        self.SliderValue=self.controls[3].value
        self.controls[2].value=str(self.SliderValue)

def updateDecksJson():
    with open("decks.json", "w", encoding="utf-8") as f:
        json.dump(Decks, f, indent=4)

def Learn(deck, TempList=[]):
    print(deck)
    """for card in deck.values():
        if card.LearningStage==1:
            TempList.append(card)
            card.read()
        if card.LearningStage>1:
            if Day%card.LastSeen==0:
                TempList.append(card)"""

    """for card in TempList:
        card.read()
        print(card)
        print(Decks[deck][card].controls)"""





















