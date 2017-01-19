#ingest_aid for moving cpd.zips and >1Gig .zips into subfolders, automatic population of 'drush-commands' with namespace, target files, and and contentmodels
# designed to remove human error, and save time ingesting into islandora, via drush.
#new functionality within tsv_populator creates drush command for cicfc drush ingest of collection containers.
import os

#input = os.read()
#input list of .zips 'ownerinstitution-cdmalias-type.zip' 'uno-p15140coll23-jp2.zip' 'lsu-p1234coll1-cpd.zip' 'loyno-morethan1Gigcoll2-mp3.zip'
#desired changes are for zips that are simple (not contain 'cpd' in filename) and less than 1 gig stay where they are.
#for cpd.zips they get moved into a folder: ie 'lsu1234coll1-cpd/lsu1234coll1-cpd.zip' 
#.zips that are simple only (not containing *cpd* in name) and are > 1Gig in size, must also go in a subfolder. IE: 'loyno-morethan1Gigcoll2-mp3/loyno-morethan1Gigcoll2-mp3.zip'


filelist=[i for i in os.listdir() if '.zip' in i]
print(filelist)

def cpd_subdir(zip_list):
 for line in zip_list:
  if 'cpd' in line:
   print(line[:-4])
   os.mkdir(line[:-4])
   os.rename(line, line[:-4]+'/'+line)

#with open('list','r',encoding='utf8') as f:

cpd_subdir(filelist)

filelist=[i for i in os.listdir() if '.zip' in i]
print(filelist)

def large_zip_subdir(zip_list):
 for line in zip_list:
  if os.stat(line).st_size > 2450:
   print('bigfile', line)
   os.mkdir(line[:-4])
   os.rename(line, line[:-4]+'/'+line)

large_zip_subdir(filelist)
	
filelist=[i for i in os.listdir() if i != 'cleanup.sh' and i != 'ingest_aid.py']
print(filelist)


#drush commands have 3 forms, cpd-subfolder, simple.zip, >1gig-subfolder/ 

def drush_ingest_writer(zips_and_dirs):
cmodels = {'pdf':'sp_pdf', 'jp2':'sp_large_image_cmodel', 'mp4':'sp_videoCModel', 'mp3':'sp-audoCmodel'}
namespace=''
name_ext=''
ext=''
  for line in zips_and_dirs:
    if 'cpd' in line:
      #create drush for cpd
      drush = 'drush -u 1 icbp --target=/tmp/{}-cpd --namespace={} --parent={}:collection' namespace
    if 'cpd' not in line and 'zip' in line:
      #create drush for simple zip
      drush = 'drush -u 1 ibsp --type=zip --scan_target=/tmp/%s --content_models=islandora:%s --namespace=%s --parent=%s:collection' % (line, cmodel[ext], namespace, namespace)

    if '.zip' not in line and 'cpd' not in line:
      #create drush for >1 gig subfolder zip
      drush = 'drush -u 1 ibsp --type=directory --scan_target=/tmp/'"$line"' --content_models=islandora:'"${cmodels[$ext]}"' --namespace='"$namespace"' --parent='"$namespace"':collection'  % (line, cmodel[ext], namespace, namespace)
    open('drush-commands', 'a')
