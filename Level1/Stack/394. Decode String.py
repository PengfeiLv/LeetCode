# -*- coding: utf-8 -*-
# @Time    : 2019/1/22 15:14
# @Author  : Lvpengfei


def decodeString(s):
	cstr, stack, cnum = "", [], 0
	for c in s:
		if c.isdigit():
			cnum = cnum * 10 + int(c)
		elif c == '[':
			stack.append(cstr)
			stack.append(cnum)
			cstr = ""
			cnum = 0
		elif c == ']':
			pnum = stack.pop()
			pstr = stack.pop()
			cstr = pstr + pnum * cstr
		else:
			cstr += c
	return cstr


if __name__ == "__main__":
	s = "a2[sd2[s]]f"
	print(decodeString(s))