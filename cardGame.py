import random

class Game:
    def __init__(self):
            self.battleTurn=1
            self.turnIncrement=0
            self.battleEnd=False
            self.playerWin=False
            self.mulligan=0
            self.discardedCardsMap={0:0, 1:7, 2:7+6, 3:7+6+5, 4:7+6+5+4, 5:7+6+5+4+3, 6:7+6+5+4+3+2}
            self.numDiscardedCards=0

    def printHand(self, comp):
            for i in range(0, len(comp.hand)):
                    print(comp.hand[i].cardName)

    def mulliganHand(self, comp):
            mulligan=input("\nType (m) to mulligan your hand and draw a new one, or (s) to skip.\n")
            while mulligan in ['m', 'M', 'mulligan', 'Mulligan', 'MULLIGAN', 'draw', 'Draw',
                               'DRAW', 'redraw', 'Redraw', 'REDRAW'] and self.mulligan<7:
                    self.mulligan+=1
                    comp.hand=[]
                    deck.drawCards(comp, 7-self.mulligan, self.discardedCardsMap[self.mulligan])
                    comp.discardedCards+=self.discardedCardsMap[self.mulligan]
                    print(comp.discardedCards)
                    self.printHand(comp)
                    if self.mulligan<6:
                            mulligan=input("\nType (m) to mulligan your hand and draw a new one, or (s) to skip.\n")
                    else:
                            mulligan='No'

    def welcomeMessages(self):
            print("Welcome brave traveller to the unforgiving land of the Card open")
            print("It is a battleground where the strongest of foes pit their wits against each other.")
            print("All in the hopes to be crowned world card champion!")
            playerName = input("What is your name brave traveller?\n")
            return playerName

    def battleStart(self):
            print("\nYour first opponent is {0}.".format(cpu.name))
            if self.turnIncrement % 2 == 0:
                    print("You will be going first.")
            else:
                    print("You will be going second")
            print("\nYou have 20 health and 5 mana. \nYour starting hand is:")
            self.printHand(player)
            self.mulliganHand(player)

    def turnStart(self, regeneratedMana):
            if player.health<1:
                    self.battleEnd=True
                    self.playerWin=False
            print("\nIt is now your turn.")
            if regeneratedMana==False:
                    print("You regenerate 3 mana and draw a card.")
                    player.mana+=3
                    deck.drawCards(player, 1, player.discardedCards)
            print("You have", player.health, "health and", player.mana, "mana.")
            print("\nYour hand is:")
            self.printHand(player)

    def playerAction(self):
            action = input("\nType (x) to examine a card, (c) to cast a card or (?) for help.\n")
            if action in ['x', 'X', 'examine', 'Examine', 'EXAMINE']:
                    self.examineCard(player)
            if action in ['c', 'C', 'cast', 'Cast', 'CAST']:
                    self.castCard(player, cpu)
            if action in ['?', 'h', 'H', 'help', 'Help', 'HELP']:
                    self.helpMenu()
            if action in ['q', 'Q', 'quit', 'Quit', 'QUIT']:
                    self.quit()

    def examineCard(self, comp):
            print("Which card do you want to examine type 1 -", len(comp.hand))
            card = int(input())-1
            print("The card in your hand is {}.".format(comp.hand[card].cardName),
                    "It costs {} mana to use.".format(comp.hand[card].cost))
            print("It inflicts {} damage when cast.".format(comp.hand[card].damage))
            if comp.hand[card].cardText!= '':
                    print("The card text reads: {0}".format(comp.hand[card].cardText))

    def castCard(self, caster, target):
            print("Which card do you want to cast type 1 -", len(caster.hand))
            card = int(input())-1
            caster.hand[card].cast(caster, target)

    def helpMenu(self):
            print("Ummm.... \nWork it out...")

    def quit(self):
            print("Quitting game")
            self.turnIncrement=1
            self.battleEnd=True
            self.playerWin=False

    def cpuTurn(self, cpuRegeneratedMana):
            if cpu.health<1:
                    self.battleEnd=True
                    self.playerWin=True
            else:
                    print("\nIt is now {0}'s turn.".format(cpu.name))
                    if cpuRegeneratedMana==False:
                            print("{0} regenerates 3 mana.".format(cpu.name))
                            cpu.mana+=3
                    print(cpu.name, "now has", cpu.health, "health and", cpu.mana, "mana.\n")
                    card=random.randint(0,len(cpu.hand)-1)
                    #print("hand size is", len(cpu.hand), "chosen card is", card)
                    cpu.hand[card].cast(cpu, player)
                    self.battleTurn+=1

    def battleEnding(self):
            print("The battle is over!")
            if self.playerWin:
                    print("You win")
            else:
                    print("You lost")

class Card:
    def __init__(self, cardNum, name, cost, damage, cardText):
            self.cardNum = int(cardNum)
            self.cardName = name
            self.cardText = cardText
            self.cost = int(cost)
            self.damage = damage

    def cast(self, caster, target):
            if caster.mana-self.cost>=0:
                    print(caster.name, "has cast", self.cardName)
                    caster.hand.remove(self)
                    caster.discardedCards+=1
                    caster.mana -= self.cost
                    target.health-=self.damage
                    print(self.cardName, "Deals", self.damage, "damage to", target.name)
                    game.turnIncrement+=1
            else:
                    print("{0} does not have enough mana to cast that card.".format(caster.name))

class Deck:
    def __init__(self):
            self.cardsOwned = ['Basic attack', 'Meditate*', 'Heavy attack', 'Signiture card']
            self.cardCost = {'Basic attack': 1, 'Meditate*': 0,
            'Heavy attack': 3, 'Signiture card': 5}
            self.cardDamage = {'Basic attack': 1,'Meditate*': 0,
            'Heavy attack': 3, 'Signiture card': 5}
            self.cardText = {'Basic attack': '','Meditate*': 'Regenerates 3 mana',
            'Heavy attack': '', 'Signiture card': ''}

    def shuffleDeck(self, comp):
            for i in range(0, 60):
                    name = random.choice(self.cardsOwned)
                    cost = self.cardCost[name]
                    damage = self.cardDamage[name]
                    cardText = self.cardText[name]
                    card = Card(i, name, cost, damage, cardText)
                    comp.deck.append(card)
            random.shuffle(comp.deck)

    def drawCards(self, comp, numCards, startingCard):
            for i in range(startingCard, startingCard + numCards):
                    comp.hand.append(comp.deck[i])

class Player:
    def __init__(self, name):
            self.name = name
            self.health = 20
            self.mana = 2
            self.deck = []
            self.hand = []
            self.discardedCards = 0
            deck.shuffleDeck(self)
            deck.drawCards(self, 7, 0)

class Cpu:
    def __init__(self, name):
            self.name = name
            self.health = 20
            self.mana = 2
            self.deck = []
            self.hand = []
            self.discardedCards = 0
            deck.shuffleDeck(self)
            deck.drawCards(self, 7, 0)

game = Game()
deck = Deck()

playerName = game.welcomeMessages()
cpuName = "Lord Grendlefist"

player = Player(playerName)
cpu = Cpu(cpuName)

playerRegeneratedMana=False
cpuRegeneratedMana=False
game.battleStart()

while game.battleEnd==False:
    while game.turnIncrement % 2 == 0:
            game.turnStart(playerRegeneratedMana)
            game.playerAction()
            playerRegeneratedMana=True
            cpuRegeneratedMana=False
    while game.turnIncrement % 2 == 1:
            game.cpuTurn(cpuRegeneratedMana)
            cpuRegenerateMana=True
            playerRegeneratedMana=False

game.battleEnding()
