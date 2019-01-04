# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 12:46
# @Author  : Lvpengfei

def convert(s, numRows):
	if numRows == 1: return s  # 注意边界
	ret = ['']*min(numRows, len(s))  # 边界
	row, shift = 0, 1
	for i, c in enumerate(s):
		if row == 0:
			shift = 1
		if row == numRows - 1:
			shift = -1
		ret[row] += c
		row += shift
	return ''.join(ret)


if __name__ == '__main__':
	s = 'adsajdbkj'
	n = 1
	print(convert(s, n))


