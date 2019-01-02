# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 12:36
# @Author  : Lvpengfei


class Solution(object):
	def solveSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		self.backtrack(0, board)

	def backtrack(self, level, board):
		if level == 81:
			print(board)
			return True
		else:
			row = level // 9
			col = level % 9
			if board[row][col] == str('.'):
				for i in range(1, 10):
					board[row][col] = str(i)
					if self.check(level, board):
						if self.backtrack(level + 1, board):
							return True
				board[row][col] = '.'
			else:
				return  self.backtrack(level + 1, board)
		return False


	def check(self, level, board):
		row = level // 9
		col = level % 9
		# 检查所在行
		for i in range(9):
			if col != i and board[row][i] == board[row][col]:
				return False
		# 检查所在列
		for i in range(9):
			if row != i and board[i][col] == board[row][col]:
				return False
		# 检查所在3x3
		for i in range(3 * (row // 3), 3 * (row // 3 + 1)):
			for j in range(3 * (col // 3), 3 * (col // 3 + 1)):
				if row != i and col != j and board[row][col] == board[i][j]:
					return False
		return True


if __name__ == '__main__':
	board = [
		['5', '3', '.', '.', '7', '.', '.', '.', '.'],
		['6', '.', '.', '1', '9', '5', '.', '.', '.'],
		['.', '9', '8', '.', '.', '.', '.', '6', '.'],
		['8', '.', '.', '.', '6', '.', '.', '.', '3'],
		['4', '.', '.', '8', '.', '3', '.', '.', '1'],
		['7', '.', '.', '.', '2', '.', '.', '.', '6'],
		['.', '6', '.', '.', '.', '.', '2', '8', '.'],
		['.', '.', '.', '4', '1', '9', '.', '.', '5'],
		['.', '.', '.', '.', '8', '.', '.', '7', '9']]

	solu = Solution()
	solu.solveSudoku(board)
	print()
	for v in board:
		print(v)