'''
This function draws a chessboard with pieces on it from scratch.

@params		board_dimension, a constant 8 for an 8 X 8 board

@return		seperated_gameBoard, returns gameboard seperated w
		with spaces so that it can be treated as a list 

'''
def draw_board(board_dimension):
		
	
	seperated_gameBoard = []

#Loop to create an  8 X 8 board

	for i in range(board_dimension):

			
		entered_row = ""

#Gets each row from user as an 8 character string				
		entered_row = input("Enter row # " + str(i + 1) + " of chessboard (1 is at the top of the board, 8 is the bottom row): ").strip(" ")
#Error check row
		valid = error_check_row(entered_row)

		while valid == False:

			print("Invalid row, please input a valid row: ")

			entered_row = input()

			valid = error_check_row(entered_row)

		seperated = ''

		final_seperated = ""
#Seperates each character in row string with a spaced so it can be converted to a list, which will then be added to the gameBoard list
			
		for char in entered_row:
				
			seperated = seperated + char + ' '

		final_seperated = seperated[:-1].split(' ')

				
		seperated_gameBoard.append(final_seperated)

			
	return seperated_gameBoard

'''
This function prints the chessboard the user most recently worked with to the console.

@params		gameBoard, a two-dimensional list of characters representing the chessboard 

@return		none

'''

def printBoard(gameBoard):
#Prints x-axis coordiantes labels 
	print("01234567")

#Prints board along with y-aaxis labels					
	for i in range(len(gameBoard)):
			
		for col in gameBoard[i]:
				
			print(col, end="")

		print("", i)

'''
This function checks the score of the game on the chessboard.

@params		gameBoard, a two-dimensional list of characters representing the chessboard 

@return		none

'''

def checkScore(gameBoard):

	blackScore = 0.0

	whiteScore = 0.0

		
	for i in range(len(gameBoard)):

#goes through every character of every row of the whole board and adds score for both colors based on what pieces are on the board			
		for lst in gameBoard[i]:

			for char in lst:

				if char == "q":

					whiteScore += 10

				elif char == "Q":

					blackScore += 10

				elif char == "r":

					whiteScore += 5

				elif char == "R":

					blackScore += 5

				elif char == "n":

					whiteScore += 3.5

				elif char == "N":

					blackScore += 3.5

				elif char == "b":

					whiteScore += 3

				elif char == "B":

					blackScore +=3


				elif char == "p":


					whiteScore += 1

				elif char == "P":


					blackScore +=1
#Displays both scores and who is winning
	if whiteScore == blackScore:


		print("White currently has a score of " + str(whiteScore) + " and Black currently has a score of " + str(blackScore) + ", the score is tied")


	elif whiteScore > blackScore:


		print("White currently has a score of " + str(whiteScore) + " and Black currently has a score of " + str(blackScore) + ", White is winning")

	elif blackScore > whiteScore:


		print("White currently has a score of " + str(whiteScore) + " and Black currently has a score of " + str(blackScore) + ", Black is winning")

'''
This function error checks each user entered row of the chessboard when drawing it from scratch.

@params		row_to_check, a string of characters representing a row of the chessboard 

@return		valid, returns True if the row is error free or returns False if the row 
		has an error

'''

def error_check_row(row_to_check):

	valid = True

	accepted_values = ["k", "K", "q", "Q", "b", "B", "n", "N", "r", "R", "p", "P", "-"]
#If the row is not 8 characters long, valid flag is False
	if len(row_to_check) != 8:

		valid = False

	else:

#If row contains a characters that is not one of the permitted characters, valid flag is false
		for char in row_to_check:

			if char not in accepted_values:

				valid = False

				break

#Returns True or False based on valid flag
	if valid == True:

		return True

	else:

		return False

'''
This function takes a piece on the chessboard and moves it to a spot the user specifies.

@params		gameBoard, a two-dimensional list of characters representing the chessboard

@return		gameBoard, a two-dimensional list of characters representing the chessboard
		with the pieces moved from the original

'''

def move_piece(gameBoard):
		
	pos = ""

	pos2 = ""
		
	piece = ""
						
	x_coordinate = 0

	y_coordinate = 0

	x_coordinate_2 = 0

	y_coordinate_2 = 0

	valid = False

#Gets position of piece to be moved 	
	pos = input("Please enter the location of the piece to be moved: ").strip(' ').strip('(').strip(')').split(',')
	x_coordinate = int(pos[0]); y_coordinate = int(pos[1])

#Error checking position to make sure there is a piece at the specified position and the position is on the board
	while valid == False:

		while x_coordinate < 0 or x_coordinate > 7 or y_coordinate < 0 or y_coordinate > 7:

			print("Invalid spot, please input a valid spot: ")

			pos = input().strip(' ').strip('(').strip(')').split(',')

			x_coordinate = int(pos[0]); y_coordinate = int(pos[1])

		piece = gameBoard[x_coordinate][y_coordinate]

				

		if piece == "-":

			print("No piece to move on this spot, please input a valid spot: ")

			pos = input().strip(' ').strip('(').strip(')').split(',')

			x_coordinate = int(pos[0]); y_coordinate = int(pos[1])

			while x_coordinate < 0 or x_coordinate > 7 or y_coordinate < 0 or y_coordinate > 7:

				print("Invalid spot, please input a valid spot: ")

				pos = input().strip(' ').strip('(').strip(')').split(',')

				x_coordinate = int(pos[0]); y_coordinate = int(pos[1])


			piece = gameBoard[x_coordinate][y_coordinate]

		else:
			valid = True

#Removes moved piece from the board and replaces it with a blank spot

	piece = gameBoard[x_coordinate].pop(y_coordinate)

	gameBoard[x_coordinate].insert(y_coordinate, "-")

#Gets position to move piece to
		
	pos2 = input("Please enter the location to move the piece to: ").strip(' ').strip('(').strip(')').split(',')

	x_coordinate_2 = int(pos2[0]); y_coordinate_2 = int(pos2[1])

#Error checks position to move piece to

	while x_coordinate_2 < 0 or x_coordinate_2 > 7 or y_coordinate_2 < 0 or y_coordinate_2 > 7:

		print("Invalid spot, please input a valid spot: ")

		pos2 = input().strip(' ').strip('(').strip(')').split(',')

		x_coordinate_2 = int(pos2[0]); y_coordinate_2 = int(pos2[1])
		
#Puts piece on new position
	gameBoard[x_coordinate_2].pop(y_coordinate_2)

	gameBoard[x_coordinate_2].insert(y_coordinate_2, piece)

	return gameBoard

'''
This is the main function, responsible for the user interface.

@params		none

@return		none

'''

def main():

	gameBoard = []

	board_dimension = 8 
	while True:

		print("NOTE: Capital letters define black pieces and lowercase letters define white pieces.")

		option = input("\nPlease enter a letter option for one of the options: \nA. Enter a new chessboard \nB. move a piece on most recent chessboard \nC. quit\n ")
#Error checks menu options		
		while option.upper() != "A" and option.upper()!= "B" and option.upper() != "C":

			print("Please enter a valid option from the list: ", end = '')
			option = input()

#Calls draw board function
		if option.upper() == "A":

			gameBoard = draw_board(board_dimension)
		
			printBoard(gameBoard)

			checkScore(gameBoard)
			
#Calls move function			
		elif option.upper() == "B":

			if gameBoard == []:

				print("A gameboard must first be created before you can move a piece!")

				gameBoard = draw_board(board_dimension)

				printBoard(gameBoard)

				checkScore(gameBoard)

			else:

				gameBoard = move_piece(gameBoard)

				printBoard(gameBoard)

				checkScore(gameBoard)

								
#Quits programme			
		elif option.upper() == "C":

			break

main()
