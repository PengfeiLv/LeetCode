# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 10:28
# @Author  : Lvpengfei


def romanToInt(s):
	dic = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
	ret = 0
	for i in range(len(s)):
		if i + 1 < len(s) and dic[s[i]] < dic[s[i + 1]]:
			ret -= dic[s[i]]
		else:
			ret += dic[s[i]]
	return ret

if __name__ == '__main__':
	s = 'MMCDXLIV'
	print(romanToInt(s))

