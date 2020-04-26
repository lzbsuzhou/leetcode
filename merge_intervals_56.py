def merge_interval(list0, list1):
	if list0[1] < list1[0] or list0[0] > list1[1]:  # 无交集
		return None
	_min = min(list0[0], list1[0])
	_max = max(list0[1], list1[1])
	return [_min, _max]


class Solution:
	def merge(self, intervals):
		if not intervals:
			return []
		result = [intervals[0]]
		if len(intervals) == 1:
			return result
		for interval in intervals[1:]:
			while len(result) >= 1:
				temp = merge_interval(result[-1], interval)

				if not temp:  # 无交集
					result.append(interval)
					break
				else:
					interval = temp
					result.pop()
			if not result:
				result.append(interval)
		return result


if __name__ == "__main__":
	solution = Solution()
	arr = [[2, 3], [5, 5], [2, 2], [3, 4], [3, 4]]
	print(solution.merge(arr))
