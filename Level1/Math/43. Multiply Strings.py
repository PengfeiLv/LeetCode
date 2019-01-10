# -*- coding: utf-8 -*-
# @Time    : 2019/1/10 13:01
# @Author  : Lvpengfei

def multiply1(num1, num2):
	n1 = n2 = 0
	for c in num1:
		n1 *= 10
		n1 += ord(c) - ord('0')
	for c in num2:
		n2 *= 10
		n2 += ord(c) - ord('0')
	return str(n1*n2)


# 按乘法竖式的格式实现
def multiply2(num1, num2):
	m, n = len(num1), len(num2)
	ret = [0] * (m + n)
	for i in range(m - 1, -1, -1):
		for j in range(n - 1, -1, -1):
			mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
			hi, lo = i + j, i + j + 1
			mul += ret[lo]
			ret[hi] += mul // 10
			ret[lo] = mul % 10
	loc = -1
	for i in range(len(ret)):
		if ret[i] > 0:
			loc = i
			break
	return ''.join(map(str, ret[loc:]))


if __name__ == '__main__':
	num1 = '123'
	num2 = '456'
	print(multiply1(num1, num2))
	print(multiply2(num1, num2))

