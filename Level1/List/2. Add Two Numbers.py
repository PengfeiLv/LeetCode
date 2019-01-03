# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 17:32
# @Author  : Lvpengfei

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

def addTwoNumbers(l1, l2):
	ret = head = ListNode(0)
	carry = 0
	while l1 or l2 or carry:  # 注意最后的进位，可能两个列表都为空了，但进位 carry=1
		val1 = l1.val if l1 else 0
		val2 = l2.val if l2 else 0
		carry, val = divmod(sum([carry, val1, val2]), 10)
		head.next = ListNode(val)
		head = head.next
		l1 = l1.next if l1 else None
		l2 = l2.next if l2 else None
	return ret.next
