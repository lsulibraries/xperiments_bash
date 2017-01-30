#!/usr/bin/env python3
# input should be a list of .zip filenames with institution-alias-filetype.zip
# some aliases included institution, we have altered them for the purpose of this script only
# script outputs .tsv with 'namespace => title' based on an input dictionary of alias-names file
# writes a drush command populated with namespace, and the .tsv file as input.
#------------------------------------------------------------TO DO---------------------------------------------------------------------
# to add content type flag for drush command, could add all types for default. or could crossref a filetypes => content-model dictionary
# check for duplicated namespace in input (list of zips) (ie lsu-acc-jp2.zip and lsu-acc-cpd.zip in same list) if true skip second tsv and drush command.
# check whether ldl.lib.lsu.edu/islandora/object/{namespace}:collection exists yet (curl)
# incorporate into ingest_aid.py
import csv
import re

with open('alias-names', 'r', encoding='utf-8') as f:
    csv_reader = csv.reader(f, delimiter='\t')
    at_dict = {i:j for i, j in csv_reader}

#print(at_dict)

namespace = ''
alias = ''
title = ''

with open('zips', 'r', encoding='utf-8') as f:
    for line in f:
        namespace = line[:-9]
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
        drushcommand = 'drush --user=admin cicfc --input=/tmp/{0}.tsv  --namespace={0}:collection --parent=islandora:root\n'.format(namespace)
        with open('drush-coll-migrate', 'a') as f:
             f.write(drushcommand) 
        print('drush command = {}'.format(drushcommand))
        #print(tsvcontents, file=tsvname)
        #write drush command to file.
