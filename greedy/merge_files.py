import math


def binary_search(el, array, low, high):
	if low > high:
		print(str(low) + '  ' + str(high))
		return -1
	else:
		mid = math.floor((high + low) / 2)
		if el < array[mid]:
			return binary_search(el, array, low, mid - 1)
		elif el > array[mid]:
			return binary_search(el, array, mid + 1, high)
		else:
			return mid


def binary_insert(el, array, low, high):
	if low > high:
		array.insert(low, el)
		return
	else:
		mid = math.floor((high + low) / 2)
		if el < array[mid]:
			return binary_insert(el, array, low, mid - 1)
		elif el > array[mid]:
			return binary_insert(el, array, mid + 1, high)
		else:
			array.insert(mid, el)
			return


def merge_files(f):
	# sort the files based on their lenghs
	f_copy = f.copy()
	f_copy.sort()

	total_merge_time = 0
	for i in range(0, len(f) - 1):
		merge_time_for_two_files = f_copy.pop(0) + f_copy.pop(0)
		binary_insert(merge_time_for_two_files, f_copy, 0, len(f_copy) - 1)
		total_merge_time += merge_time_for_two_files
	return total_merge_time


# f = [10, 5, 100, 50, 20, 15]
# f = [10, 10, 10, 15, 50]
f = [10, 10, 10, 10, 20, 20]
print(merge_files(f))

# f.sort()
# print(binary_insert(10, f, 0, len(f)))
