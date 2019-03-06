# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 20:37:33 2019

@author: Mimi
"""

from matplotlib.pyplot import *
from numpy import *

#1 calculate & print the value of function y = 2x^2 + 2x + 2 for x=[56, 57, ... 100] (0.5p)

for i in range(56,101):
    y = 2*i**2+2*i+2;
    print(y)
    
print('-' * 50)

#2 ask the user for a number and print its factorial (1p)
print("Insert a random number: ");
silnia = 1;
a=int(input());
if a < 0:
    print("The factorial doesn't exist")
elif a==0:
    print("The factorial is: 1")
else:
    for i in range(1,a+1):
        silnia=silnia*i
    print("The factorial of your number is: ",silnia)
print('-' * 50)

#3 write a function which takes an array of numbers as an input and finds the lowest value. 
#Return the index of that element and its value (1p)
def lista(lis):
    indeks = [];
    dl_lis = int(len(lis));
    liczba=min(lis)
    for i in range(dl_lis):
        if lis[i]==liczba:
            indeks.append(i);
    return indeks, liczba
wynik = lista([10,20,-1,5,4,10])
#wynik=lista(input())
print("The index of the lowest element and its value:",wynik)

print('-' * 50)

#4 looking at lab1-input and lab1-plot files create your own python script that takes a number 
#and returns any chart of a given length. the length of a chart is the input to your script. 
#The output is a plot (it doesn't matter if it's a y=x or y=e^x+2x or y=|x| function, use your imagination)
#test your solution properly. Look how it behaves given different input values. (1p)

print ("Insert a number: ")
dlugosc=int(input());
x=linspace(0,100,dlugosc)
y=e**(-x**2)+cos(x**2)
plot(x,y,'g-');
show()