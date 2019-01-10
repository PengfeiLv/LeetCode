# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 17:52
# @Author  : Lvpengfei

"""
方法一：暴力 O(N^2)  超时
	对每个元素a，找到它左边最大值left_maxi，右边最大值right_maxi，
	则此元素位置处所能存放的雨水为：min(left_maxi, right_maxi)-a
"""
def trap1(height):
	ret = 0
	for i in range(1, len(height)-1):
		left_maxi = right_maxi = 0
		for h in height[:i+1]:  # 搜索左右最大值时都要将该元素height[i]包含进去
			left_maxi = max(left_maxi, h)
		for h in height[i:]:
			right_maxi = max(right_maxi, h)
		ret += min(left_maxi, right_maxi) - height[i]  # 否则这里要判断min(left_maxi, right_maxi)与height[i]的大小关系
	return ret

"""
方法二：动态规划 O(N)
	与方法一中的计算公式是一样的，但我们可以用dp数组记录每个元素左右两侧的最大值
"""
def trap2(height):
	if not height: return 0
	ret, n = 0, len(height)
	left_dp = [height[0]]*n
	right_dp = [height[-1]]*n
	for i in range(1, n):
		left_dp[i] = max(left_dp[i-1], height[i])  # 记录截至到i位置的最大值
	for i in range(n-2, -1, -1):
		right_dp[i] = max(right_dp[i+1], height[i])
	for i in range(1, n-1):
		ret += min(left_dp[i], right_dp[i]) - height[i]
	return ret

"""
方法三：单调栈 stack
	栈中存放的是数组下标，本题是维持一个递减栈

"""
def trap3(height):
	ret, stack = 0, [0]
	for i in range(1, len(height)):
		while stack and height[stack[-1]]<height[i]:
			temp = stack.pop()
			if not stack:  # 最左边的边不能存水
				break
			h = min(height[i], height[stack[-1]]) - height[temp]
			w = i - stack[-1] - 1  # 注意这里不能是 w = i - temp，因为栈中的索引不一定是连续的
			ret += h * w
		stack.append(i)
	return ret

"""
方法四：two-pointers
	只要是双指针方法，肯定是O(N)且只需遍历一轮，

"""
def trap4(height):
	if not height: return 0
	ret = 0
	lt, rt = 0, len(height)-1
	lt_maxi, rt_maxi = 0, 0
	while lt < rt:
		if height[lt]<height[rt]:  # 左边<右边，则移动左边
			if height[lt]>=lt_maxi:
				lt_maxi = height[lt]
			else:
				ret += lt_maxi - height[lt]  # 哪边小，该位置存放的水就由哪边决定
			lt += 1
		else:  # 哪边小，移动哪边
			if height[rt]>=rt_maxi:
				rt_maxi = height[rt]
			else:
				ret += rt_maxi - height[rt]
			rt -= 1
	return ret


if __name__ == "__main__":
	nums = [0,1,0,2,1,0,1,3,2,1,2,1]
	print(trap1(nums))
	print(trap2(nums))
	print(trap3(nums))
	print(trap4(nums))



