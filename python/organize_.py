import os, shutil


#add exception for '-3', '_Envelope' 
# I'm using some lazy directory creating methods. I think I should keep it to the current folder.

#If I'm using underscores to split strings and create directories, I need to not use them in my nameing convention

output_dir = 'output'
os.mkdirs(output, exist_ok=True)

def organize_cpd_structure():
    filelist = [os.path.abspath(i) for i in os.listdir()]
    print(filelist)
    for line in filelist:
        if '_' not in line:
            #print('{}'.format(line))

            filename, ext = os.path.splitext(line)
            os.makedirs(filename, exist_ok=True)
    for line in filelist:
        #print(line)
        if ('_0') in line:
            directory = line.split('_')
            objdir = '{}/'.format(directory[0])
            print(objdir)
            subfolder = directory[1]
            subfolder = subfolder.split('.')
            subdir = objdir + subfolder[0]
            print(subdir)
            os.makedirs(subdir, exist_ok=True)
    for line in filelist:
        if '_0' in line:
            directory = line.split('_')
            objdir = '{}/'.format(directory[0])
            subfolder = directory[1]
            subfolder = subfolder.split('.')
            subdir = objdir + subfolder[0]
            if '.xml' in line:
                os.rename(line, 'MODS.xml')
                line = 'MODS.xml'
            if '.jp2' in line:
                os.rename(line, 'OBJ.jp2')
                line = 'OBJ.jp2'
            shutil.move(line, subdir)
    filelist = [os.path.abspath(i) for i in os.listdir()]
    for line in filelist:
        if '.xml' in line:
            place = '{}/'.format(line[:-4])
            os.rename(line, 'MODS.xml')
            shuti.move('MODS.xml', place)
 

organize_cpd_structure()