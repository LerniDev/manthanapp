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

def Learn(deck, TempList=[]):
    print(deck)
    for card in Decks[deck]:
        if card.LearningStage==1:
            TempList.append(card)
        if card.LearningStage>1:
            if Day%card.LastSeen==0:
                TempList.append(card)
            TempList.append(card)
        print(card)
        print(Decks[deck][card].controls)


















