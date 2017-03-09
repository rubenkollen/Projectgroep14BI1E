# -*- coding: utf-8 -*-
 
"""
 
Created on Sat Feb 11 17:30:58 2017
 
Opdelen van sequentie in codons
 
v 1.0
 
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
 
        bestand = open("eiwitsequence.fasta")
 
        bestand = bestand.read().lower()                        # Opent het bestand en read het bestand volledig
 
        vraag = input("wat wil je invoeren??")
 
        sequentie = seq(bestand)                        # Roept de functie seq aan met bestand
 
        #print(sequentie)
 
        apart = split(sequentie,3)                      # Roept split aan in "apart" en split de sequentie in delen van 3
 
        #print(apart)
 
        #print('-'*80)
 
        frequentie = freq(apart)
 
        #print(frequentie)
 
        standerd = sd(apart)
 
        substitutie,lowest,highest = subb(apart,vraag)
 
        spec_per(substitutie)
 
        legenda = table(highest,lowest)
 
        #bar(apart,standerd)
 
        bar_aa(substitutie, legenda)
 
        #print('\nLowest:', str(lowest),'\nHighest:', str(highest),"\nStop is not included as it's not an amino acid")
 
        #print('\n','SD: ',standerd,'(De rode stippellijn)')
 
        
 

 
    
 
    def seq(file):
 
        bestand = file
        
        print(file)
 
        useful = re.search("\n", bestand)           # Zoekt de positie van "ORIGIN" in het bestand
 
        n = useful.end()                                # Het einde van "ORIGIN"
 
        fasta = bestand[n::]                            # fasta is nu het bestand na "ORIGIN"
 
        #print(fasta)
 
        #print("-"*80)
 
        step = fasta.replace(' ','').replace('\n','').replace('//','').replace('\r','')         # Verwijder alles behalve de getallen
 
        #print(step)
 
        #print("-"*80)
 
        seq = re.sub(r'\d+', '', step)                  # Verwijder de getallen
 
        return seq
 

 
          
 
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
 
        mean = np.mean(lijst)
 
        #print(mean)
 
        sd = np.std(lijst)
 
        return sd
 
    
 
        
 
# ----------------------------------------- Vanaf hier is afvink 3 -----------------------------------------------    
 
    
 
    def subb(apart,vraag):
 
      
 
        
 
        code = {'ttt': 'Phe', 'tct': 'Ser', 'tat': 'Tyr', 'tgt': 'Cys',
 
        'ttc': 'Phe', 'tcc': 'Ser', 'tac': 'Tyr', 'tgc': 'Cys',
 
        'tta': 'Leu', 'tca': 'Ser', 'taa': '*  ', 'tga': '*  ',
 
        'ttg': 'Leu', 'tcg': 'Ser', 'tag': '*  ', 'tgg': 'Trp',
 
        'ctt': 'Leu', 'cct': 'Pro', 'cat': 'His', 'cgt': 'Arg',
 
        'ctc': 'Leu', 'ccc': 'Pro', 'cac': 'His', 'cgc': 'Arg',
 
        'cta': 'Leu', 'cca': 'Pro', 'caa': 'Gln', 'cga': 'Arg',
 
        'ctg': 'Leu', 'ccg': 'Pro', 'cag': 'Gln', 'cgg': 'Arg',
 
        'att': 'Ile', 'act': 'Thr', 'aat': 'Asn', 'agt': 'Ser',
 
        'atc': 'Ile', 'acc': 'Thr', 'aac': 'Asn', 'agc': 'Ser',
 
        'ata': 'Ile', 'aca': 'Thr', 'aaa': 'Lys', 'aga': 'Arg',
 
        'atg': 'Met', 'acg': 'Thr', 'aag': 'Lys', 'agg': 'Arg', 
 
        'gtt': 'Val', 'gct': 'Ala', 'gat': 'Asp', 'ggt': 'Gly',
 
        'gtc': 'Val', 'gcc': 'Ala', 'gac': 'Asp', 'ggc': 'Gly',
 
        'gta': 'Val', 'gca': 'Ala', 'gaa': 'Glu', 'gga': 'Gly',
 
        'gtg': 'Val', 'gcg': 'Ala', 'gag': 'Glu', 'ggg': 'Gly'}
 
        
 
        aminozuren = ''.join(str(code.get(apart, apart)) for apart in apart)
 
        #print(final_string)
 
        if vraag == "aminozuren":  
           lijst_aa = [ aminozuren[start:start+1] for start in range(0, len(aminozuren), 1) ]
        elif vraag == "genoom":
            lijst_aa = [ aminozuren[start:start+3] for start in range(0, len(aminozuren), 3) ]
        else:
            print("verkeerde invoer, probeer opnieuw")
            main()
            
        #print(lijst_aa)
 
        
 
        counts = Counter(lijst_aa)
 
        #print('counts',counts)
 
        
 
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
 
        #print('\nLowest:', lowest,'\nHighest:', highest,"\nStop is not included as it's not an amino acid")
 
        
 
        return counts,lowest,highest
 
    
 
    
 
    def spec_per(subs):
 
        total = sum(subs.values())
 
        for key,value in subs.items():
 
            if key == 'Cys':
 
                Cys = (value/total)*100
 
            elif key == 'Trp':
 
                Trp = (value/total)*100
 
        #print('Cys:',Cys,'%','\nTrp:',Trp,'%')
 
        
 
        
 
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
 

 
        print('nmb1',nmb1)
 
        
 
        
 
        
 
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
 
        plt.bar(indexes, values, width, color = 'lime')
 
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
 
        plt.bar(indexes, values, width, color = 'lime')
 
        plt.xticks(indexes, labels)
 
        plt.ylabel('Frequentie')
 
        plt.title('Frequentie aminozuren in de sequentie')
 
        
 
        plt.gcf()
 
        
 
        print(legenda)
 
        
       
 
        
 
        
 
        
 
        
 
        
 
        
 
        
 
        
 
        
 
        
 
        
 
        
 

 
    main()
 

 
#except ValueError:
 
 #   print("ValueError")
 
except FileNotFoundError:
 
    print("Bestand niet gevonden")
 

 

 

 

 
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
 