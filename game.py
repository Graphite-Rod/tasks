class TicTacToe():
	def __init__(self):
		self.matrix = [" " for _ in range(9)]
		self.status = "X"

	def place(self, number):
		if number not in range(1, 10):
			return "INCORRECT_INPUT"
		else:
			if self.matrix[number-1] != " ":
				return "OCCUPIED"
			elif self.status in ["X", "O"]:
				self.matrix[number-1] = self.status
				self.status = "O" if self.status == "X" else "X"
				return "OK"
			else:
				return "GAME END"

	def check(self):
		scopes = []
		for i in range(3):
			scopes.append("".join(self.matrix[i*3:(i*3)+3]))
			scopes.append(self.matrix[i]+self.matrix[i+3]+self.matrix[i+6])
		scopes.append(self.matrix[0]+self.matrix[4]+self.matrix[8])
		scopes.append(self.matrix[2]+self.matrix[4]+self.matrix[6])
		for scope in scopes:
			if scope in ["XXX", "OOO"]:
				self.status = scope[0] + " WON"
				return scope[0] + " WON"
				break
		return "Continue"

	def reset(self):
		self.matrix = [" " for _ in range(9)]
		self.status = "X"
