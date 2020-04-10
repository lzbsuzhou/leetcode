# -*- coding:utf-8 -*-
import time


def select_sort(arr):
	for i in range(len(arr)-1):
		min_index = i
		for j in range(i+1, len(arr)):
			if arr[j] < arr[min_index]:
				min_index = j
		arr[i], arr[min_index] = arr[min_index], arr[i]


def bubble_sort(arr):
	for i in range(len(arr)-1, 0, -1):
		for j in range(i):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]


def insert_sort(arr):
	for i in range(1, len(arr)):
		for j in range(i, 0, -1):
			if arr[j] < arr[j-1]:
				arr[j], arr[j-1] = arr[j-1], arr[j]

def shell_sort(arr):
	n = len(arr)
	gap = n // 2
	while gap > 0:
		for i in range(gap, n):
			j = i
			while j >= gap:
				if arr[j] < arr[j-gap]:
					arr[j], arr[j-gap] = arr[j-gap], arr[j]
				j -= gap
		gap = gap // 2


def quick_sort(arr: list, start: int, end: int) -> None:
	if start >= end:  # 递归结束
		return
	mid = arr[start]
	low = start
	high = end
	while low < high:
		while low < high and mid <= arr[high]:
			high -= 1
		arr[low] = arr[high]
		while low < high and mid > arr[low]:
			low += 1
		arr[high] = arr[low]
	arr[low] = mid
	quick_sort(arr, start, low-1)
	quick_sort(arr, low+1, end)


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


def merge_sort(arr):
	if len(arr) <= 1:
		return arr
	num = len(arr) // 2
	left = merge_sort(arr[:num])
	right = merge_sort(arr[num:])
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
