class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		max_len = 0
		string = ""
		for str_single in s:
			if str_single in string:
				if max_len < len(string):
					max_len = len(string)
				max_index = string.rfind(str_single)
				string = string[max_index+1:] + str_single
			else:
				string += str_single
		if max_len < len(string):
			max_len = len(string)
		return max_len
