from deck import Deck

class Cpu:
    def __init__(self, name, game):
        self.name = name
        self.game = game
        self.health = 20
        self.mana = 2
        self.deck = Deck(self.game).shuffleDeck(self)
        self.hand = []
        self.discardedCards = 0
        Deck(self.game).drawCards(self, 7, 0)
