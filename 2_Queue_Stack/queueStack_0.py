################## Queue ##################

# queue 선언
q = []
# enqueue 0(1)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
# deqeue 0(n)
q.pop(0)
q.pop(0)
q.pop(0)

from collections import deque
queue = deque()
# enqueue() 0(1)
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
# deqeue() 0(1)
queue.popleft()
queue.popleft()
queue.popleft()

################## Stack ##################
# stack 선언
stack = []
# push 0(1)
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
# pop 0(1)
stack.pop()
stack.pop()
stack.pop()