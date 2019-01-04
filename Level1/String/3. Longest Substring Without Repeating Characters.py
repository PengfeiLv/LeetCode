# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 9:44
# @Author  : Lvpengfei

"""
抽象滑动窗口：hash+index
"""
def lengthOfLongestSubstring(s):
	last = {}
	start, ret = 0, 0
	for i, c in enumerate(s):
		if c in last and start<=last[c]:  # 重复字符，start之后第二次遇到该字符
			start = last[c] + 1  # 则从该字符上一次出现的位置之后start
		else:
			ret = max(ret, i-start+1)  # 不是重复字符，则更新最大长度
		last[c] = i  # 不论重复与否，都要更新成最新位置
	return ret


if __name__ == '__main__':
	s = 'aaaaaa'
	print(lengthOfLongestSubstring(s))


