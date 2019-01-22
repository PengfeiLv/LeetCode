# -*- coding: utf-8 -*-
# @Time    : 2019/1/22 16:08
# @Author  : Lvpengfei


def reconstructQueue1(people):
	ret = [[] for _ in range(len(people))]
	people.sort(key=lambda x: x[0])  # 按身高从低到高排序
	for p in people:  # 每次寻找最低身高应处的位置
		cnt = -1
		for i in range(len(people)):
			if not ret[i] or ret[i][0] == p[0]:  # 空位置是比它高的，已经插入的最多和它一样高
				cnt += 1
			if cnt == p[1]:
				ret[i] = p
				break
	return ret

def reconstructQueue2(people):
	ret = []
	for p in sorted(people, key=lambda x:(-x[0], x[1])):  # 按身高降序，位次升序排列，这里必须指明第二个键为 x[1]
		ret.insert(p[1], p)
	return ret


if __name__ == '__main__':
	people = [[7,1], [4,4], [7,0], [5,0], [6,1], [5,2]]
	print(reconstructQueue2(people))