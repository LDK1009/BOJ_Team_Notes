
data = dict()
data['사과'] = 'apple'
data['바나나'] = 'banana'
data['코코넛'] = 'coconut'

print(data)
print(data['사과'])

if '사과' in data:
    print("사과가 있슈")


key_list = data.keys() #키만 담은 리스트
value_list = data.values() #값만 담은 리스트
print(key_list) 
print(value_list)

#각 키에 따른 값을 출력
for key in key_list:
    print(data[key]) #키가 사과, 바나나, 코코넛일 값을 출력