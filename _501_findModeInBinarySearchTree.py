'''
题解：
1. 中序遍历树的所有节点，将 "数" 以及出现的 "次数" 存在字典中
2. 字典的 "次数" 最大值为索引，找出众数

注意点:
1. leetcode中避免出现全局变量

问题:
1. 开辟了额外的空间，即存储 "数: 次数" 的字典
'''


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def add_node(node: TreeNode, x, dir):
	new_node = TreeNode(x)
	if dir == "left":
		node.left = new_node
	else:
		node.right = new_node


class Solution:
	def findMode(self, root: TreeNode):
		TIME_DICT = dict()
		def mid_traverse(node: TreeNode):
			if node is None:
				return
			mid_traverse(node.left)
			cur_val = node.val
			if cur_val in TIME_DICT.keys():
				TIME_DICT[cur_val] += 1
			else:
				TIME_DICT[cur_val] = 1
			mid_traverse(node.right)
		if root is None:
			return []
		if root.left is None and root.right is None:
			return [root.val]
		mid_traverse(root)
		max_time = max(TIME_DICT.values())
		result = list()
		for key in TIME_DICT.keys():
			if TIME_DICT[key] == max_time:
				result.append(key)
		return result


if __name__ == "__main__":
	solution = Solution()
	my_tree = TreeNode(2)
	add_node(my_tree, 1, "left")
	add_node(my_tree, 4, "right")

	add_node(my_tree.right, 4, "left")
	add_node(my_tree.right, 7, "right")

	add_node(my_tree.right.left, 3, "left")
	add_node(my_tree.right.left, 4, "right")

	print(solution.findMode(my_tree))
