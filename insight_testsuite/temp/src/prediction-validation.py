#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 14:39:30 2018

@author: Andy
"""

#Sample execution python run_job.py ./input/window.txt ./input/actual.txt ./input/predicted.txt ./output/comparison.txt

#sys library for inputting files as arguments  
import sys

#import os 
#dir_path='/Users/zza847/Downloads/prediction-validation-master/insight_testsuite'
#dir_path = os.path.dirname(os.path.realpath(__file__))
#print('current working directory is: '+ dir_path)

#Function to check and read in each input file.
def readFile(direc):
    with open(direc,'r') as f_in:
        lines = list(line for line in (l.strip() for l in f_in) if line)
        if len(lines) == 0:
            print('ERROR: The input file :'+direc+' is empty')
        else:
            return(lines)
                

#input files    
#actual_file=dir_path+'/tests/test_1/input/actual.txt'
#predicted_file=dir_path+'/tests/test_1/input/predicted.txt'
#window_file=dir_path+'/tests/test_1/input/window.txt'

#Input file arguments into script
window_file = sys.argv[1]
actual_file = sys.argv[2]
predicted_file = sys.argv[3]
output_file = sys.argv[4]

#read in first line of file and use as window size
window=readFile(window_file)[0]
window=int(window) if window.isdigit() else print('need to input a number in the window.txt')

#read in predicted/actual files
actual=readFile(actual_file)
predicted=readFile(predicted_file)

#define the actual dic and predict_dict, the key is the tiime and stock name, the value is the value
actual_dict={i.rsplit('|', 1)[0]:float(i.rsplit('|', 1)[1]) for i in actual }
predicted_dict={i.rsplit('|', 1)[0]:float(i.rsplit('|', 1)[1]) for i in predicted }      

#define the error dict, key are the intesect of actual and predict
intersect_keys=list(set(actual_dict.keys())& set(predicted_dict.keys()))
error_dict={key:abs(actual_dict[key]-predicted_dict[key]) for key in intersect_keys}

#define the largest number for the slide window
time_list=[int(i.split('|')[0]) for i in intersect_keys]
max_num=max(time_list)

#find the stock from the intesect            
stock_names=list(set([i.split('|')[1] for i in intersect_keys]))

#calculate the error
i=1
print('max time is larger than sliding window? passed') if max_num-i+1 >=window else print('the time collected is less than window')
with open (output_file,'w') as fout:
    while max_num-i+1 >= window:
        seq_number=list(range(i,i+window))
        numbers=[error_dict['|'.join([str(time),name])] for name in stock_names for time in seq_number if  '|'.join([str(time),name]) in error_dict]
        if len(numbers) ==0:
            fout.write(str(seq_number[0])+'|'+str(seq_number[-1])+'|NA\n')
        else:
            mean=sum(numbers) / float(len(numbers))
            Rounded_Mean= '{:.2f}'.format(round(mean, 2))
            fout.write(str(seq_number[0])+'|'+str(seq_number[-1])+'|'+str(Rounded_Mean)+'\n')
        i=i+1
    
 


