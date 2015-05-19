#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""blackjack project. test"""


import blackjack

card = blackjack.Card()
assert card.value == 1

deck = blackjack.Deck()
assert len(deck.cards) == 52

cstack = blackjack.CardStack(2)
assert len(cstack.stack) == 104
cstack.draw()
assert len(cstack.stack) == 103

hand = blackjack.Hand()
hand.update_cards(card)
assert hand.values[0] == 1
assert hand.values[1] == 11
num_players = int(raw_input('enter the number of player '))
num_players = int(num_players)
game = blackjack.MainGame(num_players)
assert len(game.cardstack.stack) == 52 * 8
game.play()
