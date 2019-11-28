test_board = [' ']*10
#STEP 1: function that prints the board
def display_board(board):
	print("   |     |   ")
	print(f" {board[7]} |  {board[8]}  | {board[9]} ")
	print("   |     |   ")
	print("-------------")
	print("   |     |   ")
	print(f" {board[4]} |  {board[5]}  | {board[6]} ")
	print("   |     |   ")
	print("-------------")
	print("-------------")
	print("   |     |   ")
	print(f" {board[1]} |  {board[2]}  | {board[3]} ")
	print("   |     |   ")
	print("-------------")

#STEP 2: Take ina player input and assign a marker as X or O
def player_input():
	marker = ' '
	while marker != "X" and marker != "O":
		marker = input("Player 1, choose 'X' or 'O' ")
	player1 = marker
	if player1 == 'X':
		player2 = 'O'
	else:
		player2 = 'X'
	return(player1,player2)


#this sets the marker = to the output of the function player input
#player_input function asks X or 0 for player one and we can assign the markers below
player1_marker, player2_marker = player_input()

#STEP 3: Place the player input on the board
def place_marker(board, marker, position):
	board[position] = marker 


#STEP 4: Function that takes in a board and checks to see if someone has won
def win_check(board,mark):


#STEP 5: function that uses random to randomly decide which player gets to go first
import random
def choose_first():

#STEP 6: function that returns a boolean indicating whether a space on the board is freely available
def space_check(board, position):
	

#STEP 7: function that checks if the board is full and return a boolean value. true if full
def full_board_check(board):

#STEP 8: function that asks for a player's next position (as a number 1-9)
# and then uses the function from 
#step 6 to check if its a free position. If it is, then return the position for later use.
def player_choice(board):


#STEP 9: function that asks the player if they want to play again and returns booolean True if they do
def replay():
	

#STEP 10: Use while loops and the functions you've made to run the game.