# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 10:33:37 2017

@author: thijs
"""
import re
import matplotlib.pyplot as plt
import numpy as np




def main(): 
    keuze = input('bestand met extentsie: ')

    matrix = file(keuze)
    histo(matrix,keuze)

def file(keuze):
    file = open(keuze).read()
    one = re.search('1:',file)
    two = re.search('2:',file)
    first = one.start()
    second = two.start()
    
    file = file[first:second]
    lijst = file.split()   
    
    matrix = lijst[3::]
    return matrix
    
    
def histo(matrix,keuze):
    new = []
    for x in matrix:
        s = float(x)
        new.append(s)
        
    print(new)
        
    #freq = np.arange(new)
    titel = 'Histogram van ' + keuze
    
    plt.hist(new)
    plt.title(titel)
    plt.xlabel('% overeenkomstig')
    plt.ylabel("Frequency")
    
    plt.gcf()
            
        
        
        
        
    
main()