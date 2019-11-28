import random
#Global Variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True

#class for card itself. 2 attributes. and you can print it out and it will report back the card and the suit
class Card():

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return self.rank + " of " + self.suit


class Deck():

	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))
	
	def __str__(self):
		deck_comp = ""
		for card in self.deck:
			deck_comp += '\n' + card.__str__()
		return "The deck has: " + deck_comp

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		single_card = self.deck.pop()
		return single_card

#testing out the deck to see if it worked
test_deck = Deck()
test_deck.shuffle()
print(test_deck)


#Creating a hand class
class Hand():

	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0
	def add_card(self,card):
		#card passed in is actually going to be from the Deck class
		#from Deck.deal() -->single Card(suit, rank)
		self.cards.append(card)
		self.value += values[card.rank]

		#Track aces
		if card.rank == "Ace":
			self.aces += 1
	def adjust_for_ace(self):

		#Ace is 11 unles its over 21
		#IF TOTAL VALUE > 21 AND I STILL HAVE AN ACE
		#THAN CHANGE MY ACE TO BE A 1 INSTEAD OF AN 11
		#0 as an int is treated as FALSE and any other int is treated as TRUE!!! same thing to say self.aces > 0
		while self.value > 21 and self.aces > 0:
			self.value -= 10
			self.aces -=1


#TESTING SECTION
test_deck = Deck()
test_deck.shuffle()
# PLAYER
test_player = Hand()
#Deal 1 card from the deck CARD(suit,rank)
pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)

test_player.add_card(test_deck.deal())
test_player.value
#END OF TESTING SECTION


class Chips():
	def __init__(self):
		self.total = 100 # This can be set to a default value or supplied by a user input
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet


def take_bet(chips):

	while True:

		try:
			chips.bet = int(input("How many chips would you like to bet? "))
		except:
			print("Sorry please provide an integer")
		else:
			if chips.bet > chips.total:
				print("Sorry, you do not have enough chips! you have: {}".format(chips.total))
			else:
				break

def hit(deck,hand):

	single_card = deck.deal()
	hand.add_card(single_card)
	hand.adjust_for_ace()



def hit_or_stand(deck, hand):
	global playing # to control an upcoming while loop

	while True:
		x = input("Hit or Stand? Enter h or s ")

		if x[0].lower() == 'h':
			hit(deck,hand)
		elif x[0].lower() == 's':
			print("Player Stands, Dealer's Turn")
			playing = False 
		else:
			print("Sorry, I did not understand that, please enter h or s only!")
			continue
		break


#Functions to display cards
def show_some(player,dealer):
	print("Dealers Hand: ")
	print("One Card Hidden! ")
	print(dealer.cards[1])
	print("\n")
	print("players hand: ")
	for card in player.cards:
		print(card)

def show_all(player,dealer):
	print("Dealer's Hand: ")
	for card in dealer.cards:
		print(card)
	print("\n")
	print("Players Hand: ")
	for card in player.cards:
		print(card)

#Write functions to handle end of the game scenarios
def player_busts(player,dealer,chips):
	print("Bust Player!")
	chips.lose_bet()

def player_wins(player,dealer,chips):
	print("Player Wins!")
	chips.win_bet()

def dealer_busts(player,dealer,chips):
	print("Player Wins! Dealer Busted")
	chips.win_bet()

def dealer_wins(player,dealer,chips):
	print("Dealer Wins!")
	chips.lose_bet()

def push(player,dealer,chips):
	print("Dealer and player tie! PUSH")



while True:
	#print openning statement

	print("Welcome to blackjack")
	deck = Deck()
	deck.shuffle()

	#create player hand and add two cards to it
	player_hand = Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	#create dealer hand and add two cards to it
	dealer_hand = Hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())

	#Set up the player's chips
	player_chips = Chips()

	#Prompt player for their bet
	take_bet(player_chips)

	#Show cards (but keep on dealer card hidden)
	show_some(player_hand,dealer_hand)

	while playing:  #recall this variable from the hit_or_stand function
		#prompt to hit or stand
		hit_or_stand(deck, player_hand)

		#show cards (keep one dealer card hidden)
		show_some(player_hand, dealer_hand)

		#if player's hand exceeds 21, run player_busts() and break out of loop
		if player_hand.value > 21:
			player_busts(player_hand,dealer_hand,player_chips)
			break

	#if player hasn't busted, play dealer's hand until dealer reaches 17
	if player_hand.value <= 21:

		while dealer_hand.value < player_hand.value:
			hit(deck,dealer_hand)

		#show all cards
		show_all(player_hand,dealer_hand)

		#run different winning scenarios
		if dealer_hand.value > 21:
			dealer_busts(player_hand, dealer_hand, player_chips)
		elif dealer_hand.value > player_hand.value:
			dealer_wins(player_hand, dealer_hand, player_chips)
		elif dealer_hand.value < player_hand.value:
			player_wins(player_hand, dealer_hand, player_chips)
		else:
			push(player_hand,dealer_hand,player_chips)

		#inform player of their chips total
	print("\n Player total chips are at: {}".format(player_chips.total))
		#ask to play again
	new_game = input("Would you like to play another hand? y/n: ")

	if new_game[0].lower() == 'y':
		playing = True
		continue
	else:
		print("Thank you for playing!")

		break
