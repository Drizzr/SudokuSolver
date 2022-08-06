import pygame
import sys
import time

pygame.init()

pygame.display.set_caption("auto_solver")


class Board:
	feld = [[0,2,0, 0,0,0, 0,4,3],
			[0,5,0, 3,0,7, 6,0,0],
			[0,0,6, 0,2,0, 0,0,0],
			#
			[0,0,3, 0,4,8, 0,9,0],
			[0,0,0, 0,6,0, 0,0,0],
			[0,9,0, 1,5,0, 2,0,0],
			#
			[0,0,0, 0,1,0, 3,0,0],
			[0,0,8, 5,0,6, 0,1,0],
			[7,1,0, 0,0,0, 0,5,0]
			]
		
	COLORS = {"green": (180,250,180), "red": (250,180,180), "white": (230,230,230)}
			
	def __init__(self):
		self.WIDTH = self.HEIGHT = 580
		self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		self.font = pygame.font.SysFont("Calibri", 50)
		self.size = self.HEIGHT//9
		self.emptyField = 0
		self.delay = int(input("delay: "))

	def check_keyboard_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

	def number_possible(self, x, y, number):
		for xi in range(9):
			if self.feld[xi][y] == number:
				return False
		for yi in range(9):
			if self.feld[x][yi] == number:
				return False
		for xi in range((x // 3)*3, (x // 3)*3 + 3):
			for yi in range((y // 3)*3, (y // 3)*3 + 3):
				if self.feld[xi][yi] == number:
					return False
		return True
		"""
		checks if the 'number' can be inserted at feld['x']['y']
		"""
		
	def end_loop(self):
		while True:
			self.check_keyboard_event()
			self.screen.fill(self.COLORS["green"])
			self.print_grit()
			pygame.display.update()
		"""
		draws the solved Sodoku on the screen
		"""		

	def smart_solver(self):
		for x in range(9):
			for y in range(9):
				if self.feld[x][y] == self.emptyField:
					for number in range(1,10):
						if self.number_possible(x, y, number):
							self.feld[x][y] = number		
							self.print_gamestate(x, y)
							time.sleep(self.delay)
							self.smart_solver()
							self.feld[x][y] = self.emptyField
					return
		self.end_loop()
	"""
	solves the Sudoku by backtracking
	"""

	def print_gamestate(self, x, y):
		self.check_keyboard_event()
		self.print_red(x, y)
		self.print_grit()
		pygame.display.update()
	"""
	prints the Sudoku on the screen whilst beeing solved by the smart_solver() function
	"""
	
	def print_red(self, x, y):
		self.screen.fill(self.COLORS["white"])
		for c in range(x+1):
			for b in range(9):
				pygame.draw.rect(self.screen, self.COLORS["red"], [b*self.size, (c-1)*self.size, self.size, self.size])
				if c == x:
					for b in range(y+1):
						pygame.draw.rect(self.screen, self.COLORS["red"], [b*self.size, (c)*self.size, self.size, self.size])
	"""
	prints the red squares (already solved) on the screen
	"""

	def print_grit(self):
		for i in range(9):
			for j in range(9):
				pygame.draw.rect(self.screen, (0,0,0), [j*self.size, i*self.size, self.size, self.size], 1)
				pygame.draw.rect(self.screen, (0,0,0), [(j//3)*self.HEIGHT//3, (i//3)*self.HEIGHT//3, self.HEIGHT//3, self.HEIGHT//3], 3)
				
				value = self.feld[i][j]
				if value != self.emptyField:
					rendered = self.font.render(str(value), True, (0,0,0))
					self.screen.blit(rendered, (j*self.size + 20, i*self.size + 8))
	"""
	prints the grit and the numbers on the screen
	"""


def main():
	board = Board()
	board.smart_solver()


if __name__ == "__main__":
	main()	

	
