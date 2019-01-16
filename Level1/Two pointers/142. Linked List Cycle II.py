# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 10:00
# @Author  : Lvpengfei


def detectCycle(head):
	if not head: return None
	fast = head.next
	slow = head
	while fast != slow:
		if not fast or not fast.next:
			return None
		fast = fast.next.next
		slow = slow.next
	fast = head       # fast重新指向头结点
	slow = slow.next  # slow先行一步
	while fast != slow:
		fast = fast.next
		slow = slow.next
	return fast
