#!coding:utf-8

'''
=====================================
+      Input CSV format data        +
+   This code is write for ManLin   +
=====================================
'''

___time__ = "2018-07-15"
___author__ = "Wei"
___mail__ = "hanwei@shanghaitech.edu.cn"

import os
import pandas as pd

#Now you should give program your folder that save your data file
fold = input("Input your folder name: ")
#Get data file name as a list
dir_now = os.getcwd()
fold_path = dir_now + "\\" + fold
file_list = os.listdir(fold_path)

for filee in file_list:
	#Get absolute path of data file
	path = fold_path + "\\" + filee
	#Read data from file
	df = pd.read_csv(path)
	#Get max value and corresponding time
	value_max = df.max(axis=0)[1]
	time = [df['time'][i] for i in df.index if df['data'][i]==value_max]
	#Write result to output file
	with open("outdata.csv", 'a') as out:
		for line in time:
			out.write(filee + ',' + str(value_max) + ',' + line + '\n')
	print(filee + " is gone!")
	
	
