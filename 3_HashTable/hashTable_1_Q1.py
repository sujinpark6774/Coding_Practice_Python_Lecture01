def twoSum(nums, target):
    memo = {}
    for v in nums:
        memo[v] = 1         # key 값에 input으로 받은 nums들을 저장하고, value에는 dummy value를 넣어줌(value는 이 문제에서 따로 사용하지 않을 예정)

    for v in nums:
        needed_number = target - v
        if needed_number in memo and v != needed_number:        # input으로 받은 숫자들 2번 사용하지 않는 조건을 뒤에 붙여줌
            return True
    return False


twoSum([4,1,9,7,8,2], 14)