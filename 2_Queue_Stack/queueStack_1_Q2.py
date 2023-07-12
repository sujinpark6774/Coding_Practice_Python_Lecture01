def dailyTemperatures(temperatures):
    ans = [0] * len(temperatures)
    stack = []
    for cur_day, cur_temp in enumerate(temperatures):
        while stack and stack[-1][1] < cur_temp:
            prev_day, _ = stack.pop()
            ans[prev_day] = cur_day - prev_day
        stack.append((cur_day, cur_temp))  # 튜플을 이용해서 날짜와 온도를 같이 저장
    return ans


temperatures = [73,74,75,71,69,72,76,73]
result = dailyTemperatures(temperatures)
result