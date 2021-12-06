import random

from card import Card

class Deck:
    def __init__(self, game):
        self.cardsOwned = [
            'Basic attack',
            'Meditate*',
            'Heavy attack',
            'Signiture card'
        ]
        self.cardCost = {'Basic attack': 1, 'Meditate*': 0,
                'Heavy attack': 3, 'Signiture card': 5}
        self.cardDamage = {'Basic attack': 1,'Meditate*': 0,
                'Heavy attack': 3, 'Signiture card': 5}
        self.cardText = {'Basic attack': '','Meditate*': 'Regenerates 3 mana',
                    'Heavy attack': '', 'Signiture card': ''}
        self.game = game

    def shuffleDeck(self, comp):
        for i in range(0, 60):
            name = random.choice(self.cardsOwned)
            cost = self.cardCost[name]
            damage = self.cardDamage[name]
            cardText = self.cardText[name]
            card = Card(i, name, cost, damage, cardText, self.game)
            comp.deck.append(card)
        random.shuffle(comp.deck)

    def drawCards(self, comp, numCards, startingCard):
        for i in range(startingCard, startingCard + numCards):
            comp.hand.append(comp.deck[i])
