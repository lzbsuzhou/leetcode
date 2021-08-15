"""
8. 字符串转换整数 (atoi)
"""

class Solution:
	def isPalindrome(self, x: int) -> bool:
		return str(x) == str(x)[::-1]


if __name__ == "__main__":
	solution = Solution()
	print(solution.isPalindrome(323))
