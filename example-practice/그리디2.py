# #내 풀이
# n, k = map(int, input().split())
# count = 0  # 연산 횟수

# while n != 1:
#     if (n % k != 0):  # n이 k로 나누어 떨어지지 않을 때
#         n -= 1  # n에서 1을 뺀다
#         count += 1
#     if (n % k == 0):  # n이 k로 나누어 떨어질 때
#         n = n/k  # 실수형 반환
#         count += 1

# print(count)

# 답안 예시(시간복잡도 최적화)
n, k = map(int, input().split())
result = 0

while True:
    #n이 k로 나누어 떨어지는 수가 될 때까지 빼기
    target=(n//k)*k #n을 k로 나눈 몫과 k를 곱하면 n이 k로 나누어 떨어지는 수를 구할 수 있다.
    result+=(n-target) #n-target은 n이 k로 나누어질 때까지 -1연산을 한 횟수이다.
    n=target
    #더 이상 나눌 수 없을 때 반복문 종료
    if n<k:
        break
    #k로 나누기
    n= n//k
    result += 1

#마지막으로 남은 수에 대하여 1씩 빼기
# result += (n-1)
print(result)