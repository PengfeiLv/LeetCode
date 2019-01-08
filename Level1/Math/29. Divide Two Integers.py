# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 17:48
# @Author  : Lvpengfei


def divide(dividend, divisor):
	ret, mul = 0, 1
	sign = (dividend < 0) is (divisor < 0)
	dividend, divisor = abs(dividend), abs(divisor)
	while dividend >= divisor:
		dividend -= mul * divisor
		ret += mul
		mul *= 2
		if dividend < mul * divisor:
			mul = 1
	return min(ret, 2 ** 31 - 1) if sign else -ret


if __name__ == '__main__':
	print(divide(105, -50))
