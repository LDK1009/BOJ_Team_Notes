#논리 연산자
a=True
b=False

if (a or b):
    print("or")
if (a and b):
    print("and")
if not (a and b):
    print("notw and")

#기타 연산자
a=[1,2,3,4,5,6,7]
if 8 in a:
    print("8이 있다")
    pass # 아무것도 처리하고 싶지 않을 때 pass 사용
if 8 not in a:
    print("8이 없다")
    
#조건문 표현식을 이용한 변수 대입
score=85
result = "success" if score >= 80 else "fail" #score가 80점 이상이면 success를 아니라면 fail을 대입

# 변수의 범위 표현
a=20
if (0<a<30):
    print("범위 표현 성공")
    
# continue 키워드
sum=0
for i in range(1,10):
    if i%2 ==0: #짝수 일 떄 continue 다음 코드들은 건너뛴다.
        continue
    sum += i
print(sum) 