a=0.3
b=0.6
print("a+b =",a+b)

roundNum=round(a+b, 1)
print("반올림 =", roundNum) #소수점 두번째 자리까지만 표현한다.
 
print("<일반 덧셈>")
if(a+b==0.9): #소수점의 합은 
    print('true')
else:
    print('false')

print("<반올림 후>")
if(roundNum==0.9): #소수점의 합은 
    print('true')
else:
    print('false')
