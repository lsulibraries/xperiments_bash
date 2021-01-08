import os, shutil, glob


#re-creating for new pattern 
#pattern <name>001.xml <name>001r.xml <name>001v.xml and jp2 respectively


#If I'm using underscores to split strings and create directories, I need to not use them in my nameing convention

def organize_cpd_structure():
    filelist = [os.path.abspath(i) for i in os.listdir()]
    #os.path.abspath(i) is for this file, ie ~/Desktop/Source
    #print(filelist)

    directories = glob.glob('*[0-9].xml')
    for xml in directories:
        #mkdir for every parent object, should always be the first half of *_*.whatever
        dir_path = xml[:-4]
        print(dir_path)
        os.makedirs(dir_path, exist_ok=True)
        shutil.move(xml, dir_path)
        others_r = glob.glob('{}r.*'.format(dir_path))
        others_v = glob.glob('{}v.*'.format(dir_path))
        os.makedirs('{}/r'.format(dir_path))
        os.makedirs('{}/v'.format(dir_path))
        for file in others_r:
            print(file)
            shutil.move(file, '{}/r'.format(dir_path))
        for file in others_v:
            print(file)
            shutil.move(file, '{}/v'.format(dir_path))


organize_cpd_structure()
