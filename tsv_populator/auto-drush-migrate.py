#!/usr/bin/env python3
# this script takes a list of input zips (with no repeated namespaces or those with pre-existing collection containers)
# the script writes a simple .tsv with 'alias => title' based on an input dictionary of alias title associations
# the script then writes a drush command populated with namespace, and the .tsv file as input.
import csv
import re

with open('alias-names', 'r', encoding='utf-8') as f:
    csv_reader = csv.reader(f, delimiter='\t')
    at_dict = {i:j for i, j in csv_reader}


namespace = ''
alias = ''
title = ''

with open('input', 'r', encoding='utf-8') as f:
    for line in f.readline():
        print(line)
        namespace = line[:-8]
        print(namespace)
        alias = re.search('/(-.*)/', namespace)
        #alias = alias[-1:]
        print(alias)
        #at-dict:namespace
        #write tsv to file
        #write drush command to file.
  
