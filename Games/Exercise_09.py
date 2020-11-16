'''
Create a function called DECK
Suit: H S C D - Ranks : A, 2 - 9, T J Q K
Return shuffled deck
'''


from random import shuffle


def deck():
    deck = []
    for suit in ['H', 'D', 'C', 'S']:
        for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']:
            deck.append(suit + rank)

    shuffle(deck)
    return deck


# A function for counting players cards
# Takes in the player's cards and returns the total points


def pointCount(myCards):
    myCount = 0
    aceCount = 0

    for i in myCards:
        if i[1] == 'J' or i[1] == 'Q' or i[1] == 'K' or i[1] == 'T':
            myCount += 10
        elif i[1] != 'A':
            myCount += int(i[1])
        else:
            aceCount += 1

        if aceCount == 1 and myCount <= 10:
            myCount += 11
        elif aceCount != 0:
            myCount += 1

    return myCount


# A function to create dealer's hand and player's hand
# Randomly gives each 2 cards from the deck
# Returns a list with both hands


def createPlayingHand(myDeck):
    dealerHand = []
    playerHand = []

    dealerHand.append(myDeck.pop())
    dealerHand.append(myDeck.pop())
    playerHand.append(myDeck.pop())
    playerHand.append(myDeck.pop())

    while pointCount(dealerHand) <= 16:
        dealerHand.append(myDeck.pop())

    return [dealerHand, playerHand]


# Create the game and loop it


game = True
myDeck = deck()
hand = createPlayingHand(myDeck)
dealer = hand[0]
player = hand[1]

while game:

    dealerCount = pointCount(dealer)
    playerCount = pointCount(player)

    print("Dealer has:")
    print(dealer[0])

    print("Player, you have:")
    print(player)
    print("Points: ", playerCount)

    if playerCount == 21:
        print("BLACKJACK!! Player you win")
        game = False

    elif playerCount > 21:
        print("BUST! Player you loose with " + str(playerCount) + " points.")
        game = False

    elif dealerCount > 21:
        print("Dealer BUST!! with " + str(dealerCount) + " points. Player WON!!!")
        game = False

    play = raw_input("Do you player want to HIT : 'H' or STAND : 'S'?")

    if play == 'H':
        player.append(myDeck.pop())

    elif playerCount > dealerCount:
        print("Player wins with " + str(playerCount) + " points")
        print("Dealer has " + str(dealerCount) + " points.")
        game = False

    else:
        print("Dealer Wins!!")
        print("Dealer has " + str(dealerCount) + " points.")
        game = False
