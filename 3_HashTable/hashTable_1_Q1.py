def twoSum(nums, target):
    memo = {}
    for v in nums:
        memo[v] = 1         # key 값에 input으로 받은 nums들을 저장하고, value에는 dummy value를 넣어줌(value는 이 문제에서 따로 사용하지 않을 예정)

    for v in nums:
        needed_number = target - v
        if needed_number in memo:
            return True
    return False


nums = [2,7,11,15]
target = 9
twoSum(nums, target)