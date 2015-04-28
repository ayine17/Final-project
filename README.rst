============
Introduction
============
Blackjack, also known as twenty-one, is widely played casino banking
game in the world. Blackjack is a comparing card game between a player
and dealer. This means that players are competing against the dealer
and not against themselves. It is played with one or more decks of 52
cards. The purpose of the game is to beat the dealer, which can be
accomplished in the following ways:
    
 - Get 21 points (sum of the first two cards) on the player's first 
   two cards (called a blackjack), without a dealer blackjack; 
 - Reach a final score higher than the dealer without exceeding 21 (sum of all
   cards drawn); 
 - Let the dealer draw additional cards until his or her
   sum of cards at hand exceeds 21.

Two-card hand is initially distributed to the player or players and
they add together the value of their cards. Kings, queens, and jacks
are value as ten points and Ace can be count as 1 point or 11 points.
All other cards are counted as the numeric value shown on the card.
After receivingå their initial two cards, players have the option of
getting a "hit"-taking an additional card. The player or the dealer
wins by having a score of 21 or by having the highest score less than
21. A Score higher than 21 is called "busting" or "going bust" and
results in a loss. In the case where the dealer busts, all players
with final score less 21 wins. If a player holds an ace valued as 11
(sum of all cards), the hand is called "soft", meaning that the player
cannot go bust by taking an additional card because 11 plus any other
card will always bAe less than or equal to 21. Else, the hand is
"hard" meaning player can bust.

The dealer has to take hits until his
or her cards total 17 or more points. Players win if they have hands
less 21 and value is higher than the dealer's. The dealer loses if he
or she busts (greater than 21) or has a lesser hand than the player
who not busted. If the player and dealer have the same total, this is
called a "push" and the player does not win or lose.

The players' object is to win money by creating card totals that turn out to be
higher than the dealer's hand but do not exceed 21
("busting"/"breaking"), or alternatively by allowing the dealer to
take additional cards until he/she busts. On their turn, players must
choose whether to "hit" (take a card), "stand" (end their turn),
"double" (double wager, take a single card and finish), "split" (if
the two cards have the same value, separate them to make two hands) or
"surrender" (give up a half-bet and retire from the game). If the
dealer does not bust, each remaining players wins if its hand is
higher than the dealer's, and loses if it is lower. In the case of a
tied score, known as "push" or "standoff", bets are normally returned
without adjustment; however, a blackjack beats any hand that is not a
blackjack, even one with a value of 21. An outcome of blackjack vs.
blackjack results in a push. Wins are paid out at 1:1, or equal to the
wager, except for winning blackjacks, which are traditionally paid at
3:2 (meaning the player receives three dollars for every two bet), or
one-and-a-half times the wager. Blackjack games almost always provide
a side bet called insurance, which may be played when dealer's up card
is an ace. Additional side bets, such as "Dealer Match" which pays
when the player's cards match the dealer's up card, are sometimes
available. Main Goals: My goal in this project is write a program that
allows multiplayers and a dealer but not more than 6 players. It will
ask for the name of the players and their initial bets. At the
beginning of the game each player is given $100 worth of chips. When a
player makes a bet, the bet money is substrate from the initial $ 100.
At the end of each game, the each player name, total and number of
games played is print on the screen. Since this is a text base game,
the program will tell the user what is happening. For example, tell
him/her when he/she draws a card, the name of the card, when they
bust, win or when the dealer busted. Cards for the deck is randomly
select from the cards in the deck and the selected cards are remove
from the deck. At the end of each round, the deck will be reset to
include all cards before the next round starts. After receiving the
initial two cards, the players will have the following options: "hit",
"stand", "double down", or "split".

**Hit:**
    Take another card from the dealer. Stand: Take no more cards
    also known as "stand pat", "stick", or "stay".

**Double down:**
    Allowed player to increase the initial bet by up to 100%
    in exchange for committing to stand after receiving exactly one more
    card. The additional bet is placed in the betting box next to the
    original bet.

**Surrender:**
    When the player surrenders, he/she lost half of the bet and
    is taking out of the game at that round. He rejoin the after the round

**Insurance:**
    If the dealer's first is an ace, the program offered the to
    allow the player the option of taking "insurance" before the dealer
    second card is draw. The player may add up to half the value of their
    original bet to the insurance and these extra chips is placed on a
    portion of the table usually marked "Insurance pays 2 to 1".

**Split:**
    allow players to split the first two cards of a hand that have
    the same value into two hands and put a second bet equal to the first.
    The program separates the two cards and draws an additional card on
    each and associate one bet with each hand. The player then plays out
    the two separate hands in turn. The program should treat the hands as
    independent new hands and the player winning or losing their wager
    separately for each hand. I have not decided whether I will allow only
    identical hand like hand of 10-10 may be split or allow any hand of
    10-value cards to be splittable. Blackjacks after a split will be
    counted as non-blackjack 21 when comparing against the dealer's hand
    and hit will be allow after split.

Pay out
_______
    Blackjack is 1.5 times the player initial bet plus the bet.
    
    Normal wins and insurance bet is 2:1 or bet plus 1 time bet.


Personas:

Problem Scenario
+++++++++++++++++
My friend James has lost money playing blackjack game and wants a way
to learn to read cards.


Detail:
-------
James, who has recently lost money-playing blackjack, came to me with
an idea of learning to counting cards. The only way for him to learn
to count blackjack is by playing the game. However, he does not want
to spend money playing the game at casino or online since anytime
plays for money, he loss focus and stop keeping track of the cards. In
order for him to get use to keep track of cards while playing the
game, he want me to design a blackjack game for him use to practice a
home so he can learn to counting and keep of the cards. By playing
this game everyday, he will become use to keep track of the cards.
Therefore, he will be able to counting the cards in real game setting.
He thinks by practicing cards counting with a computer blackjack game,
he will be used to cards counting and cards counting will become
second nature weather he is playing at casino or computer.


User story
++++++++++

James Likes to play blackjack at casino and went me to a program for
him to play and learn how to read or count cards and other advantage
playing techniques.

Acceptance Stories:
-------------------
Knowing basic strategy for blackjack increases a player's chance of
winning. When a player acts on a guess, they can end up giving up a
big advantage, this is where strategizing and cards counting comes
into play.

Story:
``````
scenario 1:
```````````
when the first two cards are dealt and
dealer cards sum is 21, the dealer get blackjack. Then the dealer
should win and all the players’ loss

Scenario 2:
```````````
when cards are dealt and a player cards sum up 21, the
gets win with Blackjack and get paid 1.5.

Scenario 3:
```````````
when cards are dealt and neither the dealer nor players
did not cards add up to 21, the players can choose to stay or hit.
Hit take addition card to try to 21 or higher without bust. 

Scenario 4:
```````````
when cards are dealt and the dealer first card is ace,
the player can take “insurance” before the dealer draw the second
cards by add half of his/her original bet. Insurance is paid 2 to 1.
