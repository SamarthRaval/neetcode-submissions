class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        output = [0] * length
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_temp_idx = stack.pop()
                output[prev_temp_idx] = i - prev_temp_idx
            stack.append(i)

        return output