class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Create a dictionary to store the value and its index
        num_to_index = dict()
        
        for index, val in enumerate(nums):
            # Check if the complement (target - val) exists in the dictionary
            if target - val in num_to_index:
                # If found, return the indices that sum up to the target
                return [num_to_index[target - val], index]
            
            # Store the current value and its index in the dictionary
            num_to_index[val] = index
        
        # If no solution is found, return an empty list
        return []
    
if __name__ == "__main__":
    solution = Solution()

    nums = [2, 7, 11, 15]
    target = 9

    assert solution.twoSum(nums, target) == [0,1] or [1,0], f"Test case 1 failed: {solution.twoSum(nums, target)}"

    nums = [3, 2, 4]
    target = 6

    assert solution.twoSum(nums, target) == [1,2] or [2,1], f"Test case 1 failed: {solution.twoSum(nums, target)}"

    nums = [3, 3]
    target = 6

    assert solution.twoSum(nums, target) == [0,1] or [1,0], f"Test case 1 failed: {solution.twoSum(nums, target)}"

    print("All test cases passed")