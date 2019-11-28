def display_boards(r,c):
	for i in range(0,3):
		print("--------")
		for i in range(0,3):
			print("  |  ")
#two players play at same computer


#board should be printed out every time a player makes a move


#Accept input of the player position and then place a symbol on the board

#prompt user to select X or O
player1 = input("Please pick a marker 'X' or 'O': ")
#prompt user to enter a number
position = int(input("Please enter a number from 1 - 9: "))
#clear board
print('\n'*100)




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

#STEP 2: Take in a player input and assign a marker as X or O
def player_input():
	marker = " "
	#keep asking player 1 to choose X or O
	while marker != 'X' and marker != "O":
		marker = input("Player 1, choose X or O: ")
	#Assign player 2, the opposite Marker
	player1 = marker

	if player1 =="X":
		player2 = "O"
	else:
		player2 = "X"
	return (player1,player2)
#this sets the marker = to the output of the function player input
#player_input function asks X or 0 for player one and we can assign the markers below
player1_marker, player2_marker = player_input()

#STEP 3: Place the player input on the board
def place_marker(board, marker, position):
	board[position] = marker 

#STEP 4: Function that takes in a board and checks to see if someone has won
def win_check(board,mark):
	return ((board[7] == mark and board[8] == mark and board[9] == mark) or #check across top
	(board[4] == mark and board[5] == mark and board[6] == mark) or #check across middle
	(board[1] == mark and board[2] == mark and board[3] == mark) or #check across bottom
	(board[7] == mark and board[4] == mark and board[1] == mark) or #check down left
	(board[8] == mark and board[5] == mark and board[2] == mark) or #check down middle
	(board[9] == mark and board[6] == mark and board[3] == mark) or #check down right
	(board[7] == mark and board[5] == mark and board[3] == mark) or #check diagonal right
	(board[1] == mark and board[5] == mark and board[9] == mark)) or #check diagonal left

#STEP 5: function that uses random to randomly decide which player gets to go first
import random
def choose_first():
	if random.randint(0,1) == 0:
		return "Player 2"
	else:
		return "Player 1"
#STEP 6: function that returns a boolean indicating whether a space on the board is freely available
def space_check(board, position):
	return board[position] == " "

#STEP 7: function that checks if the board is full and return a boolean value. true if full
def full_board_check(board):
	for i in range(1,10):
		if space_check(board,i):
			return False
	return True 
#STEP 8: function that asks for a player's next position (as a number 1-9)
# and then uses the function from 
#step 6 to check if its a free position. If it is, then return the position for later use.
def player_choice(board):
	position = 0
	while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
		position = int(input("Choose your next position: (1-9) "))
	return position

#STEP 9: function that asks the player if they want to play again and returns booolean True if they do
def replay():
	return input("Do you want to play again? Enter Yes or No ").lower().startswith("y")






#STEP 10: Use while loops and the functions you've made to run the game.

print("Welcome to Tic Tac Toe!")

while True:
	#Reset the Board
	theBoard = [' '] * 10
	player1_marker,player2_marker = player_input()
	turn = choose_first
	print(turn + " will go first.")

	play_game = input("Are you ready to play? Enter Yes or No: ")

	if play_game.lower()[0] == 'y':
		game_on = True
	else:
		game_on = False

	while game_on:
		if turn == "Player 1":
			#Player 1's turn

			display_board(theBoard)
			position = player_choice(theBoard)
			place_marker(theBoard,player1_marker,position)

			if win_check(theBoard, player1_marker):
				display_board(theBoard)
				print("Congrats! You have won the game")
				game_on = False
			else:
				if full_board_check(theBoard):
					display_board(theBoard)
					print("The game is a draw!")
					break
				else:
					turn = "Player 2"
		else:
			#Player 2 turn

			display_board(theBoard)
			position = player_choice(theBoard)
			place_marker(theBoard, player2_marker,position)

			if win_check(theBoard,player2_marker):
				display_board(theBoard)
				print("Player 2 has won the game!")
				game_on = False
			else:
				if full_board_check(theBoard):
					display_board(theBoard)
					print("The game is a draw! ")
					break
				else:
					turn = "Player 1"
		if not replay():
			break



