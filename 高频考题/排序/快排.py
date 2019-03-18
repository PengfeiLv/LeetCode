# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 16:48
# @Author  : Lvpengfei
import random
import timeit


def partition(num, start, end):
	index = random.randint(start, end)
	pivot = num[index]
	num[end], num[index] = num[index], num[end]
	loc = start
	for i in range(start, end):
		if num[i]<pivot:
			num[i], num[loc] = num[loc], num[i]
			loc += 1
	num[loc], num[end] = num[end], num[loc]
	return loc


def quickSort1(num, start, end):
	if start<end:
		loc = partition(num, start, end)
		quickSort1(num, start, loc-1)
		quickSort1(num, loc+1, end)


# 用栈实现 非递归快排
def quickSort2(num, lo, hi):
	stack = []
	if lo < hi:
		mid = partition(num, lo, hi)
		if lo<mid-1:
			stack.append(lo)      # 左，首元素
			stack.append(mid-1)   # 左，尾元素
		if hi>mid+1:
			stack.append(mid+1)   # 右，首元素
			stack.append(hi)      # 右，尾元素

		while stack:
			q = stack[-1]  # 右尾
			stack.pop()
			p = stack[-1]  # 右首
			stack.pop()
			mid = partition(num, p, q)
			if p<mid-1:
				stack.append(p)
				stack.append(mid-1)
			if q>mid+1:
				stack.append(mid+1)
				stack.append(q)
	return


if __name__ == "__main__":
	num1 = list(range(10000))
	quickSort1(num1, 0, len(num1)-1)

	num2 = list(range(10000))
	quickSort2(num2, 0, len(num2)-1)
