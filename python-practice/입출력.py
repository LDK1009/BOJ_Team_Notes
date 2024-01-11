#데이터의 개수 입력
n= int(input()) #데이터 개수 입력 받기

data=list(map(int, input().split())) #입력 받은 문자열을 공백 문자로 구분해 정수형으로 바꾼 후 리스트로 묶는다.

data.sort(reverse=True)
print(data)

#f-string
answer=7
print(f"정답은 {answer}입니다.")