"""
题目：二叉搜索树中的众数 - 解法2
解法：考虑到中序遍历是 不递减序列，所以考虑 val_last 和 val_cur 的值是否相同
"""


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
		# --- 中序遍历所有节点 ---
		def mid_traverse(node: TreeNode, data, result):
			if node is None:
				return
			mid_traverse(node.left, data, result)
			if data["first_node"]:
				# --- 处理第一个 ---
				data["first_node"] = False
				data["val_last"] = node.val
				result.append(data["val_last"])
			else:
				# --- 处理后续 ----
				val_cur = node.val
				if data["val_last"] == val_cur:
					data["time_last"] += 1
				else:
					data["time_last"] = 1
				if data["time_last"] == data["time_max"]:
					if val_cur not in result:
						result.append(val_cur)
				elif data["time_last"] > data["time_max"]:
					data["time_max"] += 1
					result.clear()
					result.append(val_cur)
			# print(node.val, data, result)
			data["val_last"] = node.val
			mid_traverse(node.right, data, result)

		result = list()
		if root is None:
			return []
		# --- root 节点 ---
		data = {"val_last": 0, "time_last": 1, "time_max": 1, "first_node": True}
		mid_traverse(root, data, result)
		return result


if __name__ == "__main__":
	solution = Solution()
	my_tree = TreeNode(1)
	# add_node(my_tree, 1, "left")
	add_node(my_tree, 4, "right")
	add_node(my_tree.right, 4, "right")


	print(solution.findMode(my_tree))
