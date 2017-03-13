# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:06:31 2017

@author: thijs

Title: Weektaak 5
Version: 1.0

Leest Oppervlakte eiwit HIV1 in en shuffled de sequentie

"""

import random
import re

def main():
    bestand1 = bstnd1()
    #print(bestand1)
    codes = code(bestand1)
    
    
    
    
def bstnd1():
    bestand = open('hiv1opp.fasta').read()
    return bestand



def code(bestand):

    seq = []
    variants = []
    enter = re.search('\n',bestand)
    n = enter.end()
    file = bestand[n::]
    file = re.sub('\n', '', file)
    
    for x in file:
        seq.append(x)
        
    print(seq)

    for i in range(0,100):
        random.shuffle(seq)
        string = ''.join(seq)
        variants.append(string)
        
    print(variants)
        
    
    
main()


















