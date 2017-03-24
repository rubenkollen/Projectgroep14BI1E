# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 14:22:11 2017

@author: thijs
"""
import time

def main():
    file = open('p53 seq.txt').read().lower()
    print(file,'\n')
    amount = 0
    file = [ file[start:start+250] for start in range(0, len(file), 250) ]
    trues = []
    
    
    for x in file:
        bestand = str(x)
        if recur(bestand,amount):        
            trues.append(1)
        else:
            trues.append(0)
    
    
    if sum(trues) == len(file):
        print('Dit is een nucleotide sequentie')
    else:
        print('Dit is geen nucleotide sequentie')
    
    
def recur(bestand,amount):
    
    n = amount
    if n == len(bestand):
        return True
    #time.sleep(1)
    #print(bestand[n],len(bestand))
        
    if bestand[n] in ['a','t','c','g']:
        return recur(bestand,amount+1)
    else:
        print('Dit is geen nucleotide sequentie')
        return False
       
    
main()