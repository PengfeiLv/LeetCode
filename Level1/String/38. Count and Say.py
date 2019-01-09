# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 16:03
# @Author  : Lvpengfei

"""
1.     1
2.     11
3.     21
4.     1211
5.     111221
前面几个如上所示，找出什么规律了吗？？？
"""

def countAndSay(n):
	if n==1: return '1'
	ret = '1'
	for _ in range(1, n):
		temp, cnt, say = '', 0, ret[0]
		for c in ret:
			if c==say:
				cnt += 1
			else:
				temp += str(cnt) + say
				say = c
				cnt = 1
		temp += str(cnt) + say
		ret = temp
	return ret


if __name__ == '__main__':
	for i in range(1, 10):
		print(countAndSay(i))