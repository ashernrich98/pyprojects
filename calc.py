# -*- coding: utf-8 -*-
"""
Created on Thur Mar 25 2021

@author: asher
"""

import tkinter as tk

class myApp:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()
        tk.Label(frame, text='1. Operand = ').grid(row=0, column=0)
        self.a_var = tk.DoubleVar()
        tk.Entry(frame, textvariable=self.a_var).grid(row=0, column=1)
        
        tk.Label(frame, text='2. Operand = ').grid(row=1, column=0)
        self.b_var = tk.DoubleVar()
        tk.Entry(frame, textvariable=self.b_var).grid(row=1, column=1)
        
        button=tk.Button(frame,text='ADD',bg='aqua',fg='white',command=self.add)
        button.grid(row=2,column=0)
        
        button=tk.Button(frame,text='SUB',bg='navy',fg='white',command=self.sub)
        button.grid(row=2,column=1)
        
        button=tk.Button(frame,text='CLR',bg='red',fg='white',command=self.clear)
        button.grid(row=2,column=2)
        
        tk.Label(frame,text='Result = ').grid(row=3,column=0)
        self.result_var=tk.DoubleVar()
        tk.Label(frame,textvariable=self.result_var).grid(row=3,column=1)
        
    def add(self):
        a = self.a_var.get()
        b = self.b_var.get()
        c = float(a+b)
        self.result_var.set("{:.3f}".format(c))
        
    def sub(self):
        a = self.a_var.get()
        b = self.b_var.get()
        c = float(a-b)
        self.result_var.set("{:.3f}".format(c))
         
    def clear(self):
        self.result_var.set(0.0)
        
root = tk.Tk()
root.wm_title('ANR Calc')
app = myApp(root)
root.mainloop()