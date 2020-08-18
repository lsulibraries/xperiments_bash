import os, shutil


#add exception for '-3', '_Envelope' 
# I'm using some lazy directory creating methods. I think I should keep it to the current folder.

#If I'm using underscores to split strings and create directories, I need to not use them in my nameing convention

def organize_cpd_structure():
    filelist = [os.path.abspath(i) for i in os.listdir()]
    #os.path.abspath(i) is for this file, ie ~/Desktop/Source
    #print(filelist)
    for line in filelist:
        if '_' not in line:
            print('{}'.format(line))
            filename, ext = os.path.splitext(line)
            os.makedirs(filename, exist_ok=True)
    for line in filelist:
        #create directories for every child
        if ('_0') or ('_E') in line:
            #creates a directory for each object with children
            #main objects with '*_999' will always have children
            directory = line.split('_')
            objdir = '{}/'.format(directory[0])
            print(objdir)
            subfolder = directory[1]
            subfolder = subfolder.split('.')
            subdir = objdir + subfolder[0]
            print(subdir)
            os.makedirs(subdir, exist_ok=True)
    for line in filelist:
        #move the children to their directory and rename them
        if '_' in line:
            #Changed this condition from '_0' to '_' to account for '*_Envelope' 
            #works but currently is renaming Envelope the wrong way, also envelopes need their own folders...
            directory = line.split('_')
            objdir = '{}/'.format(directory[0])
            subfolder = directory[1]
            subfolder = subfolder.split('.')
            subdir = objdir + subfolder[0]
            if 'Envelope' in directory[0]:
                os.rename(line, 'MODS.xml')
                line = 'MODS.xml'
            if '.xml' in line:
                os.rename(line, 'MODS.xml')
                line = 'MODS.xml'
            if '.jp2' in line:
                os.rename(line, 'OBJ.jp2')
                line = 'OBJ.jp2'
            shutil.move(line, subdir)
    filelist = [os.path.abspath(i) for i in os.listdir()]
    for line in filelist:
        #move the parent metadata into the appropriate folder
        if '.xml' in line:
            place = '{}/'.format(line[:-4])
            os.rename(line, 'MODS.xml')
            shutil.move('MODS.xml', place)
 

organize_cpd_structure()