# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 14:57
# @Author  : Lvpengfei


def swapPairs(head):
	dummy = prev = ListNode(0)
	prev.next = head
	while prev.next and prev.next.next:
		a = prev.next
		b = prev.next.next
		# from pre->a->b->b.next to pre->b->a->b.next 一次性按顺序重新排列，不必考虑交换顺序
		# 只需对比交换前后的状态，即可直接交换，不会混淆
		prev.next, b.next, a.next = b, a, b.next
		prev = a
	return dummy.next  # 注意返回值

