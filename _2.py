"""
题目：两数相加
按照普通加法的方式做即可
"""

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:

	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		cur_node0, cur_node1 = l1, l2
		result_node = ListNode(0)
		cur_node = result_node
		num_c = 0  # 进位
		while True:
			num0, num1 = 0, 0
			if cur_node0:
				num0 = cur_node0.val
				cur_node0 = cur_node0.next
			if cur_node1:
				num1 = cur_node1.val
				cur_node1 = cur_node1.next
			num = num0 + num1 + num_c
			if num < 10:
				num_c = 0
			else:
				num_c = 1
				num -= 10
			cur_node.val = num
			if not (cur_node0 or cur_node1):  # 两个链表都遍历结束
				if num_c == 1:
					cur_node.next = ListNode(1)
				break
			new_node = ListNode(0)
			cur_node.next = new_node
			cur_node = new_node
		return result_node


if __name__ == "__main__":
	solution = Solution()

	num_list0 = [2, 4, 5, 3]
	list_node0 = ListNode(num_list0[0])
	cur_node = list_node0
	for num in num_list0[1:]:
		node = ListNode(num)
		cur_node.next = node
		cur_node = node

	num_list1 = [1]
	list_node1 = ListNode(num_list1[0])
	cur_node = list_node1
	for num in num_list1[1:]:
		node = ListNode(num)
		cur_node.next = node
		cur_node = node

	result_node = solution.addTwoNumbers(list_node0, list_node1)
	cur_node = result_node
	while cur_node:
		print(cur_node.val, end="")
		cur_node = cur_node.next
