# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 14:30
# @Author  : Lvpengfei


def mergeTwoLists(l1, l2):
	dummy = head = ListNode(0)
	while l1 and l2:
		if l1.val <= l2.val:
			head.next = l1
			l1 = l1.next
		else:
			head.next = l2
			l2 = l2.next
		head = head.next
	head.next = l1 if l1 else l2
	return dummy.next


if __name__ == '__main__':
	for i in range(1, 101):
		print(str(i)+'. ')

