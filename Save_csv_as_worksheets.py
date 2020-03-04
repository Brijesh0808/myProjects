#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import glob
import csv
from xlsxwriter import Workbook

#Make a workbook(xlsx file) and its object
path = '/home/brijesh/Documents/CSVfiles/output.xlsx'
wb_obj = Workbook(path)

#glob gives list of all files ending with .csv
for csv_file in glob.glob('/home/brijesh/Documents/CSVfiles/*.csv'):
    
    #To find name of csv file
    sheet_name = csv_file.split('/')[-1]
    sheet_name = sheet_name[:-4]
    
    #adding a worksheet to the workbook
    #add_worksheet returns an object
    ws_obj = wb_obj.add_worksheet(sheet_name)
    
    #To write the contents of csv_file in the worksheet created
    with open(csv_file, 'rt') as csv_obj:
        #create an object to read csv_file
        csv_reader = csv.reader(csv_obj)
        
        #csv_reader have rows of csv files
        #r stores index for rows
        #row is a list having elements as values in different columns
        for r, row in enumerate(csv_reader):
            # c stores index for col's
            for c in range(len(row)):
                ws_obj.write(r, c, row[c])
                
wb_obj.close()

