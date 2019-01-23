# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 11:00
# @Author  : Lvpengfei


def findAnagrams1(s, p):
	sp = sorted(p)
	ret, m, n = [], len(s), len(p)
	for i in range(m-n+1):
		t = sorted(s[i:i+n])  # 每次排序，费时，可能超时
		if t == sp:
			ret.append(i)
	return ret


# two_pointer 滑动窗口，记录窗口内的字符频次
def findAnagrams2(s, p):
	ret, pmap, smap = [], {}, {}
	for c in p:
		pmap[c] = pmap.get(c, 0) + 1

	m, n = len(s), len(p)
	for i in range(m):
		smap[s[i]] = smap.get(s[i], 0) + 1
		if i >= n:
			smap[s[i-n]] -= 1
			if smap[s[i-n]] == 0:
				smap.pop(s[i-n])
		if smap == pmap:
			ret.append(i-n+1)
	return ret


if __name__ == "__main__":
	s = "abcabca"
	p = "acb"
	print(findAnagrams1(s, p))
	print(findAnagrams2(s, p))


