# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 13:51:20 2017

@author: thijs
"""
import re


p53 = open('p63.gb').read()

oori = re.search('ORIGIN',p53)
oori = oori.end()
string = p53[oori:]

step = string.replace(' ','').replace('\n','').replace('//','').replace('\r','')         # Verwijder alles behalve de getallen
seq = re.sub(r'\d+', '', step)
seq = seq.upper()

print(p53)



file = open('p63 seq.txt','w')
file.write(seq)
file.close()
