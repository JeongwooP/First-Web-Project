a = 3
b = a
a = a + 1

num = a*b
num2 = 99

name = 'bob'
is_number= True

print(a + b)
print(name)

c = str(b)

print(name + c)

a_list = [1,2]
a_list.append(4)
a_list.append([7,8])

a_dict = {}
a_dict = {'name' : 'bob', 'age' : 21}
a_dict['height'] = 178      #딕셔너리에 추가함
print(a_dict)

def f(x):
    return 2*x + 3

result = f(5)
print(result)

def is_adult(age):
    if age > 19:
        print('성인입니다.')
    else:
        print('청소년이에요')

is_adult(30)

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

count = 0
for fruit in fruits:
    if fruit == '사과':
        count += 1

print(count)

people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

def get_age(myname):
    for person in people:
        if person['name'] == myname:
            return person['age']
    return '해당하는 이름이 없습니다.'

print(get_age('bob'))