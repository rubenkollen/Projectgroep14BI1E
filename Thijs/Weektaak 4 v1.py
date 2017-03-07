# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 17:30:58 2017
Opdelen van sequentie in codons en aminozuren
@author: thijs

Version 1.1.1
Debug and one useless function removed, code is better looking
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import re
from collections import Counter

try:
    
    def main():

        bestand = []   
        bestand = open("hiv1 gag.txt")
        bestand = bestand.read().lower()                        # Opent het bestand en read het bestand volledig

        sequentie = seq(bestand)                        # Roept de functie seq aan met bestand
        apart = split(sequentie,3)                      # Roept split aan in "apart" en split de sequentie in delen van 3
        standerd = sd(apart)
        substitutie = subb(apart)
        bar(apart,standerd)
        print('\n','SD: ',standerd,'(De rode stippellijn)')
        bar_aa(substitutie)

    
    def seq(file):
        bestand = file
        useful = re.search("\n", bestand)           # Zoekt de positie van "ORIGIN" in het bestand
        n = useful.end()                                # Het einde van "ORIGIN"
        fasta = bestand[n::]                            # fasta is nu het bestand na "ORIGIN"
        step = fasta.replace(' ','').replace('\n','').replace('//','').replace('\r','')         # Verwijder alles behalve de getallen
        seq = re.sub(r'\d+', '', step)                  # Verwijder de getallen
        return seq

          
    def split(string, num):                                                            #Dit spilt de sequentie in codons van 3
        return [ string[start:start+num] for start in range(0, len(string), num) ]  
    
# --------------------------------------- Vanaf hier is afvink 2 -----------------------------
    
    def sd(a):
        counts = Counter(a).values()
        lijst = []
        for i in counts:
            lijst.append(i)                             # Van de values in de dictionary wordt een lijst gemaakt en wordt de SD berekend
        sd = np.std(lijst)
        return sd
        
# ----------------------------------------- Vanaf hier is afvink 3 -----------------------------------------------    
    
    def subb(apart):
      
        codon_counts = Counter(apart)
        print(codon_counts, '\n')
        
        
        
        
        
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
        'gtg': 'Val', 'gcg': 'Ala', 'gag': 'Glu', 'ggg': 'Gly'}                 # Dictionary met aminozuur en codon
        
        aminozuren = ''.join(str(code.get(apart, apart)) for apart in apart)    # Vergelijkt de lijst van split() en maakt van het codon het aminozuur
        print(aminozuren)
                            
        lijst_aa = [ aminozuren[start:start+3] for start in range(0, len(aminozuren), 3) ]  # Zelfde principe als split() om aminozuren in een lijst te zetten
        
        counts = Counter(lijst_aa)                                              # Bepaalt frequentie van aminozuren, in dictionary
        return counts
    
                
# ------------------------------ Bar plots -----------------------------------------           
    
    def bar(a,sd): # Collection of plots for codons
        labels, values = zip(*Counter(a).items())
        
        indexes = np.arange(len(labels))
        width = 0.7
        
        plt.figure(figsize=(22,7))
        plt.bar(indexes, values, width, color = 'lightblue')
        plt.xticks(indexes, labels, rotation = 'vertical')
        plt.ylabel('Frequentie')
        plt.title('Frequentie codons in de sequentie')
        
        plt.plot(values, color='darkblue')
        
        z = len(labels)
        y = np.linspace(sd,sd)
        x = np.linspace(-1,z)
        plt.plot(x, y, '--', color='red', linewidth=2)
        
        plt.gcf()
        
        
    def bar_aa(sub_aa): # Aminoacid bar plot
        labels, values = zip(*sub_aa.items())
        
        indexes = np.arange(len(labels))
        width = 0.7
        
        plt.figure(figsize=(22,7))
        plt.bar(indexes, values, width, color = 'lightblue')
        plt.xticks(indexes, labels)
        plt.ylabel('Frequentie')
        plt.title('Frequentie aminozuren in de sequentie')
        
        plt.gcf()
        

    main()

except ValueError:
    print("ValueError")
except FileNotFoundError:
    print("Bestand niet gevonden")
except:
    print("Unknown Error")




'''
Pseudocode:
    
Importeer sequentie via input buiten functie, in variabele string
Importeer het getal voor splitten via input buiten functie, in variabele number

[string [van positie start tot start + number] met een begrenste loop in een range van 0 tot de lengte van de string, met het number]   
    
    
def split(string, num):                                                            #Dit spilt de sequentie in codons van 3
    return [ string[start:start+num] for start in range(0, len(string), num) ]  
    














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
