#!/usr/bin/env python
# coding: utf-8

# In[ ]:


TAX CALCULATOR


# In[ ]:


n = int(input('Enter a cost : $'))
m = int(input('Enter a city or state tax: '))

print(f'Tax is equal to {(m/100)*n}')
print(f'Which brings the total cost to {n +((m/100)*n)}')


# In[ ]:


RETURN A VALUE TO THE NTH DIGIT


# In[ ]:


st = '2465326453264832643287'
n = int(input('Enter a number : '))
y = list(map(int, st))
print(y)
print(y[0:n:1]
def join_int(lst):
    d = str(i) for I in lst
    result = int(''.join(d))
    return result
print(join_int(y[0:n:1]))


# In[ ]:





# In[ ]:


FIND PI TO THE NTH DIGIT


# In[ ]:


import math 

def find_pi(nth):
    placepi = round(math.pi,nth);
    pi = str(placepi)
    lst = list(pi)

    return placepi;
roundTo = input('Enter the number of digits you want after the decimal for Pi: ')

try:
    roundint = int(roundTo);
    print(find_pi(roundint));
except:
    print("You did not enter an integer");     


# In[ ]:


COIN FLIP SIMULATION


# In[ ]:


import random

coin_flip = ('heads', 'tails')
y = random.choice(coin_flip)
print(y)
heads = 0
tails = 0
while heads < 10 and tails < 10:
    for y in coin_flip:
        if y == 'heads':
            
            heads += 1
        elif y == 'tails':
            tails += 1

print (heads, tails)


# In[ ]:





# In[ ]:


FAST EXPONENTATION


# In[ ]:


a = int(input('Enter a value for a: '))
b = int(input('Enter a value for b : '))

print(a**b)


# In[ ]:





# In[ ]:


STRING REVERSE


# In[ ]:


n = str(input('Enter a word: '))
reverse = n[::-1]
print(reverse)


# In[ ]:





# In[ ]:


REPLACE PRACTICE


# In[ ]:


x= 'devil'
s= x.replace('d', 'c')
y = s.replace('e', 'i')
n = 'ity'
print(y + n)


# In[ ]:


PRIMES IN 100


# In[ ]:


x = list(range(100))
for values in list(x):
    if values % 2 == 0 or values % 3 == 0 or values % 5 ==0:
        x.remove(values)
    elif values % 7 ==0 or values % 11 == 0:
        x.remove(values)
x.insert(1, 2)
x.insert(2, 3)
x.insert(3, 5)
x.insert(4, 7)
x.insert(5, 11)
print(x)
    


# In[ ]:


PIG LATIN


# In[ ]:


n = str(input('Enter a word: '))
x = list(map(str,n))
lst = [str(x[0]), 'ay']
x.extend(lst)
x.remove(x[0])

def join_str(string):
    d=[i for i in string]
    result = ''.join(d)
    return result
print(join_str(x))


# In[ ]:


VOWEL COUNT


# In[ ]:


n = str(input('Enter a word: '))
vowel_count=0
for x in n:
    if x == 'a' or x=='e' or x=='i' or x=='o' or x=='u':
        vowel_count=vowel_count+1
        print(vowel_count)
            


# In[ ]:





# In[ ]:


FACOTRIZATION


# In[ ]:


n = int(input('Please enter a number: '))
a =[1, 2, 3, 5, 7, 9, 11, n]
for x in a:
    if n % x == 0:
        print(f'A prime factor of {n} is {x}')

        


# In[ ]:





# In[ ]:


CHANGE RETURN PROGRAM


# In[ ]:


n = int(input('Please enter the amount given: '))
m = int(input('Please enter cost of item: '))

a = [0.25, 0.10, 0.05, 0.01]

y = n - m 

for x in a :
    if y % x == 0 :
        b =int(y/x)
        print(f'Your change is ${y}\nYou need {b} {x} coins')


# In[ ]:





# In[ ]:


BASIC OPERATIONS


# In[ ]:


n = int(input('Enter your first number: '))
m = int(input('Enter your second number: '))
o  = str(input('Please choose a function\nmultiplication(m)\ndivision(d)\naddition(a)\nsubtraction(s)'))

def multiplication(x):
    if o == 'm':
        print(f'the answer is {m*n} by multiplication')
multiplication(x)

def division(y):
    if o == 'd':
        print(f'the answer is {n/m}]  by division')
division(y)

def addition(z):
    if o == 'a':
        print(f'the answer is {n+m}by addition ')
addition(x)

def subtraction(y):
    if o == 's':
        print(f'the answer is {n-m} by subtraction')
subtraction(y)
    


# In[ ]:


STRING PALINDROME CHECKER


# In[ ]:


n = str(input('Enter a word without spaces: '))
if n[::-1] == n:
    print(f'True, the word "{n}", is a palindrome')
else:
    print(F'Oops! looks like your word "{n}" isnt a palindrome\nWhen read backwards your word is "{n[::-1]}"')


# In[ ]:





# In[ ]:


CODEACADEMY PRACTICE


# In[ ]:


grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print(grade)

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / len(grades_input)
  return average

def grades_variance(grades):
    variance = 0
    for number in grades:
        variance += (grades_average(grades) - number) ** 2
    return variance / len(grades)

variance = grades_variance(grades)

for grade in grades:
    print(grade)
print('The sum of the grades is {}' .format(grades_sum(grades)))
print('The average of the grades is {}' .format(grades_average(grades)))
print('The grade variance is {}' .format(grades_variance(grades)))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




