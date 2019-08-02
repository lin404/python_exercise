import random

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{values[self.rank]}  of {self.suit}'


class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n'+str(card)
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        deal_card = self.deck.pop()
        return deal_card


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self, card):
        #         self.cards.append(card)
        #         self.value += values[card.rank]
        #         print(card.rank)
        #         if card.rank == 'Ace':
        #             self.aces += 1
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('what is your bet '))
        except ValueError:
            print('Input a number')

        else:
            if chips.bet > chips.total:
                print(f'Your total is not enough: {chips.total}')
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    while True:
        x = input("Hit or Stand? ")
        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print('Please input h/s')
            continue

        break


def show_some(player, dealer):
    print(f"Dealer's hand: {dealer.cards[-1]}")
    print(f"Player's Hand: {[str(i) for i in player.cards]}")


def show_all(player, dealer):
    print(f"Dealer's hand: {[str(i) for i in dealer.cards]}")
    print(f"Player's Hand: {[str(i) for i in player.cards]}")


def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()


def push():
    print("Dealer and Player tie! It's a push.")


while True:
    print('Game Start')

    deck = Deck()
    deck.shuffle()

    player = Hand()
    player.add_card(deck.deal())
    player.add_card(deck.deal())

    dealer = Hand()
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())

    player_chips = Chips()
    take_bet(player_chips)

    show_some(player, dealer)

    while playing:  # recall this variable from our hit_or_stand function

        hit_or_stand(deck, player)
        show_some(player, dealer)

        if player.value > 21:
            dealer_busts(player, dealer, player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player.value <= 21:

        while dealer.value < 17:
            hit(deck, dealer)

        show_all(player, dealer)

        if dealer.value > 21:
            dealer_busts(player, dealer, player_chips)

        elif dealer.value > player.value:
            dealer(player, dealer, player_chips)

        elif dealer.value < player.value:
            player_wins(player, dealer, player_chips)

        else:
            push(player, dealer)

    # Inform Player of their chips total
    print(f"Player's winnings stand at {player_chips.total}")

    # Ask to play again
    play_again = input('Play again? (y/n) ')
    if play_again[0].lower() == 'y':
        playing = True
        continue
    else:
        break
