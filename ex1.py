##
## EPITECH PROJECT, 2022
## workshop-scrapy
## File description:
## ex1
##

import scrapy

nblist = 1;
check = 0;

while nblist <= 100:
    if (nblist % 3 == 0 and nblist % 5 == 0):
        print("ThreeFive");
    elif (nblist % 5 == 0):
        print("Five");
    elif (nblist % 3 == 0):
        print("Three");
    else:
        print(nblist);
    nblist+=1;
