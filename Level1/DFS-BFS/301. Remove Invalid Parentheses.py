# -*- coding: utf-8 -*-
# @Time    : 2019/1/18 16:52
# @Author  : Lvpengfei


def removeInvalidParentheses(s):
	left, right = 0, 0  # 记录错放的左括号、右括号的个数
	for c in s:
		if c == '(':
			left += 1
		elif c == ')':
			right = right + 1 if left==0 else right
			left = left - 1 if left>0 else left

	result = {}
	def recursion(s, index, left_count, right_count, left_rem, right_rem, expr):
		if index == len(s):
			if left_rem == 0 and right_rem == 0:
				ans = ''.join(expr)
				result[ans] = 1
		else:
			if s[index]=='(' and left_rem>0 or s[index]==')' and right_rem>0:
				recursion(s, index+1, left_count, right_count, left_rem-(s[index]=='('), right_rem-(s[index]==')'), expr)
			expr.append(s[index])

			if s[index]!='(' and s[index]!=')':
				recursion(s, index+1, left_count, right_count, left_rem, right_rem, expr)
			elif s[index]=='(':
				recursion(s, index+1, left_count+1, right_count, left_rem, right_rem, expr)
			elif s[index]==')' and left_count > right_count:
				recursion(s, index+1, left_count, right_count+1, left_rem, right_rem, expr)
			expr.pop()
	recursion(s, 0, 0, 0, left, right, [])
	return list(result.keys())


if __name__ == '__main__':
	s = '((a))))(())'
	print(removeInvalidParentheses(s))
