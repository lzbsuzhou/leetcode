"""
6. Z字型变换
解法：将s按照“Z”逐个填入res中，最后将res合并
"""


class Solution:
	def convert(self, s: str, numRows: int) -> str:
		if numRows <= 1:
			return s
		res = ["" for _ in range(numRows)]
		i, flag = 0, -1
		for _s in s:
			if i == numRows - 1 or i == 0:
				flag = - flag
			res[i] += _s
			i += flag
		return "".join(res)


my_solution = Solution()
print(my_solution.convert("PAYPALISHIRING", 3))
