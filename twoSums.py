# Trishitha Dharmavaram
# 10-12-2025
# Solves the two-sum problem using loops and dictionaries.

def twoSumLoops(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

def twoSumDict(nums, target):
    d = {}
    for i, num in enumerate(nums):
        if target - num in d:
            return [d[target - num], i]
        d[num] = i
    return None

def twoSumLoopsAll(nums, target):
    result = []
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                result.append([i, j])
    return result

def twoSumDictAll(nums, target):
    result = []
    d = {}
    for i, num in enumerate(nums):
        if target - num in d:
            result.append([d[target - num], i])
        d[num] = i
    return result

def main():
    nums = [2, 7, 11, 15, 7]
    target = 9
    print("Two Sum Loops:", twoSumLoops(nums, target))
    print("Two Sum Dict:", twoSumDict(nums, target))
    print("Two Sum Loops All:", twoSumLoopsAll(nums, target))
    print("Two Sum Dict All:", twoSumDictAll(nums, target))

if __name__ == "__main__":
    main()
