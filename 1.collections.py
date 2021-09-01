from collections import Counter

mylist = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]

print(Counter(mylist)) # Conta a quantidade de valores iguais

mylist2 = ['a', 'a', 10, 10, 10]

print(Counter(mylist2))

###################################################################

print(Counter('aaaaaaaaaaaasasfksfasjfsfsk'))

sentence = 'How many times does each word show up in this sentence with a word'
print(Counter(sentence.lower().split()))

###################################################################

letters = 'aaabbbccccccccdddddddddddddd'
c = Counter(letters)
n = 2 # Quantidade de mais comuns
print(c.most_common(n)) # Retorna os mais comuns dentro de uma tupla

print(list(c))

###################################################################

from collections import defaultdict

d = {'a': 10}
print(d['a'])
# print(d['WRONG']) Key Error

d = defaultdict(lambda: 0) # Valor default para Keys sem valor
d['correct'] = 100
d['correct']
print(d['WRONG KEY!'])

##################################################################

mytuple = (10, 20, 30)
print(mytuple[0]) # Index position

from collections import namedtuple

Dog = namedtuple('Dog',['age','breed','name']) # Attributes position
sammy = Dog(age=5,breed='Husky',name='Sam')
print(type(sammy))
print(sammy)
print(sammy.age)
print(sammy.breed)
print(sammy.name)

################################################################
