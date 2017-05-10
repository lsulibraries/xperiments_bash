#ingest_aid for moving cpd.zips and >1Gig .zips into subfolders, automatic population of 'drush-commands' with namespace, srt files, and and contentmodels
# designed to remove human error, and save time ingesting into islandora, via drush.
#new functionality within tsv_populator creates drush command for cicfc drush ingest of collection containers.
import os
import shutil
#input = os.read()
#input list of .zips 'ownerinstitution-cdmalias-type.zip' 'uno-p15140coll23-jp2.zip' 'lsu-p1234coll1-cpd.zip' 'loyno-morethan1Gigcoll2-mp3.zip'
#desired changes are for zips that are simple (not contain 'cpd' in filename) and less than 1 gig stay where they are.
#for cpd.zips they get moved into a folder: ie 'lsu1234coll1-cpd/lsu1234coll1-cpd.zip' 
#.zips that are simple only (not containing *cpd* in name) and are > 1Gig in size, must also go in a subfolder. IE: 'loyno-morethan1Gigcoll2-mp3/loyno-morethan1Gigcoll2-mp3.zip'



def cpd_gig_dirmaking():
    filelist=[os.path.abspath(i) for i in os.listdir() if '.zip' in i]
    for i in filelist:
        print('{}'.format(i))
    for line in filelist:
        if 'cpd' in line:
            filename, ext = os.path.splitext(line)
            print('cpd file : {}'.format(filename))
            os.makedirs(filename, exist_ok=True)
            shutil.move(line, filename + '/')
        elif os.stat(line).st_size > 999999999:
            print('bigfile in directory: {}'.format(line))
            filename, ext = os.path.splitext(line)
            os.makedirs(filename, exist_ok=True)
            shutil.move(line, '{}/'.format(filename))

cpd_gig_dirmaking()

#drush commands have 3 forms, cpd-subfolder, simple.zip, >1gig-subfolder/ 

def drush_ingest_writer():
    filelist=[os.path.abspath(i) for i in os.listdir() if i not in ('cleanup.sh', 'drush-commands', 'ingest_aid.py')]
    #print('current state of zip paths and dirs: {}'.format(filelist))

    cmodels = {'pdf':'sp_pdf', 'jp2':'sp_large_image_cmodel', 'mp4':'sp_videoCModel', 'mp3':'sp-audioCModel'}
    for line in filelist:
        _, namespace_ext = os.path.split(line)
        print(_, namespace_ext)
        inst, ali, ext = namespace_ext.split('-')
        namespace = '{}-{}'.format(inst, ali)
        print(namespace)
        if ext == 'cpd':
            drush = 'drush --user=admin icbp --src={0} --namespace={1} --parent={1}:collection'.format(line, namespace)
        elif 'zip' in ext:
            ext, z  = ext.split('.')
            drush = 'drush --user=admin ibsp --type=zip --src={0} --content_models=islandora:{1} --namespace={2} --parent={2}:collection'.format(line, cmodels[ext], namespace)
        else:
            drush = 'drush --user=admin ibsp --type=directory --src={0} --content_models=islandora:{1} --namespace={2} --parent={2}:collection'.format(line, cmodels[ext], namespace)
        with open('drush-commands', 'a') as file:
            file.write(drush+'\n')

drush_ingest_writer()
