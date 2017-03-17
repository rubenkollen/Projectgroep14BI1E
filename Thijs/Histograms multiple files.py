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
    histo(data)


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

    return data
    
    
def histo(data):
    

    #print(data)

    amount = int(len(data)/10)

    standerd = np.std(data)
    print('\nStandaarddeviatie: ',standerd)

    gemiddelde = np.mean(data)
    print('Gemiddelde %-overeenkomst: ',gemiddelde)
    
    titel = 'Histogram'
    plt.figure(figsize=(12,7))
    n, bins, patches = plt.hist(data, amount, normed=1, rwidth=0.95,color='lightblue')
    
    y = mlab.normpdf(bins, gemiddelde, standerd)
    plt.plot(bins, y, 'r--')
    
    plt.title(titel)
    plt.xlabel('% overeenkomstig')
    plt.ylabel("Frequency")
    
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