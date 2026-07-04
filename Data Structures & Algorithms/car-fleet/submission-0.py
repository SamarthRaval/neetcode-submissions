class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]
        pairs.sort(reverse=True) 
        stack = []

        for p, s in pairs:
            time_to_target = (target - p) / s
            stack.append(time_to_target)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)