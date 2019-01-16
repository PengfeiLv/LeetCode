# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 11:19
# @Author  : Lvpengfei

"""
本题中保证两个链表均无环
"""
# 方法一：直接法，先得到两个链表的长度，然后求出长度差，先遍历长链表，将两个链表对齐，然后同时往后遍历
def getIntersectionNode1(headA, headB):
	if not headA or not headB: return None
	a, b = headA, headB
	lena, lenb = 0, 0
	while a:
		a = a.next
		lena += 1
	while b:
		b = b.next
		lenb += 1

	if lena<lenb:
		headA, headB = headB, headA
		lena, lenb = lenb, lena
	cnt = lena - lenb
	a, b = headA, headB
	while cnt>0:
		a = a.next
		cnt -= 1
	while a and b:
		if a == b:
			return a
		a = a.next
		b = b.next
	return None

# 方法二：two-pointers
def getIntersectionNode2(headA, headB):
	a, b = headA, headB
	while a != b:
		a = a.next if a else headB  # 原理搞清楚
		b = b.next if b else headA
	return a  # 跳出while的情况分为两种：a==b!=None 此时a/b即为交点，a==b==None 此时无交点，返回None


