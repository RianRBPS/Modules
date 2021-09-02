import random

print(random.randint(0, 100))

random.seed(101) # Fixa um valor único aleatório
print(random.randint(0, 100)) # 74

random.seed(42)
print(random.randint(0, 100)) # 81
print(random.randint(0, 100)) # 14
print(random.randint(0, 100)) # 3
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))

######################################################################

mylist = list(range(0, 20))
print(mylist)
print(random.choice(mylist))

######################################################################

       # Sample with replacement

print(random.choices(population = mylist, k = 10))

       # Sample without replacement (A number cannot show twice)

print(random.sample(population = mylist, k = 10))

#######################################################################

random.shuffle(mylist) # Embaralha
print(mylist)

print(random.uniform(a=0, b=100))

########################################################################

print(random.gauss(mu= 0,sigma=1))

        # NUMPY