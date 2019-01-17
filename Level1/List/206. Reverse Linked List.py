# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 9:37
# @Author  : Lvpengfei


# 方法一：迭代法 Time: O(N) Space: O(1)
def reverseList1(head):
	if not head or not head.next: return head
	prev, curr = None, head  # 仅需两个指针即可
	while curr:
		head = head.next
		curr.next = prev
		prev = curr
		curr = head
	return prev  # 注意返回的时 prev

# 方法二：递归法: 尾递归 Time: O(N) Space: O(1)
def reverseList2(head):
	def recursion(prev, head):
		if not head:
			return prev
		temp = head.next
		head.next = prev
		return recursion(head, temp)


