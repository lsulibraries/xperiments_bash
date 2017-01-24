#!/usr/bin/env python3
# this script takes a list of input zips (with no repeated namespaces or those with pre-existing collection containers)
# the script writes a simple .tsv with 'alias => title' based on an input dictionary of alias title associations
# the script then writes a drush command populated with namespace, and the .tsv file as input.
import csv
import re

with open('alias-names', 'r', encoding='utf-8') as f:
    csv_reader = csv.reader(f, delimiter='\t')
    at_dict = {i:j for i, j in csv_reader}

#print(at_dict)

namespace = ''
alias = ''
title = ''

with open('input', 'r', encoding='utf-8') as f:
    for line in f:
        namespace = line[:-9]
        print(namespace)
        alias = re.search('(-.*)', namespace)
        alias = alias.group(0)
        alias = alias[1:]
        print(alias)
        title = at_dict[alias]
        print(title)
        tsvname = namespace + '.tsv'
        tsvcontents = namespace + '\t' + title
        with open(tsvname, 'w') as f:
            f.write(tsvcontents)
        drushcommand = 'drush --user=admin cicfc --input=/vagrant/%s.tsv  --namespace=%s:collection --parent=islandora:root\n'  %  (namespace, namespace)
        with open('drush-coll-migrate', 'a') as f:
             f.write(drushcommand) 
        
        #print(tsvcontents, file=tsvname)
        #write drush command to file.
  
