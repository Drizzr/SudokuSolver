
emptyField = 0

field = [[1,2,0, 6,0,3, 0,5,0], # storing the Sodoku inside an array
			[0,6,0, 0,4,0, 9,7,0], 
			[7,0,8, 0,0,5, 0,3,2],
			#
			[0,3,0, 0,2,1, 7,0,9],
			[2,0,0, 9,0,7, 0,0,0],
			[0,9,0, 4,3,8, 2,0,6],
			#
			[0,7,0, 0,5,0, 0,6,3],
			[9,5,0, 0,0,0, 8,0,4],
			[6,0,2, 0,8,4, 0,0,7]
			]
		
def print_board():
	print("-" * 17)
	for row in field:
		for num in row:
			print(str(num), end = " ")
		print("")
	print("-" * 17)

def check_solved():
	count = 0
	for i in range(9):
		for j in range(9):
			if not number_possible(i, j, field[i][j]):
				field[i][j] = emptyField
				return False
			count += 1
	return True if count == 81 else False


def number_possible(x, y, number):
	for xi in range(9):
		if field[xi][y] == number:
			return False
	for yi in range(9):
		if field[x][yi] == number:
			return False
	for xi in range((x // 3)*3, (x // 3)*3 + 3):
		for yi in range((y // 3)*3, (y // 3)*3 + 3):
			if field[xi][yi] == number:
				return False
	return True

def smarty():
	for x in range(9):
		for y in range(9):
			if field[x][y] == emptyField:
				for number in range(1,10):
					if number_possible(x, y, number):
						field[x][y] = number
						smarty()
						field[x][y] = emptyField
				return
	#if check_solved:
	print_board()

if __name__ == "__main__":
	smarty()	

