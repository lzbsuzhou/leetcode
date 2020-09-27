"""
约定：字符序列 0 ~ n-1
中心扩散法，按照 回文字符长度为 奇数和偶数 分开处理，最后取最长的
奇数：分别以字符的 1 ~ n-1-1 为中心，向两边扩散，寻找最长的回文字符
偶数：分别以字符的 0.5 ~ n-1-0.5 为中心，向两边扩散，寻找最长的回文字符
注意：需要注意字符长度过短的特殊情况
"""


class Solution:

	def longestPalindrome(self, s: str) -> str:
		s_len = len(s)
		if s_len <= 1:
			return s
		# --- 处理奇数个 ---
		longest_odd_str = s[0]
		if s_len <= 2:
			longest_odd_str = s[0]
		else:
			for i in range(1, s_len - 1):
				j = 1
				while i - j >= 0 and i + j <= s_len - 1:
					if s[i - j] == s[i + j]:
						j += 1
					else:
						break
				j -= 1
				if j * 2 + 1 > len(longest_odd_str):
					longest_odd_str = s[i - j:i + j + 1]
				# print("新序列：", j, " ", longest_odd_str)
		# --- 处理偶数 ---
		longest_even_str = ""
		if s_len <= 1:
			longest_even_str = ""
		else:
			for i in range(s_len - 1):
				cur_index = i + 0.5
				j = 0
				while cur_index - j - 0.5 >= 0 and cur_index + j + 0.5 <= s_len - 1:
					left_index = int(cur_index - j - 0.5)
					right_index = int(cur_index + j + 0.5)
					if s[left_index] == s[right_index]:
						j += 1
					else:
						break
				j -= 1
				left_index = int(cur_index - j - 0.5)
				right_index = int(cur_index + j + 0.5)
				if right_index - left_index + 1 > len(longest_even_str):
					longest_even_str = s[left_index:right_index + 1]
				# print("新序列：", j, " ", longest_even_str)
		if len(longest_even_str) > len(longest_odd_str):
			return longest_even_str
		else:
			return longest_odd_str


if __name__ == "__main__":
	solution = Solution()
	print(solution.longestPalindrome("cbbd"))
