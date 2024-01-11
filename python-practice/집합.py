a=set([1,2,3,4,5])
b=set([3,4,5,6,7])

#합집합
print(a|b)
#교집합
print(a&b)
#차집합
print(a-b)

#새로운 원소 한개 추가
a.add(4)
print(a)

#새로운 원소 여러개 추가
a.update([5,6])
print(a)

#특정한 값을 갖는 원소 삭제
a.remove(3)
print(a)