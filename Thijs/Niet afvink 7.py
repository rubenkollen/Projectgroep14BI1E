# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 13:04:41 2017

@author: thijs
"""

import tkinter as gui
from tkinter import messagebox

class GUI:
    
    def __init__(self):
        self.main_window = gui.Tk()
        self.frame = gui.Frame(self.main_window)
        self.my_button = gui.Button(self.main_window, text='Execute',command = self.conversion)
        
        self.my_button.pack()
        self.invoer = gui.Entry(self.main_window, width = 30)
        self.invoer.pack()
        
        self.value = gui.StringVar()
        self.value_label = gui.Label(self.main_window, textvariable = self.value)
        
        self.value_label.pack()
        
        self.frame.pack()
        gui.mainloop()
        
    
    def conversion(self):
        tekst = self.invoer.get()
        converse = tekst.replace('T','U')
        
        
        
        
        self.value.set(converse)
        
        
Interface = GUI()        
        
        