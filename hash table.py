import random

L = [random.randint(1,30) for i in range(100)]

hash_table = {0 : [], 1 : [], 2 : [], 3 : [], 4 : [], 5 : [], 6 : []}

for i in L:
  hash_table[i % 7].append(i)

print(hash_table)

n = (int(input('finding data : ')))

k = n % 7

if n in hash_table[k] :
  l = hash_table[k].index(n)
  print('location : {di}, {li}'.format(di = k, li = l))
else :
  print('찾는 값이 없음')

#해시 테이블 랜덤 생성

