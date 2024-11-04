import random

numbers = [random.randint(0,101),random.randint(0,101),random.randint(0,101),random.randint(0,101),random.randint(0,101),]


print(numbers)


def bubble_sort(n): 


    for j in range(0, len(n)-1):
         for i in range(0, len(n)-1):
             if n[i] > n[i+1]:
                 n[i], n[i+1] = n[i+1], n[i]


   
    print(n)

bubble_sort(numbers)