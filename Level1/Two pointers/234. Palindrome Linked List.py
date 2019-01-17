# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 14:06
# @Author  : Lvpengfei


def isPalindrome(head):
	if not head or not head.next: return True
	slow, fast = head, head.next
	while fast.next:
		slow, fast = slow.next, fast.next.next
	tail, slow.next = slow.next, None
	prev = None
	while tail:
		temp = tail.next
		tail.next = prev
		prev = tail
		tail = temp

	head2 = prev  # 注意反转之后，头结点为prev 而不是 tail，因为此时 tail为None
	while head and head2:
		if head.val != head2.val:
			return False
		head = head.next
		head2 = head2.next
	return True


