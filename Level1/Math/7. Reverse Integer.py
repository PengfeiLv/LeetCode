# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 14:51
# @Author  : Lvpengfei


def reverse(x):
	neg = 1 if x < 0 else 0
	ret, x = 0, abs(x)
	while x > 9:
		x, rest = divmod(x, 10)
		ret = ret*10 + rest
	ret = ret * 10 + x  # 注意加上最后一位
	if neg:
		return 0 if -ret<(-2**31) else -ret
	return 0 if ret>2**31-1 else ret

if __name__ == '__main__':
	x = -123001
	print(reverse(x))