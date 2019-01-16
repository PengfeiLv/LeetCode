# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 9:34
# @Author  : Lvpengfei


# two-pointers: Time: O(N) Space: O(1)
def hasCycle(head):
	if not head: return False
	fast = head.next
	slow = head
	while slow != fast:  # 将两个指针是否相等作为判断条件，可以进一步找出环入口结点
		if not fast or not fast.next:
			return False
		fast = fast.next.next
		slow = slow.next
	return True