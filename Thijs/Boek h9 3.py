# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:06:31 2017

@author: thijs
"""

'''

3.
File encryption and Decryption

Write  a  program  that  uses  a  dictionary  to  assign  “codes”  to  each  letter  of  the  alphabet. 
For example:
codes = { 'A' : '%', 'a' : '9', 'B' : '@', 'b' : '#', etc . . .}
Using  this  example,  the  letter A would  be  assigned  the  symbol %,  the  letter a would  be assigned the number 9, 
the letter B would be assigned the symbol @, and so forth.

The program should open a specified text file, read its contents, and then use the dictionary 
to write an encrypted version of the file’s contents to a second file. Each character in the 
second file should contain the code for the corresponding character in the first file.
Write  a  second  program  that  opens  an  encrypted  file  and  displays  its  decrypted  contents 
on the screen.

'''


def main():
    bestand1 = bstnd1()
    #print(bestand1)
    codes = code(bestand1)
    
    
    
    
def bstnd1():
    bestand = open('bestand1.txt').read()
    return bestand



def code(bestand1):
    codes = {'A': '%', 'a': '9', 'B': '@', 'b': '#', 'C': '!', 'c': '*', 'D': '&', 'd': '$', 
             'E': '€', 'e': '^', 'F': '(', 'f': ')', 'G': '1', 'g': '2', 'H': '3', 'h': '4',
             'I': '5', 'i': '6', 'J': '7', 'j': '8', 'K': 'A', 'k': 'a', 'L': 'B', 'l': 'b',
             'M': 'C', 'm': 'c', 'N': 'D', 'O': 'D', 'o': 'd', 'P': 'E', 'p': 'e', 'Q': 'F',
             'q': 'f', 'R': 'G', 'r': 'g', 'S': 'H', 's': 'h', 'T': 'i', 't': 'I', 'U': 'm',
             'u': 'q', 'V': 'z', 'v': 'x', 'W': 'Z', 'w': 'X', 'X': 'R', 'x': 'r', 'Y': 'T',
             'y': 't', 'Z': 'm', 'z': 'M'}
    
    encoded = ''.join(str(codes.get(bestand1, bestand1)) for bestand1 in bestand1)
    #print(encoded)
    
    file2 = open('bestand2.txt','w').write(encoded)
    
    test = open('bestand2.txt').read()
    print(test)
    
    
    noncode = {"Letterlijk de dict omdraaien"}
    
    decoded = ''.join(str(noncodes.get(test, test)) for test in test)
    
    print(decoded)
    
    
    
    
main()


















