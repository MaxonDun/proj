import math
# print('My {1} name is {0}. I\'m {1}'.format(name,age))
#print('My name is {x}. I\'m {y}'.format(x=name, y=age))
#f - strings
# print(f'My name is {name}. I\'m {age}')
#print(f'My name is {name}. I\'m {age+5}')
#print('5 + 2 = {}'.format(5 + 2))
#print(f'5 + 2 = {"5" + "2"} ')

# words = [ 'мадам', 'топот', 'test', 'madam','word',]
# polind = []
# j=1
# s=''
# for i in words:
#     a = i
#     while j <= len(a)//2+1:
#         if a[j-1]==a[-j]:
#             j+=1
#             if j-1==len(a)//2+1:
#                 polind.append(a)
#         else:
#             break
#     j=1
# print(polind)

# for i in words:
#     if i = i[::-1]:
#         polind.append(i)

# polind = [word for word in words if word == word[::-1]]

# words = [ 'Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']
# polind = []
# p=1
# strok=''
# for i in words:
#     a = i.split(' ')
#     for b in a:
#         strok = strok +b.lower()
#     while p <= len(strok) // 2 + 1:
#         if strok[p-1]==strok[-p]:
#             # print(f'{strok[p - 1]} == {strok[-p]}')
#             p+=1
#             if p-1==len(strok)//2+1:
#                 polind.append(i)
#         else:
#             break
#     p=1
#     strok=''
# print(polind)
# price = []
# big = [
#     {"name": "bread", "price": 100},
#     {"name": "wine", "price": 138},
#     {"name": "meat", "price": 15},
#     {"name": "water", "price": 1}]
# i=0
# print(len(big))
# while i < len(big):
#     if big[i]['price']>price:
#         price = big[i]['price']
#     i+=1
# print(price)

#
# data = []
# with open("input-201.txt") as f:
#     for line in f:
#         data.append([int(x) for x in line.split()])
# i=0
# j=0
# check=0
# while i < len(data):
#     j = data[i]
#     if data.count(j) == 1:
#         print(data[i][0])
#     i+=1

# f = open('input.txt')
# n = int(f.readline())

# b = input()
# a = list(map(int, input().split()))
# i=0
# j=len(a)-1
# while i < len(a):
#     while j>i:
#         if a[j] + a[i]==b:
#             print(1)
#             break
#         j-=1
#     i+=1
#     j=len(a)-1

# a ={}
# a['age']= 25
# a['job']= 'develop/manage'
# print(a)

values={4, 8, 10, 11, 12, 17}
one = 9
i=0
ind=0
if one not in values:
    values.add(one)
sorted(values)
values1= list(values)
print(values1)
i=values1.index(one)
if i!=0 and i!=len(values1)-1:
    if abs(values1[i-1]-one)>abs(values1[i+1]-one):
        print(values1[i+1])
    elif abs(values1[i-1]-one)<abs(values1[i+1]-one):
        print(values1[i-1])
elif i==0:
    print(values1[1])
else:
    print(values1[len(values1)-1])

# sorted(values)
# raznica=1000
# while i<len(values):
#     if abs(values[i]-one)<raznica:
#         raznica=abs(values[i]-one)
#         # if
#         ind = i
#     i+=1
# print(values[ind])