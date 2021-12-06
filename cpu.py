class Cpu:
    def __init__(self, name, game):
        self.name = name
        self.game = game
        self.health = 20
        self.mana = 2
        self.deck = []
        self.hand = []
        self.discardedCards = 0
        self.game.deck.shuffleDeck(self)
        self.game.deck.drawCards(self, 7, 0)
