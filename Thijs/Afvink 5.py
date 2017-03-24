# -*- coding: utf-8 -*-
'''
Opdracht:
    
Schrijf een class gen die je de volgende attributen mee kunt geven:
    - Naam van het gen
    - DNA sequentie
    - Familienaam
    - Organisme
Daarnaast bevat de class de methode:
    - getTransscript
    - getTranslatie
Instantieer een class voor het humane p53 en p63, en roep de methodes aan.
'''
"""
Created on Thu Mar 16 16:26:06 2017

@author: thijs
"""
import re


class Gen:
    
    def __init__(self,naam,seq,fam,org):
        self.naam = naam
        self.seq = seq
        self.fam = fam
        self.org = org
        
    def setNaam(self,naam):
        self.naam = naam
    
    def getNaam(self):
        return self.naam


    def getTranscript(self):
        sequentie = self.seq
        sequentie = sequentie.replace('T','U')
        return sequentie
    
    def getTranslatie(self):
        sequentie = self.seq
        sequentie = sequentie.upper()
                      
        stop = False
        aug = re.search("ATG",sequentie)
        pos1 = aug.start()
        n = aug.start()
        
        while not stop:
            
            if "TGA" in sequentie[n:n+3]:
                stop = True
                coded = sequentie[pos1:n+3]
            
            elif "TAA" in sequentie[n:n+3]:
                stop = True
                coded = sequentie[pos1:n+3]
            
            elif "TAG" in sequentie[n:n+3]:
                stop = True
                coded = sequentie[pos1:n+3]
            
            else:
                n+=3
        
        coded = coded.lower()
        coding = [ coded[start:start+3] for start in range(0, len(coded), 3) ]
        
        
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
                'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G'}
            
        joined = ''.join(str(code.get(coding, coding)) for coding in coding)
        
        return joined
       




p53 = Gen('p53',open('p53 seq.txt').read(),'fam','org')
p63 = Gen('p63',open('p63 seq.txt').read(),'fam','org')