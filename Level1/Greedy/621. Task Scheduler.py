# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 13:59
# @Author  : Lvpengfei


def leastInterval(tasks, n):
	ret, cnt = 0, {}
	for t in tasks:
		cnt[t] = cnt.get(t, 0) + 1
	freq = sorted(cnt.values(), reverse=True)

	while freq[0]>0:
		if freq[0] == 1:
			for i in range(len(freq)):
				ret += 1 if freq[i]>0 else 0
			return ret

		for i in range(n+1):
			if i<len(freq) and freq[i]>0:
				freq[i] -= 1
		ret += n+1
		freq.sort(reverse=True)



