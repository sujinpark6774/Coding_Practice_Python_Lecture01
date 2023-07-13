def longestConsecutive(nums):
    longest = 0
    num_dict = {}

    # 딕셔너리 생성 방법1
    # for num in nums:
    #     num_dict[num] = True

    # 딕셔너리 생성 방법2
    # num_dict = {x : True for x in nums}

    # 딕셔너리 생성 방법3
    num_dict = set(nums)

    # 연속된 숫자 중 가장 앞의 숫자일 경우 (count + 1)
    for num in num_dict:
        if num - 1 not in num_dict:
            cnt = 1
            target = num + 1
            while target in num_dict:
                target += 1
                cnt += 1
            longest = max(longest, cnt)
    return longest


# longestConsecutive(nums = [100,4,200,1,3,2])
longestConsecutive(nums = [6,7,100,5,4,4])