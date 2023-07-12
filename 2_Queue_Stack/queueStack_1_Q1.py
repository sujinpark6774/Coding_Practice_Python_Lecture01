def isValid(s):
    stack = []
    for p in s:
        if p == "(":
            stack.append(")")
        elif p == "{":
            stack.append("}")
        elif p == "[":
            stack.append("]")
        elif not stack or stack.pop() != p:
            return False
    return not stack    # stack이 비어있으면 True 반환
    

input = "{(([]))[]}"
result = isValid(input)
result