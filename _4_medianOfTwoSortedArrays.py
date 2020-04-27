class Solution:
	def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
		len_num1, len_num2 = len(nums1), len(nums2)
		len_sum = len_num1 + len_num2
		index_1, index_2 = 0, 0
		result = 0
		if len_sum % 2 == 0:  # 共偶数个数
			last_num, cur_num = 0, 0
			while index_1 + index_2 <= len_sum / 2:
				print(index_1, index_2)
				last_num = cur_num
				if index_1 >= len_num1:
					index_2 += 1
					cur_num = nums2[index_2]
				elif index_2 >= len_num2:
					cur_num = nums1[index_1]
					index_1 += 1
				elif nums1[index_1] < nums2[index_2]:
					cur_num = nums1[index_1]
					index_1 += 1
				else:
					cur_num = nums2[index_2]
					index_2 += 1
			result = (last_num + cur_num) / 2
		else:  # 共奇数个数
			while index_1 + index_2 <= len_sum // 2:
				if index_1 >= len_num1:
					result = nums2[index_2]
					index_2 += 1
				elif index_2 >= len_num2:
					result = nums1[index_1]
					index_1 += 1
				elif nums1[index_1] < nums2[index_2]:
					result = nums1[index_1]
					index_1 += 1
				else:
					result = nums2[index_2]
					index_2 += 1
		return result


if __name__ == "__main__":
	solution = Solution()
	print(solution.findMedianSortedArrays([1, 2], [3, 4]))

