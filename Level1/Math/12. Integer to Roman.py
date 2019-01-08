# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 10:00
# @Author  : Lvpengfei


def intToRoman(num):
	dic = {1000:'M', 900:'CM', 500:'D', 400:'CD',
	       100:'C', 90:'XC', 50:'L', 40:'XL',
	       10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
	ld = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
	ret = ''
	for n in ld:
		if num >= n:
			cnt, num = divmod(num, n)
			ret += cnt * dic[n]
	return ret


if __name__ == '__main__':
	num = 3445
	print(intToRoman(num))
