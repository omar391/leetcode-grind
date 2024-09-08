from typing import List  # Import List from typing

def two_sum(nums: List[int], target: int) -> List[int]:
    m = {}
    for i, num in enumerate(nums):
        if target - num in m:
            return [m[target - num], i]
        m[num] = i
    return []

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))