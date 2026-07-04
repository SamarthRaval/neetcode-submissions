class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        target = 0
        output = []
        length = len(nums)

        for i in range(length-2):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            if nums[i] > 0:
                break

            left = i+1
            right = length - 1

            while left < right:
                summ = nums[i] + nums[left] + nums[right]

                if summ < target:
                    left += 1
                
                elif summ > target:
                    right -= 1

                else:
                    output.append([nums[i], nums[left], nums[right]])
                    # [-4, -1, -1, 0, 1, 2]
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        
        return output

