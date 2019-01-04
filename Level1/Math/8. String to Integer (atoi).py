# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 15:12
# @Author  : Lvpengfei


def myAtoi(str):
	ret, sign = 0, 1
	i = 0
	while i < len(str) and str[i]==' ':  # 找到第一个非空字符
		i += 1
	if i < len(str) and str[i] in ['-', '+']:  # 如果是符号位，记录符号，并跳到下一位
		sign = -1 if str[i] == '-' else 1
		i += 1
	while i < len(str) and str[i].isdigit():
		ret = ret * 10 + ord(str[i]) - ord('0')
		i += 1
	return max(-2**31, min(sign*ret, 2**31-1))  # 处理溢出


if __name__ == "__main__":
	s = '    -12357 567dasd'
	print(myAtoi(s))

