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
    code(bestand1)




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

    original = ''.join(seq)
    #print('Originele sequentie: ',original, '\n')

    for i in range(0,100):
        random.shuffle(seq)
        string = ''.join(seq)
        variants.append(string)

    #print(variants)



    #print(open('fastas.txt').read())
    x = 1
    fasta = open('fastas.txt', 'w')
    fasta.write('>HIV1originalsequence\n')
    fasta.write(original)
    fasta.write('\n\n')


    for sequence in variants:

        writing = '>HIV1randomsequences' + str(x)
        fasta.write(writing)
        fasta.write('\n')
        fasta.write(sequence)
        fasta.write('\n\n')
        x += 1

    fasta.close()
    print(open('fastas.txt').read())


main()
