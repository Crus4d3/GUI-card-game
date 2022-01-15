import random

from deck import Deck
from player import Player
from cpu import Cpu

class Game:
    def __init__(self):
        self.battleTurn=1
        self.turnIncrement=0
        self.battleEnd=False
        self.playerWin=False
        self.mulligan=0
        self.discardedCardsMap={
            0:0,
            1:7,
            2:7+6,
            3:7+6+5,
            4:7+6+5+4,
            5:7+6+5+4+3,
            6:7+6+5+4+3+2,
        }
        self.numDiscardedCards=0

    def initGame(self):
        cpuName = "Lord Grendlefist"
        self.cpu = Cpu(cpuName, self)
        playerName = self.welcomeMessages()
        self.player = Player(playerName, self)

    def welcomeMessages(self):
        print("Welcome brave traveller to the unforgiving land of the Card open")
        print("It is a battleground where the strongest of foes pit their wits against each other.")
        print("All in the hopes to be crowned world card champion!")
        playerName = input("What is your name brave traveller?\n")
        return playerName

    def mulliganHand(self, comp):
        # This needs to be somehow moved into the actions class 
        # This is because both front ends will need to use it
        print("\nType (m) to mulligan your hand and draw a new one, or (s) to skip.")
        mulligan=input()
        mulligans = [ 'm', 'mulligan', 'draw', 'redraw' ]
        if mulligan.lower() in ['q', 'quit']:
            self.quit()
        while mulligan.lower() in mulligans and self.mulligan<7:
            self.mulligan+=1
            comp.hand=[]
            self.deck.drawCards(
                    comp,
                    7-self.mulligan,
                    self.discardedCardsMap[self.mulligan],
                    )
            comp.discardedCards+=self.discardedCardsMap[self.mulligan]
            print(comp.discardedCards)
            self.printHand(comp)
            if self.mulligan<6:
                print("\nType (m) to mulligan your hand and draw a new one,", "or (s) to skip.")
                mulligan=input()
            else:
                mulligan='No'

    def battleStart(self):
        print("Your first opponent is {0}.".format(self.cpu.name))
        if self.turnIncrement % 2 == 0:
            print("You will be going first.")
        else:
            print("You will be going second")
        print("\nYou have 20 health and 5 mana. \nYour starting hand is:")
        self.printHand(self.player)
        self.mulliganHand(self.player)

    def turnStart(self, regeneratedMana):
        if self.player.health<1:
            self.battleEnd=True
            self.playerWin=False
        print("\nIt is now your turn.")
        if regeneratedMana==False:
            print("You regenerate 3 mana and draw a card.")
            self.player.mana+=3
            self.deck.drawCards(self.player, 1, self.player.discardedCards)
        print("You have", self.player.health, "health and", self.player.mana, "mana.")
        print("\nYour hand is:")
        self.printHand(self.player)

    def playerAction(self):
        action = input("\nType (x) to examine a card, (c) to cast a card or (?) for help.\n")
        if action.lower() in ['x', 'examine']:
            self.examineCard(self.player)
        if action.lower() in ['c', 'cast']:
            self.castCard(self.player, self.cpu)
        if action.lower() in ['?', 'h', 'help']:
            self.helpMenu()
        if action.lower() in ['q', 'quit']:
            self.quit()

    def examineCard(self, comp):
        goodInput = False
        while goodInput == False:
            print("Which card do you want to examine type 1 -", len(comp.hand))
            card = input()
            try:
                card = int(card) - 1
                goodInput = True
            except:
                goodInput = False
        print("The card in your hand is {}.".format(comp.hand[card].cardName),
                "It costs {} mana to use.".format(comp.hand[card].cost))
        print("It inflicts {} damage when cast.".format(comp.hand[card].damage))
        if comp.hand[card].cardText!= '':
            print("The card text reads: {0}".format(comp.hand[card].cardText))

    def castCard(self, caster, target):
        goodInput = False
        while goodInput == False:
            print("Which card do you want to cast type 1 -", len(caster.hand))
            card = input()
            try:
                card = int(card) - 1
                goodInput = True
            except:
                goodInput = False
        caster.hand[card].cast(caster, target)

    def helpMenu(self):
        print("Ummm.... \nWork it out...")

    def quit(self):
        print("Quitting game")
        quit()

    def printHand(self, comp):
        for i in range(0, len(comp.hand)):
            print("[{}] {}".format(i+1, comp.hand[i].cardName))

    def cpuTurn(self, cpuRegenMana):
        if self.cpu.health<1:
            self.battleEnd=True
            self.playerWin=True
            self.battleTurn+=1
            self.turnIncrement+=1
            # return self.battleEnd, self.playerWin
        else:
            print("\nIt is now {0}'s turn.".format(self.cpu.name))
            if cpuRegenMana==False:
                print("{0} regenerates 3 mana.".format(self.cpu.name))
                self.cpu.mana+=3
            print(self.cpu.name, "now has", self.cpu.health, "health and", self.cpu.mana, "mana.\n")
            card=random.randint(0,len(self.cpu.hand)-1)
            #print("hand size is", len(self.cpu.hand), "chosen card is", card)
            self.cpu.hand[card].cast(self.cpu, self.player)
            self.battleTurn+=1

    def battleEnding(self):
        print("The battle is over!")
        if self.playerWin:
            print("You win")
        else:
            print("You lost")
        quit()

    def main(self):
        playerRegenMana=False
        cpuRegenMana=False
        while self.battleEnd==False:
            print("self.battleEnd:", self.battleEnd)
            print("self.turnIncrement:", self.turnIncrement)
            while self.turnIncrement % 2 == 0:
                self.turnStart(playerRegenMana)
                self.playerAction()
                playerRegenMana=True
                cpuRegenMana=False
            print("self.turnIncrement :", self.turnIncrement)
            while self.turnIncrement % 2 == 1:
                self.cpuTurn(cpuRegenMana)
                cpuRegenMana=True
                playerRegenMana=False
        self.battleEnding()
