# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 13:43:58 2021

@author: asher
"""

fname = input("Please enter the input file name = ")

data=[]

nr=0;
try:
    file=open(fname,"r")
    for line in file:
        data.append(line)
    file.close()
    
except IOError:
    print("Error: coult not open file: ",fname)
    
print("dst  src  mode  value")
print("=====================")

i=0
j=0
for i in range(len(data)):
    if data[i] != "0000":
        #print(data[i])
        j=int(data[i],16)
        dig0=(j & 0b0000000001111111)
        dig1=(j & 0b0000000010000000) >> 7
        dig2=(j & 0b0000111100000000) >> 8
        dig3=(j & 0b1111000000000000) >> 12
        
        print('{:2d}'.format(dig3),'{:2d}'.format(dig2),
              '{:2d}'.format(dig1),'{:2d}'.format(dig0),sep='    ')
        
        