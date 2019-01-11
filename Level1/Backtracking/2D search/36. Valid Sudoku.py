# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 14:10
# @Author  : Lvpengfei


def isValidSudoku(board):
	def isValidRow(row):
		had = set()
		for c in board[row]:
			if c!='.' and c in had:
				return False
			had.add(c)
		return True

	def isValidCol(col):
		had = set()
		for i in range(9):
			c = board[i][col]
			if c!='.' and c in had:
				return False
			had.add(c)
		return True

	def isValidSquare(row, col):
		had = set()
		for i in range(3*(row//3), 3*(row//3)+3):
			for j in range(3*(col//3), 3*(col//3)+3):
				c = board[i][j]
				if c!='.' and c in had:
					return False
				had.add(c)
		return True

	for i in range(9):
		for j in range(9):
			if not (isValidRow(i) and isValidCol(j) and isValidSquare(i, j)):
				return False
	return True


def isValidSudoku1(board):
	for i in range(9):
		for j in range(9):
			if board[i][j]!='.':
				c = board[i][j]
				for k in range(9):
					if k!=j and board[i][k]==c: return False
					if k!=i and board[k][j]==c: return False
					if i!=(3*(i//3)+k//3) and j!=(3*(j//3)+k%3) and board[3*(i//3)+k//3][3*(j//3)+k%3]==c:
						return False
	return True


if __name__ == "__main__":
	board1 = [["5","3",".",".","7",".",".",".","."],
			  ["6",".",".","1","9","5",".",".","."],
			  [".","9","8",".",".",".",".","6","."],
			  ["8",".",".",".","6",".",".",".","3"],
			  ["4",".",".","8",".","3",".",".","1"],
			  ["7",".",".",".","2",".",".",".","6"],
			  [".","6",".",".",".",".","2","8","."],
			  [".",".",".","4","1","9",".",".","5"],
			  [".",".",".",".","8",".",".","7","9"]]
	board2 = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
	          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
	          [".", "9", "8", ".", ".", ".", ".", "6", "."],
	          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
	          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
	          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
	          [".", "6", ".", ".", ".", ".", "2", "8", "."],
	          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
	          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
	board3 = [[".",".","4",".",".",".","6","3","."],
	          [".",".",".",".",".",".",".",".","."],
	          ["5",".",".",".",".",".",".","9","."],
	          [".",".",".","5","6",".",".",".","."],
	          ["4",".","3",".",".",".",".",".","1"],
	          [".",".",".","7",".",".",".",".","."],
	          [".",".",".","5",".",".",".",".","."],
	          [".",".",".",".",".",".",".",".","."],
	          [".",".",".",".",".",".",".",".","."]]
	print(isValidSudoku(board1))
	print(isValidSudoku(board3))
	print(isValidSudoku1(board1))
	print(isValidSudoku1(board3))

