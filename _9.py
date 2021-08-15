"""
9. 回文数
"""
class Solution:
	def isPalindrome(self, x: int) -> bool:
		x_str = str(x)
		if x_str[::-1] == x_str:
			return True
		else:
			return False


if __name__ == "__main__":
	solution = Solution()
	print(solution.isPalindrome(12321))
