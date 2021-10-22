import pandas as pd
from copy import deepcopy
from pprint import pprint

destination = pd.read_csv("<path>") #read the file where you want to replace values
source = pd.read_excel("/Users/mditu/Downloads/table_cibles_wp x LR_final.xlsx", header=[0, 1])["General Settings"][["Kantar_WP_ID","csv segment name"]] #read the file which contains the values that you want to use as replacement

d = {k: v for v, k in source.values} #create a dictionary to store (k,v) pairs 
l = [] 

for x in destination.columns:
    try:
        search_term = x.split('>')[-2].strip() #the value that we’re looking for
        search_result = d.get(search_term, x) #store in search_result the value you found should be used as replacement
        l.append(search_result) #add then new value to the list
    except IndexError:
        l.append(x) #if no value was found keep the old value

destination.columns = l #amend the column header with the new value stored in the l list
destination.to_csv("<path_save_file>") #save the file as a csv
