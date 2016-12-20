#ingest_aid for moving cpd.zips into cpd folders, and > 1Gig .zips into subfolders, automatic population of 'drush-commands' with namespace, target files, and and contentmodels
# designed to remove human error, and save time ingesting into islandora, via drush.

import os

#input = os.read()
#input list of .zips 'ownerinstitution-cdmalias-type.zip' 'uno-p15140coll23-jp2.zip' 'lsu-p1234coll1-cpd.zip' 'loyno-morethan1Gigcoll2-mp3.zip'
#desired changes are for zips that are simple (not contain 'cpd' in filename) and less than 1 gig stay where they are.
#for cpd.zips they get moved into a folder: ie 'lsu1234coll1-cpd/lsu1234coll1-cpd.zip' 
#.zips that are simple only (not containing *cpd* in name) and are > 1Gig in size, must also go in a subfolder. IE: 'loyno-morethan1Gigcoll2-mp3/loyno-morethan1Gigcoll2-mp3.zip'

filelist=['uno-p15140coll1-cpd.zip','uno-p151234coll2-jp2.zip','lsu-1gig-mp3.zip']

def cpd_subdir(zip_list):
 for line in zip_list:
  if 'cpd' in line:
   print(line[:-4])
   os.mkdir(line[:-4])
   os.rename(line, line[:-4]+'/'+line)

#with open('list','r',encoding='utf8') as f:
#    filelist=[i for i in f.readlines()]

cpd_subdir(filelist)

def large_zip_subdir(zip_list):
	for line in zip_list:
		if os.stat(line).st_size > 2450:
			print('bigfile')

large_zip_subdir(filelist)
	

#drush commands have 3 forms, cpd-subfolder, simple.zip, >1gig-subfolder/ 
#def drush_ingest_writer():
	
