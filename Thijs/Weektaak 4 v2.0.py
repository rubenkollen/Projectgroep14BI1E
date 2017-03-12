# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 17:30:58 2017
Files -> codon graph
Currently doesn't support files that don't start with 'ATG' or 'M'
Version 2.0

Program now "knows" what kind of file it is, 
having to choose manually and forgotting how to type it is now over.
Wrong files get an error message after which you can try again. 

@author: thijs
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import re
from collections import Counter
import operator
import pandas as pd

try:

    
    def main():

        bestand = []   
        bestand = open(input('Bestand met extensie: '))
        bestand = bestand.read().lower()                        # Opent het bestand en read het bestand volledi
        
        sequentie,Aminoacid = seq(bestand)                        # Roept de functie seq aan met bestand
        
        if Aminoacid:
            apart = split(sequentie,1)
        else:
            apart = split(sequentie,3)
            
        freq(apart)
        sd(apart)
        substitutie,lowest,highest = subb(apart,Aminoacid)
        spec_per(substitutie)
        legenda = table(highest,lowest)
        bar_aa(substitutie, legenda)
        

    
    def seq(file):
        bestand = file
        enter = re.search("\n", bestand) 
        origin = re.search('origin', bestand)
        
        if enter != None and origin == None:
            print('Fasta format')
            Converting = True
            n = enter.end()
        elif origin != None:
            print('Not Fasta format')
            Converting = True
            n = origin.end()
        elif origin == None and enter == None:
            Converting = False
            print('Foutief bestand, probeer opnieuw')
            main()
        else:
            Converting = False
            print('Foutief bestand, probeer opnieuw')
            main()
            

        if Converting:
            
            rna = bestand[n::]                           
            step = rna.replace(' ','').replace('\n','').replace('//','').replace('\r','')      
            seq = re.sub(r'\d+', '', step)
        
            acid = re.search('[BUJOXZ]', seq) 
            
            a = seq.count('a')
            t = seq.count('t')
            g = seq.count('g')
            c = seq.count('c')
            tot = len(seq)
            nucl = a+t+g+c
            if tot - nucl == 0:
                Genome = True
            else:
                Genome = False  
                
            if acid == None and Genome == False:
                print('Aminoacid sequence\n')
                seq = seq.upper()
                Aminoacid = True
                return seq,Aminoacid
            else:
                print('Genome sequence\n')
                Aminoacid = False
                return seq,Aminoacid


    def split(string, num):                                                            #Dit spilt de sequentie in codons van 3
        return [ string[start:start+num] for start in range(0, len(string), num) ]  
    
# --------------------------------------- Vanaf hier is afvink 2 -----------------------------
    
    def freq(lijst):
        counts = Counter(lijst)
        return counts
    
    def sd(a):
        counts = Counter(a).values()
        lijst = []
        for i in counts:
            lijst.append(i)
        #print(lijst)
        sd = np.std(lijst)
        return sd
    
        
# ----------------------------------------- Vanaf hier is afvink 3 -----------------------------------------------    
    
    def subb(apart,Aminoacid):
      
        if Aminoacid == False:
            code = {'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
            'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
            'tta': 'L', 'tca': 'S', 'taa': '*', 'tga': '*',
            'ttg': 'L', 'tcg': 'S', 'tag': '*', 'tgg': 'W',
            'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
            'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
            'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
            'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
            'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
            'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
            'ata': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
            'atg': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R', 
            'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
            'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
            'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
            'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G'
            }
            
            aminozuren = ''.join(str(code.get(apart, apart)) for apart in apart)
            #print(final_string)
        
            lijst_aa = [ aminozuren[start:start+1] for start in range(0, len(aminozuren), 1) ]
            #print(lijst_aa)
            
            counts = Counter(lijst_aa)
            #print('counts',counts)
            
        else:
            lijst_aa = apart
            counts = Counter(lijst_aa)
            #print('counts',counts)
        
        
        
        dictfoob = ['A','I','L','F','V','P']

        sum1 = 0
        sum2 = 0

        for key in lijst_aa:
            sum1 += 1

        print(sum1, 'is het aantal aminozuren in het bestand')

        for key in lijst_aa:
            if key in dictfoob:
                sum2 += 1

        print(sum2, 'is het aantal hydrofobe aminozuren in het bestand\n')
        print((float(sum2) / float(sum1) * 100) , '%', ' Hydrofoob')
        print(float(100) - (float(sum2) / float(sum1) * 100) , '%' , ' Hydrofiel\n')

        counts = Counter(lijst_aa)
        
        count_sort = sorted(counts.items(), key=operator.itemgetter(1))
        #print('sorted',count_sort)
        
        highest = []
        lowest = []
        count = 0
        for i in count_sort:
            if count < 4 and count > 0:
                lowest.append(i)
            elif count >= len(counts)-3:
                highest.append(i)
                
            count += 1

        return counts,lowest,highest
    
    
    def spec_per(subs):
        total = sum(subs.values())
        for key,value in subs.items():
            if key == 'C':
                Cys = (value/total)*100
            elif key == 'W':
                Trp = (value/total)*100
        print('Cys:',Cys,'%','\nTrp:',Trp,'%\n')
        
        
    def table(high,low):
        nmb1 = []
        nmb2 = []
        nmb3 = []
        
        #print(high)
        #print(low)
        for x in range(len(high)):
            if x == 0:
                nmb3.append(high[x])
            elif x == 1:
                nmb2.append(high[x])
            elif x == 2:
                nmb1.append(high[x])
        
        for x in range(len(low)):
            if x == 0:
                nmb1.append(low[x])
            elif x == 1:
                nmb2.append(low[x])
            elif x == 2:
                nmb3.append(low[x])

        
        
        
        raw_data = {'Hoogste/Laagste':['Hoogste','Laagste'],
                    '#1':nmb1,
                    '#2':nmb2,
                    '#3':nmb3}
        
        legend = pd.DataFrame(raw_data, columns = ['Hoogste/Laagste', '#1', '#2', '#3'])
        return legend        
        
            
            
            
# ------------------------------ Bar plots -----------------------------------------           
    
    
    
    def bar(a,sd): # Afvink 2
        labels, values = zip(*Counter(a).items())
        
        indexes = np.arange(len(labels))
        width = 0.7
        
        plt.figure(figsize=(22,7))
        plt.bar(indexes, values, width, color = 'lightgray')
        plt.xticks(indexes, labels, rotation = 'vertical')
        plt.ylabel('Frequentie')
        plt.title('Frequentie codons in de sequentie')
        
        plt.plot(values, color='darkblue')
        
        z = len(labels)
        y = np.linspace(sd,sd)
        x = np.linspace(-1,z)
        plt.plot(x, y, '--', color='red', linewidth=2)
        
        
        plt.gcf()
        
        
    def bar_aa(sub_aa, legenda): # Afvink 3
        labels, values = zip(*sub_aa.items())
        
        indexes = np.arange(len(labels))
        width = 0.7
        
        plt.figure(figsize=(22,7))
        plt.bar(indexes, values, width, color = 'lightgray')
        plt.xticks(indexes, labels)
        plt.ylabel('Frequentie')
        plt.title('Frequentie aminozuren in de sequentie')
        
        plt.gcf()
        
        print(legenda)
        
        
        
        """
        
        tb = plt.subplot(111, frame_on=False)
        tb.xaxis.set_visible(False)
        tb.yaxis.set_visible(False)
       
        table(tb, legenda)
        """
        
        
        
        
        
        
        
        
        
        
        
        
        
        

    main()

except ValueError:
    print("ValueError")
except FileNotFoundError:
    print("Bestand niet gevonden, probeer opnieuw")
    main()




'''
Pseudocode:
    
Importeer sequentie via input buiten functie, in variabele string
Importeer het getal voor splitten via input buiten functie, in variabele number

[string [van positie start tot start + number] met een begrenste loop in een range van 0 tot de lengte van de string, met het number]   
    
    
def split(string, num):                                                            #Dit spilt de sequentie in codons van 3
    return [ string[start:start+num] for start in range(0, len(string), num) ]  
    














'''

'''

count = 0
        for key,value in counts.items():
            if count < 3:
                placing.append(key)
            elif count >= len(counts)-4:
                placing.append(key)
                
            count += 1
        print(placing)

'''








'''

labels, values = zip(*Counter(['A','B','A','C','A','A']).items())

indexes = np.arange(len(labels))
width = 1

plt.bar(indexes, values, width)
plt.xticks(indexes + width * 0.5, labels)
plt.show()


-------------


import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

mu, sigma = 100, 15
x = mu + sigma*np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='green', alpha=0.75)

# add a 'best fit' line
y = mlab.normpdf( bins, mu, sigma)
l = plt.plot(bins, y, 'r--', linewidth=1)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)

plt.show()
 
-----------------

 print(float(sum(d['value'] for d in counts)) / len(counts))





'''
