#Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.


n = int(input("Enter number of bars: "))
heights = list(map(int, input("Enter bar heights: ").split()))

max_area = 0

for i in range(n):
    height = heights[i]

    left = i
    while left > 0 and heights[left - 1] >= height:
        left -= 1

    right = i
    while right < n - 1 and heights[right + 1] >= height:
        right += 1

    width = right - left + 1
    area = height * width

    if area > max_area:
        max_area = area

print("Largest rectangle area:", max_area)
