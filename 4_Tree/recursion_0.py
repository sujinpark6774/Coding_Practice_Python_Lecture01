### 재귀함수 예시1. Factorial

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

factorial(3)


### 재귀함수 예시2. fibonacci

def fibo(n):
    if n == 1 or 2:
        return 1
    return fibo(n - 2) + fibo(n - 1)

fibo(3)