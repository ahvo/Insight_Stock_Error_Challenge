#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 14:39:30 2018

@author: Andy Vo (anhahvo@gmail.com)
"""

#Python code to read in actual and predicted values for stock prices are different time points and calculate average error across specified moving time window.  

#Run run.sh in main folder to execute code or use python3 run_job.py ./input/window.txt ./input/actual.txt ./input/predicted.txt ./output/comparison.txt

#Used to read arguments (input/output paths) from command line and to exit code in case of error.   
import sys

#Used to detect missing files
import os.path

#Function to check and read in each input file and exit if error.
def readFile(direc):
    if not os.path.isfile(direc):
        print('ERROR: The Input File: ' + direc + ' is Missing.  Please Check Input File.')
        sys.exit()
    else:
        with open(direc,'r') as f_in:
            lines = list(line for line in (l.strip() for l in f_in) if line)
            if len(lines) == 0:
                print('ERROR: The Input File: ' + direc + ' is Empty.  Please Check Input File.')
                sys.exit()
            else:
                return(lines)
                
#Read in command line arguments (input/output paths).
window_file = sys.argv[1]
actual_file = sys.argv[2]
predicted_file = sys.argv[3]
output_file = sys.argv[4]
 
#Read in first line of window input file and check to make sure value is an integer.
window=readFile(window_file)[0]

if window.isdigit():
    window=int(window)
else:
    print('ERROR: Incorrect Window Number Detected. Please Check Input File.')
    sys.exit()

#read in actual and predicted stock price input files
actual=readFile(actual_file)
predicted=readFile(predicted_file)

#Create dictionaries from actual and predicted data.  "Time|Stock" are defined as keys and "Prices" are defined as values. 
actual_dict={i.rsplit('|', 1)[0]:float(i.rsplit('|', 1)[1]) for i in actual }
predicted_dict={i.rsplit('|', 1)[0]:float(i.rsplit('|', 1)[1]) for i in predicted }      

#Intersect keys above to find matching data.  New error dictionary where matching "Time|Stock" are defined as keys and "error" is defined as values. 
intersect_keys=list(set(actual_dict.keys()) & set(predicted_dict.keys()))
error_dict={key:abs(actual_dict[key]-predicted_dict[key]) for key in intersect_keys}

#Obtain the largest time point to be used in sliding window.
time_list=[int(i.split('|')[0]) for i in intersect_keys]
max_num=max(time_list)

#Obtain stock names from matching data.
stock_names=list(set([i.split('|')[1] for i in intersect_keys]))

#Check to make sure window size is appropriate.
#Calculate overall average error (rounded and formatted to two decimal spots) and write results to output file. Write NA if none found. 
i=1
if max_num < window: 
    print('ERROR: Window Number is Larger Than Time Span in Data.  Please choose a small number.')
    sys.exit()
else:
    with open (output_file,'w') as fout:
        while max_num-i+1 >= window:
            seq_number=list(range(i,i+window))
            numbers=[error_dict['|'.join([str(time),name])] for name in stock_names for time in seq_number if  '|'.join([str(time),name]) in error_dict]
            if len(numbers) == 0:
                fout.write(str(seq_number[0])+'|'+str(seq_number[-1])+'|NA\n')
            else:
                mean=sum(numbers) / float(len(numbers))
                Rounded_Mean= '{:.2f}'.format(round(mean, 2))
                fout.write(str(seq_number[0])+'|'+str(seq_number[-1])+'|'+str(Rounded_Mean)+'\n')
            i=i+1

#Code ran to completion.            
print('Prediction Validation is Complete.  Data is written to ' + output_file)
    
 


