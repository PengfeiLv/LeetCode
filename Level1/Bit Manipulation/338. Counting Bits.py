# -*- coding: utf-8 -*-
# @Time    : 2019/1/22 11:06
# @Author  : Lvpengfei


def countBits1(num):
	ret = [0, 1]
	while len(ret)<=num:
		ret += [i+1 for i in ret]  # 这规律难找出来吧
	return ret[:num+1]


def countBits2(num):
	num += 1
	ret = [0]*num
	for i in range(1, num):
		ret[i] = ret[i>>1] + (i & 1)  # 位操作
	return ret


if __name__ == "__main__":
	num = 8
	print(countBits1(num))
	print(countBits2(num))