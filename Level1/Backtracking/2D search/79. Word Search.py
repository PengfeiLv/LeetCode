# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 16:27
# @Author  : Lvpengfei


def exist(board, word):
	def backtracking(start, x, y):
		if start==len(word)-1:
			return True
		c = board[x][y]
		board[x][y] = '#'
		for (i,j) in [(x,y-1), (x, y+1), (x-1, y), (x+1, y)]:
			if 0<=i<len(board) and 0<=j<len(board[0]) and board[i][j]==word[start+1]:
				if backtracking(start+1, i, j):
					return True
		board[x][y] = c
		return False

	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j]==word[0] and backtracking(0, i, j):
				return True
	return False

if __name__ == "__main__":
	board = [['A', 'B', 'C', 'E'],
			 ['S', 'F', 'C', 'S'],
			 ['A', 'D', 'E', 'E']]
	word = 'ABCCED'
	print(exist(board, word))