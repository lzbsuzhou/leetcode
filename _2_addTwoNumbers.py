# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		num0, num1 = 0, 0
		cur_node = l1
		mul_num = 1
		while cur_node:
			num0 = num0 + cur_node.val * mul_num
			mul_num *= 10
			cur_node = cur_node.next

		cur_node = l2
		mul_num = 1
		while cur_node:
			num1 = num1 + cur_node.val * mul_num
			mul_num *= 10
			cur_node = cur_node.next

		result_num = num0 + num1
		result_list = []
		result_node = ListNode(0)
		cur_node = result_node
		while result_num > 0:

			result_list.append(result_num % 10)
			result_num //= 10
		print(result_list)

		return result_node


if __name__ == "__main__":
	solution = Solution()

	num_list0 = [2, 4, 5]
	list_node0 = ListNode(num_list0[0])
	cur_node = list_node0
	for num in num_list0[1:]:
		node = ListNode(num)
		cur_node.next = node
		cur_node = node

	num_list1 = [1, 3, 6]
	list_node1 = ListNode(num_list1[0])
	cur_node = list_node1
	for num in num_list1[1:]:
		node = ListNode(num)
		cur_node.next = node
		cur_node = node

	solution.addTwoNumbers(list_node0, list_node1)
