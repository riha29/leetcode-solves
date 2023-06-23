# two sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]


# binary search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) <= 1 and nums[0] == target:
            return 0
        high = len(nums)-1
        low = 0
        while low <= high:
            mid = (high+low)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid+1
            if nums[mid] > target:
                high = mid-1
        if low > high:
            return -1


# search insert position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) <= 1:
            if nums[0] == target or nums[0] > target:
                return 0
            if nums[0] < target:
                return 1
        low = 0
        high = len(nums)-1
        if target not in nums:
            for i in range(len(nums)-1):
                if nums[-1] < target:
                    return len(nums)
                if nums[0] > target:
                    return 0
                if nums[i] < target < nums[i+1]:
                    return i+1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid+1
            if nums[mid] > target:
                high = mid-1
