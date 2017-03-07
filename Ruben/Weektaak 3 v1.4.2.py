# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 17:30:58 2017
Fasta files to codon plot

>>> ONLY USE FASTA FORMAT <<<

Version 1.4.2

>>> Belangrijk: 
    Bij SIV, niet SIVmnd. Is de coderende sequentie vanaf AUG maar
    13 codons lang, dit geeft problemen van de percentage berekening. 
    Ik heb er een if/else statement in gezet die een ZeroDivisionError voorkomt,
    maar voor een goede grafiek moet je apart = split(coding, 3), omzetten
    naar apart = split(sequentie, 3)
    

New: File choice, correct labels plot, errors loop back to main() and removed useless code
@author: thijs
"""
import numpy as np
import matplotlib.pyplot as plt
import re
from collections import Counter
import pandas as pd
from pandas.tools.plotting import table

try:

    
    def main():
        choice = input("Bestand met extensie: ")
        print('')
        bestand = []   
        bestand = open(choice)
        bestand = bestand.read().lower()                        # Opent het bestand en read het bestand volledig

        sequentie = seq(bestand)                        # Roept de functie seq aan met bestand
        coding = cds(sequentie)
        apart = split(coding,3)
        print(apart)                      # Roept split aan in "apart" en split de sequentie in delen van 3
        frequentie = freq(apart)
        standerd = sd(apart)
        substitutie = subb(apart, choice)
        legend(choice)
    
    def seq(file):
        bestand = file
        useful = re.search("\n", bestand)           # Zoekt de positie van "ORIGIN" in het bestand
        n = useful.end()                                # Het einde van "ORIGIN"
        fasta = bestand[n::]                            # fasta is nu het bestand na "ORIGIN"
        step = fasta.replace(' ','').replace('\n','').replace('//','').replace('\r','')         # Verwijder alles behalve de getallen
        seq = re.sub(r'\d+', '', step)                  # Verwijder de getallen
        seq = seq.replace('t', 'u')
        return seq
    
    
    def cds(seq):

        aug = re.search('aug', seq)
        n = aug.start()
        pos1 = aug.start()
        stop = False
        
        while not stop:
            
            if "uga" in seq[n:n+3]:
                stop = True
                return seq[pos1:n+3]
            elif "uaa" in seq[n:n+3]:
                stop = True
                return seq[pos1:n+3]
            elif "uag" in seq[n:n+3]:
                stop = True
                return seq[pos1:n+3]
            else:
                n+=3

          
    def split(string, num):                                                            #Dit spilt de sequentie in codons van 3
        return [ string[start:start+num] for start in range(0, len(string), num) ]  
    
    
    def freq(lijst):
        counts = Counter(lijst)
        return counts
    
    
    def sd(a):
        counts = Counter(a).values()
        lijst = []
        for i in counts:
            lijst.append(i)
        mean = np.mean(lijst)
        sd = np.std(lijst)
        return sd
    
        
# ----------------------------------------- Codon/aminoacid percentages -----------------------------------------------    
    
    def subb(apart, choice):
        
        code_aa = {"ala ": ["gcu" , "gcc" , "gca" , "gcg"] ,
        "arg": ["cgu" , "cgc" , "cga" , "cgg" , "aga" , "agg"] ,
        "asn": ["aau" , "aac"] ,
        "asp": ["gau" , "gac"] ,
        "cys": ["ugu" , "ugc"] ,
        "gln": ["caa" , "cag"] ,
        "glu": ["gaa" , "gag"] ,
        "gly": ["ggu" , "ggc" , "gga" , "ggg"] ,
        "his": ["cau" , "cac"] ,
        "ile": ["auu" , "auc" , "aua"] ,
        "leu": ["uua" , "uug" , "cuu" , "cuc" , "cua" , "cug"] ,
        "lys": ["aaa" , "aag"] ,
        "met": ["aug"] ,
        "phe": ["uuu" , "uuc"] ,
        "pro": ["ccu" , "ccc" , "cca" , "ccg"] ,
        "ser": ["ucu" , "ucc" , "uca" , "ucg" , "agu" ,"agc"] ,
        "thr": ["acu" , "acc" , "aca" , "acg"] ,
        "trp": ["ugg"] ,
        "tyr": ["uau" , "uac"] ,
        "val": ["guu" , "guc" , "gua" , "gug"] ,
        "start": ["aug" , "cug" , "uug" , "gug" , "auu"] ,
        "stop" : ["uag" , "uga" , "uaa"]}
        

        code = {"ala ": [(apart.count('gcu')) , (apart.count("gcc")) , (apart.count("gca")) , (apart.count("gcg"))],
        "arg": [(apart.count("cgu")) , (apart.count("cgc")) , (apart.count("cga")) , (apart.count("cgg")) , (apart.count("aga")) , (apart.count("agg"))] ,
        "asn": [(apart.count("aau")) , (apart.count("aac"))] ,
        "asp": [(apart.count("gau")) , (apart.count("gac"))] ,
        "cys": [(apart.count("ugu")) , (apart.count("ugc"))] ,
        "gln": [(apart.count("caa")) , (apart.count("cag"))] ,
        "glu": [(apart.count("gaa")) , (apart.count("gag"))] ,
        "gly": [(apart.count("ggu")) , (apart.count("ggc")) , (apart.count("gga")) , (apart.count("ggg"))] ,
        "his": [(apart.count("cau")) , (apart.count("cac"))] ,
        "ile": [(apart.count("auu")) , (apart.count("auc")) , (apart.count("aua"))] ,
        "leu": [(apart.count("uua")) , (apart.count("uug")) , (apart.count("cuu")) , (apart.count("cuc")) , (apart.count("cua")) , (apart.count("cug"))] ,
        "lys": [(apart.count("aaa")) , (apart.count("aag"))] ,
        "met": [(apart.count("aug"))] ,
        "phe": [(apart.count("uuu")) , (apart.count("uuc"))] ,
        "pro": [(apart.count("ccu")) , (apart.count("ccc")) , (apart.count("cca")) , (apart.count("ccg"))] ,
        "ser": [(apart.count("ucu")) , (apart.count("ucc")) , (apart.count("uca")) , (apart.count("ucg")) , (apart.count("agu")) ,(apart.count("agc"))] ,
        "thr": [(apart.count("acu")) , (apart.count("acc")) , (apart.count("aca")) , (apart.count("acg"))] ,
        "trp": [(apart.count("ugg"))] ,
        "tyr": [(apart.count("uau")) , (apart.count("uac"))] ,
        "val": [(apart.count("guu")) , (apart.count("guc")) , (apart.count("gua")) , (apart.count("gug"))] ,
        "start": [(apart.count("aug")) , (apart.count("cug")) , (apart.count("uug")) , (apart.count("gug")) , (apart.count("auu"))] ,
        "stop" : [(apart.count("uag")) , (apart.count("uga")) , (apart.count("uaa"))]}
        
        print(code)
        values_code = list(code.values())
        
        lijst_percen = []
            
        n = 0
        for i in values_code:
            temp = []
            n += 1
            u = 0

            for x in i:
                a = sum(i)
                if a != 0:
                    percen = (x/a)*100
                    u += 1
                    temp.append(percen)
                else:
                    u += 1
                    temp.append(0)
                        
            lijst_percen.append(temp)

        
#--------------------Lists for plots------------------------------------------------                

        
        aminos_l_1 = []
        aminos_l_2 = []
        aminos_l_3 = []
        aminos_l_4 = []
        aminos_l_5 = []
        aminos_l_6 = []
        
        for x in range(0, len(values_code)):
            aminos_l_1.append(0)
            aminos_l_2.append(0)
            aminos_l_3.append(0)
            aminos_l_4.append(0)
            aminos_l_5.append(0)
            aminos_l_6.append(0)
        
        
        for x in range(len(lijst_percen)):
            z = lijst_percen[x]
            for y in range(len(z)):
                if y == 0:
                    aminos_l_1[x] = z[y]
                elif y == 1:
                    aminos_l_2[x] = z[y]
                elif y == 2:
                    aminos_l_3[x] = z[y]
                elif y == 3:
                    aminos_l_4[x] = z[y]
                elif y == 4:
                    aminos_l_5[x] = z[y]
                elif y == 5:
                    aminos_l_6[x] = z[y]
    
                
                
        
        raw_data = {'aminozuren':['ala ', 'arg', 'asn', 'asp', 'cys', 'gln', 'glu', 'gly', 'his', 'ile', 'leu', 'lys', 'met', 'phe', 'pro', 'ser', 'thr', 'trp', 'tyr', 'val', 'start', 'stop'],
        'Codon1': aminos_l_1,
        'Codon2': aminos_l_2,
        'Codon3': aminos_l_3,
        'Codon4': aminos_l_4,
        'Codon5': aminos_l_5,
        'Codon6': aminos_l_6}
        df = pd.DataFrame(raw_data, columns = ['aminozuren', 'Codon1', 'Codon2', 'Codon3', 'Codon4', 'Codon5', 'Codon6'])
        #print (df)

    
        # Create the general blog and the "subplots" i.e. the bars
        f, ax1 = plt.subplots(1, figsize=(22,7))
        
        # Set the bar width
        bar_width = 0.75
    
        # positions of the left bar-boundaries
        bar_l = [i+1 for i in range(len(df['Codon1']))] 
    
        # positions of the x-axis ticks (center of the bars as bar labels)
        tick_pos = [i+(bar_width/2) for i in bar_l] 
    
    
        # Create a bar plot, in position bar_1
        ax1.bar(bar_l, 
                # using the pre_score data
                df['Codon1'], 
                  # set the width
                  width=bar_width,
                  # with the label pre score
                  label='Codon1', 
                  # with alpha 0.5
                  alpha=0.5, 
                  # with color
                  color='lightblue')
    
        # Create a bar plot, in position bar_1
        ax1.bar(bar_l, 
                # using the mid_score data
                df['Codon2'], 
                # set the width
                width=bar_width,
                # with pre_score on the bottom
                bottom=df['Codon1'], 
                # with the label mid score
                label='Codon2', 
                # with alpha 0.5
                alpha=0.5, 
                # with color
                color='gray')
    
        # Create a bar plot, in position bar_1
        ax1.bar(bar_l, 
                # using the post_score data
                df['Codon3'], 
                # set the width
                width=bar_width,
                # with pre_score and mid_score on the bottom
                bottom=[i+j for i,j in zip(df['Codon1'],df['Codon2'])], 
                # with the label post score
                label='Codon3', 
                # with alpha 0.5
                alpha=0.5, 
                # with color
                color='pink')
    
        ax1.bar(bar_l, 
                # using the post_score data
                df['Codon4'], 
                # set the width
                width=bar_width,
                # with pre_score and mid_score on the bottom
                bottom=[i+j+k for i,j,k in zip(df['Codon1'],df['Codon2'], df["Codon3"])], 
                # with the label post score
                label='Codon4', 
                # with alpha 0.5
                alpha=0.5, 
                # with color
                color='red')
        
        ax1.bar(bar_l, 
                # using the post_score data
                df['Codon5'], 
                # set the width
                width=bar_width,
                # with pre_score and mid_score on the bottom
                bottom=[i+j+k+l for i,j,k,l in zip(df['Codon1'],df['Codon2'], df["Codon3"], df["Codon4"])], 
                # with the label post score
                label='Codon5', 
                # with alpha 0.5
                alpha=0.5, 
                # with color
                color='lightgreen')
        
        ax1.bar(bar_l, 
                # using the post_score data
                df['Codon6'], 
                # set the width
                width=bar_width,
                # with pre_score and mid_score on the bottom
                bottom=[i+j+k+l+m for i,j,k,l,m in zip(df['Codon1'],df['Codon2'], df["Codon3"], df["Codon4"], df["Codon5"])], 
                # with the label post score
                label='Codon6', 
                # with alpha 0.5
                alpha=0.5, 
                # with color
                color='blue')
        # set the x ticks with names
        plt.xticks(tick_pos, df['aminozuren'])
        
        # Set the label and legends
        ax1.set_ylabel("codon percentage")
        ax1.set_xlabel("aminozuren")
        plt.legend(loc='upper left')
        
        # Set a buffer around the edge
        plt.xlim([min(tick_pos)-bar_width, max(tick_pos)+bar_width])
        
        plt.show()
        
        
        
    def legend(choice):
            
        lijst1= ["GCU","CGU","AAU","GAU","UGU","CAA","GAA","GGU","CAU","AUU","UUA","AAA","AUG","UUU","CCU","UCU","ACU","UGG","UAU","GUU","AUG","UAG"]
        lijst2= ["GCC","CGC","AAC","GAC","UGC","CAG","GAG","GGC","CAC","AUC","UUG","AAG","-","UUC","CCC","UCC","ACC","-","UAC","GUC","CUG","UGA"]
        lijst3= ["GCA","CGA","-","-","-","-","-","GGA","-","AUA","CUU","-","-","-","CCA","UCA","ACA","-","-","GUA","UUG","UAA"]
        lijst4= ["GCG","CGG","-","-","-","-","-","GGG","-","-","CUC","-","-","-","CCG","UCG","ACG","-","-","GUG","GUG","-"]
        lijst5= ["-","AGA","-","-","-","-","-","-","-","-","CUA","-","-","-","-","AGU","-","-","-","-","AUU","-"]
        lijst6= ["-","AGG","-","-","-","-","-","-","-","-","CUG","-","-","-","-","AGC","-","-","-","-","-","-"]
        
        
        raw_data = {'Aminozuren':['ala', 'arg', 'asn', 'asp', 'cys', 'gln', 'glu', 'gly', 'his', 'ile', 'leu', 'lys', 'met', 'phe', 'pro', 'ser', 'thr', 'trp', 'tyr', 'val', 'start', 'stop'],
        'Codon1': lijst1,
        'Codon2': lijst2,
        'Codon3': lijst3,
        'Codon4': lijst4,
        'Codon5': lijst5,
        'Codon6': lijst6}
        legend = pd.DataFrame(raw_data, columns = ['Aminozuren', 'Codon1', 'Codon2', 'Codon3', 'Codon4', 'Codon5', 'Codon6'])
        print ('\nLegenda (',choice,'):')
        
        
        tb = plt.subplot(111, frame_on=False)
        tb.xaxis.set_visible(False)
        tb.yaxis.set_visible(False)
       
        table(tb, legend)
        
        
        
        
    main()

except FileNotFoundError:
    print("File not found")
    main()
#except NameError:
 #   print("Name error")
  #  main()
#except:
 #   print('Unknown error')
  #  main()