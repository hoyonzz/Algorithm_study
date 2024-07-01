# def recursive_function():
#     print("재귀 함수를 호출합니다.")
#     recursive_function()


# recursive_function()


# def recursive_function(i):
#     # 100번째 호출을 했을 때 종료되도록 종료 조건 명시
#     if i == 100:
#         return
#     print(i, "번째 함수에서", i + 1, "번째 재귀함수를 호출합니다.")
#     recursive_function(i + 1)
#     print(i, "번째 재귀함수를 종료합니다.")


# recursive_function(1)

# 팩토리얼 구현 예제
# n! = 1 * 2 * 3 * ... * (n-1) * n
# 수학적으로 0!과 1!의 값은 1입니다.
# 반복적으로 구현한 n!


# def factorial_iterative(n):
#     result = 1
#     # 1부터 n까지의 수를 차례대로 곱하기
#     for i in range(1, n + 1):
#         result *= i
#     return result


# def factorial_recursive(n):
#     # n이 1 이하인 경우 1을 반환
#     if n <= 1:
#         return 1
#     # n! = n * (m-1)!을 그대로 코드로 작성하기
#     return n * factorial_recursive(n - 1)


# print("반복적으로 구현:", factorial_iterative(5))
# print("재귀적으로 구현:", factorial_recursive(5))


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


print(gcd(192, 162))

# 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓입니다.
# 그래서 스택을 사용해야 할 때 구현상 스택 라이브러리 대신에 재귀 함수를 이용하는 경우가 많습니다.
