#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""blackjack project."""


# Import Python libs

import random
import copy


class Card():
    """
    Implement playing card
    """
    def __init__(self, value=1, rank="Ace", suit="Spades"):
        """ Card constructor
        args:

            value: card value or ranks in blackjack game
            rank: type of card (e.g. King)
            suit: shape of cards {Diamonds, Hearts, Spades, Clubs}
        """
        self.value = value
        self.rank = rank
        self.suit = suit

    def __str__(self):
        """ function that combine rank and suit into one string
            arg: None
            return:
                '{} of {}'.format(self.rank, self.suit
        """
        return '{} of {}'.format(self.rank, self.suit)


class Deck():
    """ deck of standard 52-card deck """

    ranks = [('Ace', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6),
             ('7', 7), ('8', 8), ('9', 9), ('10', 10),
             ('Jack', 10), ('Queen', 10), ('King', 10)]
    suits = ['Spades', 'Diamonds', 'Hearts', 'Clubs']

    def __init__(self):
        """ Deck constructor
        """
        self.cards = []
        for r in self.ranks:
            for s in self.suits:
                c = Card()
                c.rank = r[0]
                c.value = r[1]
                c.suit = s
                self.cards.append(c)


class Hand():
    """
        a function to implement blackjack hand.
        Hands keep track of player bets and
        value and ranks of card
    """

    def __init__(self, bet=1):
        self.cards = []
        self.values = []
        self.valid_moves = []
        self.bet = bet

    def update_cards(self, card):
        """
        Update properties when card is added

        card: type card
        return:None
        """
        self.cards.append(card)
        self.update_values()
        self.update_valid_moves()

    def update_valid_moves(self):
        """
        Update self.valid_moves to set of possible moves
        """

        moves = ['Stay']

        # case for 21
        for value in self.values:
            if value > 21:
                self.valid_moves = 'Bust'
                return
            if value == 21:
                if len(self.cards) == 2:
                    self.valid_moves = 'Blackjack'
                    return
                self.valid_moves = '21'
                return
        moves.append('Hit')

        if len(self.cards) <= 2:
            moves.append('Double')

        if len(self.cards) == 2:
            if self.cards[0].rank == self.cards[1].rank:
                moves.append('Split')

        self.valid_moves = moves

    def update_values(self):
        """
        Calculate value of hand

        return:
            string card
        """

        v = [0]
        has_ace = False

        # two values for hands with aces
        for card in self.cards:
            v[0] += card.value
            if card.rank == 'Ace':
                has_ace = True

        # hand is soft if below 12
        if has_ace:
            if v[0] < 12:
                v.append(v[0] + 10)

        self.values = v

    def __str__(self):
        return str([str(card) for card in self.cards])


class CardStack():
    """
    Implement a variable-sized show
    """

    def __init__(self, num_decks=1):
        """
        Build stack of decks and shuffle

        args:
            num_decks(defualt=1): number of decks (52) to use
        return:
            int; length of stack cards
        """

        self.stack = []
        for i in range(num_decks):
            deck = Deck()
            for card in deck.cards:
                self.stack.append(card)
        random.shuffle(self.stack)

    def draw(self):
        return self.stack.pop()

    def __len__(self):
        return len(self.stack)


class Player():
    def __init__(self, chips=100):
        self.chips = chips
        self.name = raw_input('what is player: ')

    def __str__(self):
        return 'Player  {} has'.format(self.name)

    def place_bet(self):
        print 'Player  {}: {} chips'.format(self.name, str(self.chips))
        bet = raw_input("Place your bet ('q' to quit): ")
        if bet == 'q' or bet == 'Q' :
            return bet

        while True:
            try:
                bet = int(bet)
                if bet < 1:
                    bet = int(raw_input('Bet is less than 1. Try again: '))
                elif self.chips - bet < 0:
                    bet = int(raw_input('whop!!, No chips. Try again: '))
                else:
                    break
            except ValueError:
                bet = raw_input('Not a valid bet. Try again: ')

        self.chips -= bet
        print 'chips: {}'.format(str(self.chips))
        return bet


    def make_move(self, hand):
        print '{} , make a move for: {}'.format(str(self), str(hand))
        moves_list = hand.valid_moves
        for i, move in enumerate(moves_list):
            strr = '{} : {}'.format(str(i), move)
            print 'Valid moves - {}'.format(strr)
        move = raw_input("Choose a move (e.g. '0'): ")
        while True:
            try:
                move = int(move)
                if move < 0 or move >= len(moves_list):
                    move = int(raw_input('Invalid move number. Choose again: '))

                # case of double down without enough chips
                elif moves_list[move] == 'Double':
                    if self.chips < hand.bet:
                        move = int(raw_input('Not enough chips to double. Choose again: '))
                    else:
                        self.chips -= hand.bet
                        break

                # case of split without enough chips
                elif moves_list[move] == 'Split':
                    if self.chips < hand.bet:
                        move = int(raw_input('Not enough chips to split. Choose again: '))
                    else:
                        self.chips -= hand.bet
                        break

                else:
                    break
            except ValueError:
                move = raw_input('Invalid move. try again: ')
        return moves_list[move]


class main_Game():
    """
    Implement a blackjack main_Game
    """

    def __init__(self, num_players=2, num_decks=8):
        # positions is list of players and their hands
        self.positions = []
        self.num_players = num_players
        self.num_decks = num_decks
        for i in xrange(num_players):
            self.positions.append([Player(), []])
        self.dealer = Hand()
        self.cardstack = CardStack(num_decks)
        self.chips = 0

    def play(self):
        """
        Play a main_Game of blackjack
        """

        print "Starting a new Game!\n"

        # play until all players quit
        while True:
            print "Starting a new round!\n"

            # new shoe if less than one deck remaining
            if len(self.cardstack) < 52:
                self.cardstack = CardStack(self.num_decks)

            # collect bets and reset lists of players and hands
            self.dealer = Hand()
            new_positions = []
            for player, hands in self.positions:
                bet = player.place_bet()
                if bet == 'q':
                    print player, 'quits!'
                    self.num_players -= 1
                    if self.num_players == 0:
                        print 'No more players. Game over.'
                        return
                    continue
                new_positions.append([player, [Hand(bet)]])
            self.positions = new_positions

            self.deal_cards()
            self.print_status()

            # handle dealer blackjack case
            if self.dealer.valid_moves == 'Blackjack':
                print 'Dealer blackjack! : '.format(str(card))
                print '\n'
                for player, hands in self.positions:
                    # push on player blackjack
                    if hands[0].valid_moves == 'Blackjack':
                        player.chips += hands[0].bet
                        print '{} pushes on dealer blackjack.'.format(str(player))
                        print '\n'
                continue

            # go through players' hands and take moves
            staying_hands = []
            for player, hands in self.positions:
                for hand in hands:

                    # loop until 21, bust, or stay
                    while True:
                        # check for 21 or blackjack
                        if hand.valid_moves == 'Blackjack':
                            print '{}  has blackjack and wins {} chips!'.format(str(player),str(2 * hand.bet))
                            print '\n'
                            player.chips += 2 * hand.bet
                            break
                        if hand.valid_moves == '21':
                            print '{} has 21'.format(str(player))
                            print '\n'
                            staying_hands.append([player, hand])
                            break

                        # if not 21, then get player move
                        selected_move = player.make_move(copy.deepcopy(hand))
                        if selected_move == 'Stay':
                            if len(hand.values) == 2:
                                print ' {} stays on soft '. format(str(player), str(hand.values[1]))
                                print '\n'
                            else:
                                print  '{} stays on  {} '.format(str(player), str(hand.values[0]))
                                print '\n'
                            staying_hands.append([player, hand])
                            break
                        if selected_move == 'Hit':
                            new_card = self.cardstack.draw()
                            print '{} hits and draws a'. format(player, new_card)
                            print '\n'
                            hand.update_cards(new_card)
                            if hand.valid_moves == 'Bust':
                                print 'Bust!'
                                print '\n'
                                break
                        if selected_move == 'Double':
                            new_card = self.cardstack.draw()
                            print ' {} doubles down and draws a {}'.format(player, new_card)
                            print '\n'
                            hand.update_cards(new_card)
                            hand.bet *= 2
                            if hand.valid_moves == 'Bust':
                                print 'Bust!, Bust!'
                                print '\n'
                                break
                            print '{} ends  round with  {}'.format(str(player), str(max(hand.values)))
                            print '\n'
                            staying_hands.append([player, hand])
                            break

                        # for splits, make two new Hands and insert them after the current hand
                        if selected_move == 'Split':
                            print '{} splits hand in two {} '.format(player, str(hand.cards[0].rank))
                            print '\n'
                            index = hands.index(hand) + 1
                            hand1 = Hand(hand.bet)
                            hand1.update_cards(hand.cards[0])
                            hand2 = Hand(hand.bet)
                            hand2.update_cards(hand.cards[1])
                            hands.insert(index, hand2)
                            hands.insert(index, hand1)
                            break

            # start new round  player is empty,
            if not staying_hands:
                continue

            # dealer's turn
            while True:
                dealer_soft = False
                if len(self.dealer.values) == 2:
                    dealer_soft = True
                    dealer_value = self.dealer.values[1]
                else:
                    dealer_value = self.dealer.values[0]

                # stay if more than 17 or hard 17
                test = (dealer_value == 17 and dealer_soft is False)
                if dealer_value > 17 or test:
                    break

                # hits on soft 17
                else:
                    card = self.cardstack.draw()
                    self.dealer.update_cards(card)
                    print 'Dealer hits and draws a {}'.format(str(card))
                    print '\n'

            # if dealer busts, then all staying hands win
            dealer_busted = False
            if self.dealer.valid_moves == 'Bust':
                print 'Dealer busts!\n'
                print '\n'
                dealer_busted = True
            else:
                print 'Dealer has hand: {}'.format(str(self.dealer))
                print '\n'
                print 'Dealer stays on: {}'.format( str(dealer_value))
                print '\n'
            for player, hand in staying_hands:
                # win
                if dealer_busted or max(hand.values) > max(self.dealer.values):
                    player.chips += 2 * hand.bet
                    playchips = '{} wins {} chips with hand: {} '
                    print playchips.format(str(player),str(2 * hand.bet), str(hand))
                # push
                elif max(hand.values) == max(self.dealer.values):
                    player.chips += hand.bet
                    playchip = "{} have a pushes with hand: {} and won {}"
                    
                    print playchip.format(str(player), str(hand), str(hand.bet))
                # loss
                else:
                    print '{} loses with hand: {}'.format(str(player), str(hand))
            print '\nEnd of round.\n\n'

    def deal_cards(self):
        """
        Deal initial cards following casino order
        """
        for i in xrange(2):
            for player, hands in self.positions:
                hands[0].update_cards(self.cardstack.draw())
            self.dealer.update_cards(self.cardstack.draw())

    def print_status(self):
        """
        Print player hands, then print dealer hand
        """

        for player, hands in self.positions:
            print '-----------------------'
            print '-----------------------'
            print 'Player {}'. format(player.name)
            print '\n'
            for i, hand in enumerate(hands):
                print 'Hand  {} {}'.format(str(i), str(hand))
                print '\n'
            print '-----------------------'
            print '-----------------------'
        print 'Dealer: {}'.format(str(self.dealer))
        print '\n'
        print '-----------------------'
        print '-----------------------'
