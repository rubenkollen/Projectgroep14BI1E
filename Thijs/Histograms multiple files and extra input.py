# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 10:33:37 2017

@author: thijs
"""
import re
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
from scipy import stats
from collections import Counter




def main(): 

    hoeveelheid = int(input('Hoeveel bestanden? '))

    for u in range(hoeveelheid):
        if u == 0:
            lijst = []
        keuze = input('Bestand naam: ')
        data = file(keuze,u,lijst)
    
        
    extra = int(input('Hoeveel andere indentity %: '))
    
    others = []
    
    for t in range(extra):
        more = input('%: ')
        others.append(more)
    
    #others = [32,34,30,45,34,34]
    
    histo(data,others)


def file(keuze,r,data):

    file = open(keuze+'.pim').read()
    one = re.search('1:',file)
    two = re.search('2:',file)
    first = one.start()
    second = two.start()
    
    file = file[first:second]
    lijst = file.split()   
    
    matrix = lijst[3::]    

    
    for x in matrix:
        s = float(x)
        data.append(s)    
        
    print(file)
    return data
    
    
def histo(data,others):
    
    for x in others:
        data.append(float(x))
    
    print('-'*60)
    
    mx = np.max(data)
    print('\n\nMaximale waarde: ',mx)
    
    
    amount = int(len(data)/10)

    standerd = np.std(data)
    print('Standaarddeviatie: ',standerd)

    gemiddelde = np.mean(data)
    print('Gemiddelde %-overeenkomst: ',gemiddelde)
    
    plt.figure(figsize=(12,7))
    n, bins, patches = plt.hist(data, amount, normed=1, rwidth=0.95,color='lime',alpha=0.5)
    
    y = mlab.normpdf(bins, gemiddelde, standerd)
    plt.plot(bins, y, 'r--', label='Normaal verdeling')
    
    plt.xlabel('% overeenkomstig')
    plt.ylabel("Probability")
    plt.legend()
    
    plt.gcf()
            
        
    plt.hist    
        


    
main()



"""
    amount = int(len(data)/4)
    print(amount)

n, bins, patches = plt.hist(data, amount, normed=1, rwidth=0.95,color='lightblue')
    
    y = mlab.normpdf(bins, gemiddelde, standerd)
    plt.plot(bins, y, 'r--'
"""