# -*- coding: utf-8 -*-
# @Time    : 2019/1/10 15:42
# @Author  : Lvpengfei


def myPow(x, n):
	if n==0: return 1
	if n==1: return x
	if n==2: return x*x
	if n<0:
		n, x = -n, 1/x
	return myPow(myPow(x, n//2), 2) if n%2==0 else x*myPow(myPow(x, n//2), 2)


if __name__ == '__main__':
	print(myPow(2.3, 9))