# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 14:36
# @Author  : Lvpengfei


def solveSudoku(board):
	def isValid(row, col, c):
		for i in range(9):
			if board[row][i]!='.' and board[row][i]==c: return False
			if board[i][col]!='.' and board[i][col]==c: return False
			if board[3*(row//3)+i//3][3*(col//3)+i%3]!='.' and board[3*(row//3)+i//3][3*(col//3)+i%3]==c:
				return False
		return True

	def findSpace():
		for i in range(9):
			for j in range(9):
				if board[i][j]=='.':
					return [i, j]
		return [-1, -1]

	def solver():
		x, y = findSpace()
		if x+1==0:
			return True
		for i in range(1, 10):
			c = str(i)
			if isValid(x, y, c):
				board[x][y] = c
				if solver():
					return True
				board[x][y] = '.'  # 回溯
		return False

	solver()


if __name__ == "__main__":
	board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
	          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
	          [".", "9", "8", ".", ".", ".", ".", "6", "."],
	          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
	          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
	          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
	          [".", "6", ".", ".", ".", ".", "2", "8", "."],
	          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
	          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
	solveSudoku(board)
	print(board)

