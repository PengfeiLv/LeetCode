# -*- coding: utf-8 -*-
# @Time    : 2019/1/10 14:37
# @Author  : Lvpengfei


def rotate(matrix):
	def rotateEdge(x1, y1, x2, y2):  # 指定两个角的坐标，操作更方便
		"""(x1,y1): left_up point
		   (x2,y2): right_down point """
		for i in range(x2-x1):
			temp = matrix[x1][y1+i]
			matrix[x1][y1+i] = matrix[x2-i][y1]
			matrix[x2-i][y1] = matrix[x2][y2-i]
			matrix[x2][y2-i] = matrix[x1+i][y2]
			matrix[x1+i][y2] = temp


	n = len(matrix)
	for i in range(n//2):
		rotateEdge(i, i, n-1-i, n-1-i)


if __name__ == '__main__':
	matrix =[[5, 1, 9, 11],
			 [2, 4, 8, 10],
			 [13, 3, 6, 7],
			 [15, 14, 12, 16]]
	print(matrix)
	rotate(matrix)
	print(matrix)



