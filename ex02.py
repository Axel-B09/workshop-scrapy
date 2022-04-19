##
## EPITECH PROJECT, 2022
## workshop-scrapy
## File description:
## ex02
##

from pickle import FALSE, TRUE
import string

def atoi(str):
    resultant = 0
    isneg = False;
    if str[0] == '-':
        isneg = True;
    for i in range(len(str)):
        resultant = resultant * 10 + (ord(str[i]) - ord('0'))        #It is ASCII substraction 
    if isneg == True:
        resultant = resultant * -1;
    return resultant

def calculate(nblist):
    res = 0
    list_check = isinstance(nblist, list)
    if (list_check == False):
        return(False)
    for x in nblist:
        if (isinstance(x, str) == True):
            if (x.isdigit()):
                res += atoi(x)
    if (res == 0):
        return(False)
    else:
        return (res)
        

x = calculate(['4', '3', '-2']);
print(x);
x = calculate(453);
print(x);
x = calculate(['nothing', 3, '8', 2, '1']);
print(x);
x = calculate('54');
print(x);