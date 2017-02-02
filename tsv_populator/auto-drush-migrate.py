#!/usr/bin/env python3
# input should be a list of .zip filenames with institution-alias-filetype.zip
# some aliases included institution, we have altered them for the purpose of this script only
# script outputs .tsv with 'namespace => title' based on an input dictionary of alias-names file
# writes a drush command populated with namespace, and the .tsv file as input.
#------------------------------------------------------------TO DO---------------------------------------------------------------------
# to add content type flag for drush command, could add all types for default. or could crossref a filetypes => content-model dictionary
# incorporate into ingest_aid.py
import csv
import re
import requests

with open('alias-names', 'r', encoding='utf-8') as f:
    csv_reader = csv.reader(f, delimiter='\t')
    at_dict = {i:j for i, j in csv_reader}

prefix_url = 'http://ldl.lib.lsu.edu/islandora/object/'
check_dup = []
namespace = ''
alias = ''
title = ''

with open('input', 'r', encoding='utf-8') as f:
    for line in f:
        namespace = line[:-9]
        coll_url = '{0}{1}:collection'.format(prefix_url,namespace)
        print(coll_url)
        request = requests.get(coll_url)
        if request.status_code == 200:
            print('collection already exists')
        else:
            if namespace not in check_dup:
                check_dup.append(namespace)
                print(line + 'namespace = {}'.format(namespace))
                alias = re.search('(-.*)', namespace)
                alias = alias.group(0)
                alias = alias[1:]
                print('ailas = {}'.format(alias))
                title = at_dict[alias]
                print('title = {}'.format(title))
                tsvname ='{}.tsv'.format(namespace)
                tsvcontents = namespace + '\t' + title
                with open(tsvname, 'w') as f:
                    f.write(tsvcontents)
                print('tsv content = {}'.format(tsvcontents))
                drushcommand = 'drush --user=admin cicfc --input=/vagrant/{0}.tsv  --namespace={0}:collection --parent=islandora:root\n'.format(namespace)
                with open('drush-coll-migrate', 'a') as f:
                    f.write(drushcommand) 
                print('drush command = {}'.format(drushcommand))
            else:
                print('namespace duplicated, skipping tsv creation')
        #print(tsvcontents, file=tsvname)
        #write drush command to file.
