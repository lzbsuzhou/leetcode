"""
6. Z字型变换
解法：观察Z字结果，对于每一行，分析前后字符的index之差，以及与行的关系（./images/_7.jpg）
"""


class Solution:
	def convert(self, s: str, numRows: int) -> str:
		if numRows <= 1:
			return s
		result_str = ""  # 存放最后结果
		for row_cur in range(numRows):
			# --- 当前行的第一个字符 ---
			index_cur = row_cur
			if index_cur <= len(s) - 1:
				result_str += s[index_cur]
			else:
				break
			# --- 确定 索引增数 ---
			if row_cur in (numRows - 1, 0):  # 第一行 或 最后一行
				index_add_odd = 2 * (numRows - 1)
				index_add_even = 2 * (numRows - 1)
			else:  # 1 ~ numRows-1 行
				index_add_odd = 2 * (numRows - 1 - row_cur)
				index_add_even = 2 * row_cur
			# --- 添加后续的字符 ---
			while True:
				if index_cur + index_add_odd <= len(s) - 1:
					index_cur += index_add_odd
					result_str += s[index_cur]
				else:
					break
				if index_cur + index_add_even <= len(s) - 1:
					index_cur += index_add_even
					result_str += s[index_cur]
				else:
					break
		return result_str


my_solution = Solution()
print(my_solution.convert("abcdefghijklmn", 5))
