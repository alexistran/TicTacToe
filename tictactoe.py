class TicTacToe():
	def __init__(self, curr_player):
		self.board = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}
		self.curr_player = curr_player

	def display_board(self):
		#representing the board
		print(self.board[1] + " | " + self.board[2] + " | " + self.board[3])
		print(self.board[4] + " | " + self.board[5] + " | " + self.board[6])
		print(self.board[7] + " | " + self.board[8] + " | " + self.board[9])

	def whos_turn(self):
		return self.curr_player

	def switch_player(self):
		if self.curr_player == "Player 1":
			self.curr_player = "Player 2"
		else:
			self.curr_player = "Player 1"
	def get_move(self):
		while self.is_board_full() == False:
			print('What is your move ' + self.curr_player + "?")
			pos = input()
			if (pos in list(range(1, 10))) and (self.is_space_free(pos)):
				return pos
			else:
				print("Invalid move")

	def make_move(self):
		position = self.get_move()
		if self.curr_player == "Player 1":
			self.board[position] = "X"
		elif self.curr_player == "Player 2":
			self.board[position] = "O"

	def is_space_free(self, key):
		if self.board[key] == "":
			return True
		else: 
			return False

	def is_board_full(self):
		#board is a dictionary
		key = 1
		while key < 10:
			if self.board[key] == "":
				return False
			key+=1
		return True	
	def is_there_a_win(self):
		symbol = ""
		if self.curr_player == "Player 1":
			symbol = "X"
		elif self.curr_player == "Player 2":
			symbol = "O"
		if self.board[1] == symbol and self.board[2] == symbol and self.board[3] == symbol:
			return True
		elif self.board[4] == symbol and self.board[5] == symbol and self.board[6] == symbol:
			return True
		elif self.board[7] == symbol and self.board[8] == symbol and self.board[9] == symbol:
			return True
		elif self.board[1] == symbol and self.board[4] == symbol and self.board[7] == symbol:
			return True
		elif self.board[2] == symbol and self.board[5] == symbol and self.board[8] == symbol:
			return True
		elif self.board[3] == symbol and self.board[6] == symbol and self.board[9] == symbol:
			return True
		elif self.board[1] == symbol and self.board[5] == symbol and self.board[9] == symbol:
			return True
		elif self.board[3] == symbol and self.board[5] == symbol and self.board[7] == symbol:
			return True
		else:
			return False

def main():
		print("How to Play:")
		print("Grab a friend and play a fun game of tic tac toe! First player will be X and second player will be O. To input where you want your piece to go, type in a number from 1-9. 1 starts at the top upper left corner, and the numbers follow to the right, then down to next row, with 9 being the bottom right position. Have fun!")
		gameNotEnd = True
		game = TicTacToe("Player 1")
		game.display_board()
		while gameNotEnd:
			if game.is_board_full() and game.is_there_a_win == False:
				print("The game has ended. Its a tie!")
				break
			else:
				game.make_move()
				game.display_board()
				if game.is_there_a_win():
					print("Congratulations, " + game.curr_player + " has won!!!")
					break
				elif game.is_board_full() and game.is_there_a_win() == False:
					print("The game has ended. Its a tie!")
					break
				game.switch_player()
		

if __name__ == "__main__":
    main()