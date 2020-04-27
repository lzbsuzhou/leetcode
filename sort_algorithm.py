# -*- coding:utf-8 -*-
import time


def select_sort(array):
	for i in range(len(array) - 1):
		min_index = i
		for j in range(i+1, len(array)):
			if array[j] < array[min_index]:
				min_index = j
		array[i], array[min_index] = array[min_index], array[i]


def bubble_sort(array):
	for i in range(len(array) - 1, 0, -1):
		for j in range(i):
			if array[j] > array[j + 1]:
				array[j], array[j + 1] = array[j + 1], array[j]


def insert_sort(array):
	for i in range(1, len(array)):
		for j in range(i, 0, -1):
			if array[j] < array[j - 1]:
				array[j], array[j - 1] = array[j - 1], array[j]


def shell_sort(array):
	n = len(array)
	gap = n // 2
	while gap > 0:
		for i in range(gap, n):
			j = i
			while j >= gap:
				if array[j] < array[j - gap]:
					array[j], array[j - gap] = array[j - gap], array[j]
				j -= gap
		gap = gap // 2


def quick_sort(array: list, start: int, end: int) -> None:
	if start >= end:  # 递归结束
		return
	mid = array[start]
	low = start
	high = end
	while low < high:
		while low < high and mid <= array[high]:
			high -= 1
		array[low] = array[high]
		while low < high and mid > array[low]:
			low += 1
		array[high] = array[low]
	array[low] = mid
	quick_sort(array, start, low - 1)
	quick_sort(array, low + 1, end)


def merge(left, right):  # 合并
	left_index = 0
	right_index = 0
	result = list()
	while left_index < len(left) and right_index < len(right):
		if left[left_index] < right[right_index]:
			result.append(left[left_index])
			left_index += 1
		else:
			result.append(right[right_index])
			right_index += 1
	result.extend(left[left_index:])
	result.extend(right[right_index:])
	return result


def merge_sort(array):
	if len(array) <= 1:
		return array
	num = len(array) // 2
	left = merge_sort(array[:num])
	right = merge_sort(array[num:])
	return merge(left, right)


if __name__ == "__main__":
	func_list = (merge_sort, quick_sort, shell_sort, insert_sort, bubble_sort, select_sort)
	for func in func_list:
		t_start = time.time()
		for _ in range(1000):
			# arr = [i for i in range(100, 0, -1)]
			arr = [1, 2, 0, -3, 23, 1, 4, 9, 11, 23, 43, 53, 123, 23, 0, 54, 23]
			if func == quick_sort:
				func(arr, 0, len(arr)-1)
			else:
				func(arr)
		t_end = time.time()
		print(func.__name__, ": ", t_end - t_start, "s")
