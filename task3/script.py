def golden_pyramid(triangle, row=0, column=0, total=0):
	if row == len(triangle) - 1:
		return total + triangle[row][column]
	return max(golden_pyramid(triangle, row + 1, column, total + triangle[row][column]),
			   golden_pyramid(triangle, row + 1, column + 1, total + triangle[row][column]))

def main():
	# count 18
	param = [[9,], [2, 2], [3, 3, 3],[4, 4, 4, 4]]

	# count 23
	param2 = [[1,], [2, 3], [3, 3, 1], [3, 1, 5, 4], [3, 1, 3, 1, 3], [2, 2, 2, 2, 2, 2], [5, 6, 4, 5, 6, 4, 3]]
	print(golden_pyramid(param))


if __name__ == '__main__':
	main()