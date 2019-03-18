# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 16:08
# @Author  : Lvpengfei


def merge(num, start, mid, end, temp):
	"""合并两个有序到temp"""
	i, j, k = start, mid+1, 0
	while i<=mid and j<=end:
		if num[i]<num[j]:
			temp[k] = num[i]
			i += 1
		else:
			temp[k] = num[j]
			j += 1
		k += 1
	while i<=mid:
		temp[k] = num[i]
		k += 1
		i += 1
	while j<=end:
		temp[k] = num[j]
		k += 1
		j += 1
	for i in range(k):
		num[start+i] = temp[i]


def mergeSort(num, start, end, temp):
	if start < end:
		mid = start + (end - start) // 2
		mergeSort(num, start, mid, temp)  # 分治
		mergeSort(num, mid+1, end, temp)
		merge(num, start, mid, end, temp)  # 合并


def main(num, n):
	temp = [0]*n
	mergeSort(num, 0, n-1, temp)
	del temp
	return


if __name__ == "__main__":
	num = [9,8,7,6,5,4,3,2,1]
	main(num, len(num))
	print(num)