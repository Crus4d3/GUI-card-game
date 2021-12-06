class Card:
    def __init__(self, cardNum, name, cost, damage, cardText, game):
        self.cardNum = int(cardNum)
        self.cardName = name
        self.cardText = cardText
        self.cost = int(cost)
        self.damage = damage
        self.game = game

    def cast(self, caster, target):
        if caster.mana-self.cost>=0:
            print(caster.name, "has cast", self.cardName)
            caster.hand.remove(self)
            caster.discardedCards+=1
            caster.mana -= self.cost
            target.health-=self.damage
            print(self.cardName, "Deals", self.damage, "damage to", target.name)
            self.game.turnIncrement+=1
        else:
            print("{0} does not have enough mana to cast that card.".format(caster.name))
