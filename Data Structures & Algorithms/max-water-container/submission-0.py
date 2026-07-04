class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)

        start = 0
        end = length - 1
        max_water = float("-inf")

        while start < end:
            min_height = min(heights[start], heights[end])
            water = min_height * (end - start)

            max_water = max(max_water, water)

            if heights[start] <= heights[end]:
                start += 1
            else:
                end -= 1

        return max_water