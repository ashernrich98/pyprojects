#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 19:40:50 2021

@author: Asher
"""

import tkinter as tk
#import time

fname = input("Please enter the input file name = ")
in_port = int(input("Please enter R[0]=in_port value in decimal 0..255 = "))

fin = open(fname,"r")
prog = fin.readlines()
fin.close()

data=[]

k=0;
for k in range(len(prog)):
    if(prog[k] != '0000\n'):
        data.append(prog[k])
    k += 1

class myApp:
    
    R = [-1] * 18
    R[0] = in_port
    
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()
    
        # ===== TITLE LABELS =====
        
        tk.Label(frame,text='Name').grid(row=0,column=0)
        tk.Label(frame,text='Value').grid(row=0,column=1)
        tk.Label(frame,text='----').grid(row=0,column=2)
        
        tk.Label(frame,text='Name').grid(row=0,column=3)
        tk.Label(frame,text='Value').grid(row=0,column=4)
        tk.Label(frame,text='----').grid(row=0,column=5)
        
        tk.Label(frame,text='Name').grid(row=0,column=6)
        tk.Label(frame,text='Value').grid(row=0,column=7)
        
        # ===== VAR LABELS =====
        
        tk.Label(frame,text='CLK').grid(row=1,column=0)
        tk.Label(frame,text='R[0]').grid(row=1,column=3)
        tk.Label(frame,text='R[8]').grid(row=1,column=6)
        
        tk.Label(frame,text='PC').grid(row=2,column=0)       
        tk.Label(frame,text='R[1]').grid(row=2,column=3)     
        tk.Label(frame,text='R[9]').grid(row=2,column=6)
        
        tk.Label(frame,text='IW').grid(row=3,column=0)       
        tk.Label(frame,text='R[2]').grid(row=3,column=3)     
        tk.Label(frame,text='R[10]').grid(row=3,column=6)
        
        tk.Label(frame,text='DST').grid(row=4,column=0)       
        tk.Label(frame,text='R[3]').grid(row=4,column=3)     
        tk.Label(frame,text='R[11]').grid(row=4,column=6)
        
        tk.Label(frame,text='SRC').grid(row=5,column=0)       
        tk.Label(frame,text='R[4]').grid(row=5,column=3)     
        tk.Label(frame,text='R[12]').grid(row=5,column=6)
        
        tk.Label(frame,text='MODE').grid(row=6,column=0)       
        tk.Label(frame,text='R[5]').grid(row=6,column=3)     
        tk.Label(frame,text='R[13]').grid(row=6,column=6)
        
        tk.Label(frame,text='ADDR').grid(row=7,column=0)       
        tk.Label(frame,text='R[6]').grid(row=7,column=3)     
        tk.Label(frame,text='R[14]').grid(row=7,column=6)
        
        tk.Label(frame,text='R[DST]').grid(row=8,column=0)       
        tk.Label(frame,text='R[7]').grid(row=8,column=3)     
        tk.Label(frame,text='R[15]').grid(row=8,column=6)
        
        tk.Label(frame,text='R[SRC]').grid(row=9,column=0)   
        
        tk.Label(frame,text='Result = ').grid(row=10,column=0)
        
        # ===== VAR DECLARATIONS/INITIAL ASSIGNMENTS =====
        
        self.counter = tk.IntVar()
        self.pc = tk.IntVar()
        
        self.data_len = tk.IntVar()
        self.data_len.set(len(data))
        
        self.iw = tk.StringVar()
        self.dst = tk.IntVar()
        self.src = tk.IntVar()
        self.mode = tk.IntVar()
        self.addr = tk.IntVar()
        
        self.r0 = tk.IntVar()
        
        self.r1 = tk.IntVar()
        self.r2 = tk.IntVar()
        self.r3 = tk.IntVar()
        self.r4 = tk.IntVar()
        self.r5 = tk.IntVar()
        self.r6 = tk.IntVar()
        self.r7 = tk.IntVar()
        self.r8 = tk.IntVar()
        self.r9 = tk.IntVar()
        self.r10 = tk.IntVar()
        self.r11 = tk.IntVar()
        self.r12 = tk.IntVar()
        self.r13 = tk.IntVar()
        self.r14 = tk.IntVar()
        self.r15 = tk.IntVar()
        self.r_dst = tk.IntVar()
        self.r_src = tk.IntVar()
        
        self.result_var = tk.IntVar()
        self.iw.set(self.getdata())
    
        iw = self.getinst()
        i = int(iw, 16)
        temp_dst=(i & 0b1111000000000000) >> 12
        temp_src=(i & 0b0000111100000000) >> 8
        temp_mode=(i & 0b0000000010000000) >> 7
        temp_val=(i & 0b0000000001111111)
        self.dst.set(temp_dst)
        self.src.set(temp_src)
        self.mode.set(temp_mode)
        self.addr.set(temp_val)
        
        self.R[16] = temp_dst
        self.R[17] = temp_src
        
        result = self.R[16] - self.R[17]
        self.result_var.set(result)
        self.R[result] = self.R[16]
        
        # Attempt from urisc.v
        # result = self.result_var.get()
        
        # self.R[temp_dst] = result
        
        # if result >= 0:
        #     self.pc.set(self.pc.get()+1)
        # else:
        #     if (temp_mode):
        #         self.pc.set(temp_val)
        #     else:
        #         self.pc.set(self.pc.get()+temp_val)
                
        self.setreg(self.R)
        
        # ===== VAR LABEL VALUES =====
        
        #CLK
        tk.Label(frame,textvariable=self.counter).grid(row=1,column=1)
        #R0
        tk.Label(frame,textvariable=self.r0).grid(row=1,column=4)
        #R8
        tk.Label(frame,textvariable=self.r8).grid(row=1,column=7)
        
        #PC
        tk.Label(frame,textvariable=self.pc).grid(row=2,column=1)
        #R1
        tk.Label(frame,textvariable=self.r1).grid(row=2,column=4)
        #R9
        tk.Label(frame,textvariable=self.r9).grid(row=2,column=7)
        
        #IW
        tk.Label(frame,textvariable=self.iw).grid(row=3,column=1)
        #R2
        tk.Label(frame,textvariable=self.r2).grid(row=3,column=4)
        #R10
        tk.Label(frame,textvariable=self.r10).grid(row=3,column=7)
        
        #DST   
        tk.Label(frame,textvariable=self.dst).grid(row=4,column=1)
        #R3   
        tk.Label(frame,textvariable=self.r3).grid(row=4,column=4)
        #R11
        tk.Label(frame,textvariable=self.r11).grid(row=4,column=7)
        
        #SRC
        tk.Label(frame,textvariable=self.src).grid(row=5,column=1)      
        #R4
        tk.Label(frame,textvariable=self.r4).grid(row=5,column=4)
        #R12
        tk.Label(frame,textvariable=self.r12).grid(row=5,column=7)
        
        #MODE
        tk.Label(frame,textvariable=self.mode).grid(row=6,column=1)
        #R5
        tk.Label(frame,textvariable=self.r5).grid(row=6,column=4)
        #R13
        tk.Label(frame,textvariable=self.r13).grid(row=6,column=7)
        
        #ADDR
        tk.Label(frame,textvariable=self.addr).grid(row=7,column=1)
        #R6
        tk.Label(frame,textvariable=self.r6).grid(row=7,column=4)
        #R14
        tk.Label(frame,textvariable=self.r14).grid(row=7,column=7)
        
        #R DST
        tk.Label(frame,textvariable=self.r_dst).grid(row=8,column=1)
        #R7
        tk.Label(frame,textvariable=self.r7).grid(row=8,column=4)
        #R15
        tk.Label(frame,textvariable=self.r15).grid(row=8,column=7)
        
        #R SRC
        tk.Label(frame,textvariable=self.r_src).grid(row=9,column=1)
        
        #RESULT
        tk.Label(frame,textvariable=self.result_var).grid(row=10,column=1)
        
        # ===== BUTTONS =====
        
        #NOTE: on mac the buttons don't change color so I couldn't see the text
        #while testing but it looks much nicer in white
        #button=tk.Button(frame,text='STEP',bg='aqua',fg='white',command=self.step)
        button=tk.Button(frame,text='STEP',bg='aqua',fg='black',command=self.step)
        button.grid(row=11,column=0)
        
        #button=tk.Button(frame,text='STEP 10',bg='navy',fg='white',command=self.step10)
        button=tk.Button(frame,text='STEP 10',bg='navy',fg='black',command=self.step10)
        button.grid(row=11,column=3)
        
        #button=tk.Button(frame,text='RESET',bg='red',fg='white',command=self.reset)
        button=tk.Button(frame,text='RESET',bg='red',fg='black',command=self.reset)
        button.grid(row=11,column=6)
        
        #button=tk.Button(frame,text='SMILE',bg='green',fg='white',command=self.smile)
        button=tk.Button(frame,text='SMILE',bg='green',fg='black',command=self.smile)
        button.grid(row=12,column=2)
        
        #button=tk.Button(frame,text='CRY',bg='blue',fg='white',command=self.cry)
        button=tk.Button(frame,text='CRY',bg='blue',fg='black',command=self.cry)
        button.grid(row=12,column=5)
        
        # ===== BUTTON FUNCTIONS =====
        
    def step(self):
        count = self.counter.get()
        self.counter.set(count+1)
        
        # this would need to be deleted for failed attempts (1)
        progc = self.pc.get()
        d_len = self.data_len.get()
        
        if progc == (d_len-2):
            self.pc.set(0)
        else:
            self.pc.set(progc+1)
        
        self.iw.set(self.getdata())
        
        iw = self.getinst()
        i = int(iw, 16)
        temp_dst=(i & 0b1111000000000000) >> 12
        temp_src=(i & 0b0000111100000000) >> 8
        temp_mode=(i & 0b0000000010000000) >> 7
        temp_val=(i & 0b0000000001111111)
        self.dst.set(temp_dst)
        self.src.set(temp_src)
        self.mode.set(temp_mode)
        self.addr.set(temp_val)
        
        self.R[16] = temp_dst
        self.R[17] = temp_src
        
        result = self.R[16] - self.R[17]
        self.result_var.set(result)
        self.R[result] = self.R[16]
        
        # --- Failed Attempts (1)
        
        # self.R[16] = temp_dst
        # self.R[17] = temp_src
        
        # result = self.result_var.get()
        # self.result_var.set(self.R[16]-self.R[17])
        
        # self.R[temp_dst] = result
        
        # if result >= 0:
        #     self.pc.set(self.pc.get()+1)
        # else:
        #     if (temp_mode):
        #         self.pc.set(temp_val)
        #     else:
        #         self.pc.set(self.pc.get()+temp_val)
                
        # self.setreg(self.R)
    
        
        # --- Failed Attempts (2)
        
        # attempt to hard code the register values
        # resulted in a big migraine and wrong results
        # the best I got was the user input in R[15] but negative
        
        # R[DST] = R[DST] - R[SRC]
        # R[16] -> R[DST]
        # R[17] -> R[SRC]
        
        #check result
        #update register values at source and destination
        #update source and destination
        #update result

        # if result<0:
        #     # look at new IW for dst and src and reset registers after set
        #     destination = temp_dst
        #     source = temp_src
        #     R[destination] = destination
        #     R[source] = source
        #     self.result_var.set(R[16]-R[17])
        #     R[16] = -1
        #     R[17] = -1
            
        # else:
        #     #look at R[16] and R[17] for dst and src and set reg
        #     destination = R[16]
        #     source = R[17]
        #     R[destination] = destination
        #     R[source] = source
        #     self.result_var.set(R[16]-R[17])
        #     R[16] = R[16] - R[17]
        #     R[17] = source

        self.setreg(self.R)
        
    def step10(self):
        i=0
        for i in range(10):
            #time.sleep(1) << tried to do this to look at every iteration
            #the right thing to do is to call .configure method
            #but this makes the code much more complicated
            #so i left it as is because it will still step 10 times
            self.step()
         
    def reset(self):
        self.counter.set(0)
        self.result_var.set(0)
        self.pc.set(0)
        
        self.R = [-1] * 18
        self.R[0] = in_port
        self.setreg(self.R)
        
    def smile(self):
        self.result_var.set(":)")
    
    def cry(self):
        self.result_var.set(":*(")
        
    def getdata(self):
        index = self.pc.get()
        return data[index]
    
    def getinst(self):
        inst = str(self.iw.get())
        return inst
    
    def setreg(self,R):
        self.r0.set(R[0])
        self.r1.set(R[1])
        self.r2.set(R[2])
        self.r3.set(R[3])
        self.r4.set(R[4])
        self.r5.set(R[5])
        self.r6.set(R[6])
        self.r7.set(R[7])
        self.r8.set(R[8])
        self.r9.set(R[9])
        self.r10.set(R[10])
        self.r11.set(R[11])
        self.r12.set(R[12])
        self.r13.set(R[13])
        self.r14.set(R[14])
        self.r15.set(R[15])
        self.r_dst.set(R[16])
        self.r_src.set(R[17])
        # self.r_dst.set(self.dst.get())
        # self.r_src.set(self.src.get())
        
root = tk.Tk()
root.wm_title('ISS by ANR')
app = myApp(root)
root.mainloop()