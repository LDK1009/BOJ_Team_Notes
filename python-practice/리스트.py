a=[1,2,3,4,5,6,7]
print(a)
print(a[3])

#크기가 n이고 모든 값이 0인 1차원 리스트 초기화
n=10
a=[3]*n
print(a)

#음수 인덱싱을 이용한 역순 원소 출력
b=[1,2,3,4,5,6,7]
print(b[-1]) #마지막 원소 '7'
print(b[-3]) #뒤에서 세번째 원소 '5'

#슬라이싱을 이용한 범위 원소 출력
c=[1,2,3,4,5,6,7]
print(c[1:4]) #index1 부터 index3 원소까지 출력한다. 즉, 2,3,4 출력. 따라서 범위 설정 시 끝 인덱스는 원하는 원소의 인덱스 보다 1 크게 설정해야한다.
print(c[:4]) #첫번째 원소부터 index3까지 원소까지 출력한다 

#리스트 컴프리헨션을 이용하지 않은 리스트 초기화
common = []
for i in range(10):
    common.append(i) #i를 1씩 증가시키며 리스트에 append
print("common 배열은 >>", common)

#리스트 컴프리헨션을 이용한 리스트 초기화
d= [i for i in range(10)] #0부터 9까지의 수를 포함하는 리스트 초기화
e = [i for i in range(10) if i%2==1] #0부터 9까지의 수 중에서 홀수만을 포함하는 리스트 초기화
f=[i*i for i in range(10)]#0부터 9까지의 수를 제곱한 값을 포함한 리스트 초기화
g=[i*i for i in range(10) if (i*i)%2==0]#리스트 f에서 결과값이 짝수인 것만 포함
print(d)
print(e)
print(f)
print(g)

#리스트 컴프리헨션을 이용한 2차원 리스트 초기화(중요!)
n=4 #행
m=3 #열
array2 = [[0] * m for _ in range(n)] #반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 떄 언더바(_)를 사용한다.
# '[0] * m'은 모든 값이 0이고 크기가 m인 1차원 리스트를 생성한다. 즉, m개의 열을 생성한다.
# 그리고 해당 작업을 n번 반복한다. 크기가 m인 1차원 리스트 생성이 n번 반복되므로 n(행)*m(열) 2차원 리스트가 생성된다.
print(array2)

#잘못된 2차원 리스트 초기화
n=4
m=3
array2 = [[0] * m] * n 
print(array2) #생성에는 문제가 없지만

array2[1][2]=5
print(array2) #특정 위치의 값을 변경하면 문제 발생(2차원 리스트 내부에 있는 모든 1차원 리스트를 같은 객체로 인식하여 모든 1차원 리스트의 index2 요소를 변경한다.)