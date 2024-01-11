n=1260 #거스름돈
count=0 #동전의 개수

array = [500, 100, 50, 10] #동전의 종류

for i in array:
    count += n//i #나눈 몫. 즉, 해당 동전의 개수
    print(i,'원 동전', n//i, '개를 거슬러 주었습니다.')
    n=n%i;
    print('남은 금액은',n,'원')
    
print(count)
