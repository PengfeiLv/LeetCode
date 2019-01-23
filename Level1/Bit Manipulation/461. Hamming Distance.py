# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 15:04
# @Author  : Lvpengfei


# 统计一个二进制数中 1 的个数
def hammingDistance1(x, y):
	ret = 0
	z = x ^ y
	while z > 0:  # 最简单易想的方法
		if z & 1:  # 最低位和 1 相与
			ret += 1
		z >>= 1  # 右移一位
	return ret

def hammingDistance2(x, y):
	ret = 0
	z = x ^ y
	while z > 0:
		ret += z & 1  # 与第一种一样
		z >>= 1
	return ret

def hammingDistance3(x, y):
	ret = 0
	z = x ^ y
	while z > 0:
		ret += 1
		z &= (z-1)  # 较快
	return ret



if __name__ == "__main__":
	print(hammingDistance1(1, 115))
	print(hammingDistance2(1, 115))
	print(hammingDistance3(1, 115))


