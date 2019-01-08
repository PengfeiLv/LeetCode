# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 17:07
# @Author  : Lvpengfei

# 暴力
def strStr1(haystack, needle):
	if not needle: return 0
	l1, l2 = len(haystack), len(needle)
	if l2>l1: return -1
	for i in range(l1-l2+1):
		if haystack[i:i+l2]==needle:
			return i
	return -1

# KMP算法
def strStr2(haystack, needle):

	pass


if __name__ == '__main__':
	str1 = 'asahsnkj'
	str2 = 'hs'
	print(strStr1(str1, str2))
	print(strStr2(str1, str2))



