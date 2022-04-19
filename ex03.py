##
## EPITECH PROJECT, 2022
## workshop-scrapy
## File description:
## ex03
##

are_anagrams = lambda x, y: str(sorted(x.lower())) == str(sorted(y.lower()))

def anagrams(word, arglist):
    stock = [];
    if (isinstance(arglist, list) == False):
        return(False);
    for x in arglist:
        if (are_anagrams(word, x) == True):
            stock.append(x);
    return stock;    