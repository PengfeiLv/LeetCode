# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 11:33
# @Author  : Lvpengfei

"""
two-pointers 操作链表
"""
def removeNthFromEnd(head, n):
	dummy = ListNode(0)  # # 一定要新建一个dummy结点指向head，这样可以统一处理删除后为空结点的边界值
	dummy.next = head
	slow = dummy
	for _ in range(n):
		head = head.next
	while head:
		head = head.next
		slow = slow.next
	slow.next = slow.next.next
	return dummy.next
