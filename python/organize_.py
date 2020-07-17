import os, shutil



def organize_cpd_structure():
    filelist = [os.path.abspath(i) for i in os.listdir()]
    for line in filelist:
        if '_' not in line:
            print('{}'.format(line))

            filename, ext = os.path.splitext(line)
            os.makedirs(filename, exist_ok=True)
    for line in filelist:
        if '_0' in line:
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
                os.rename(line, 'OBJ.xml')
                line = 'OBJ.xml'
            shutil.move(line, subdir)
    filelist = [os.path.abspath(i) for i in os.listdir()]
    for line in filelist:
        if '.xml' in line:
            place = '{}/'.format(line[:-4])
            os.rename(line, 'MODS.xml')
            shutil.move('MODS.xml', place)
 

organize_cpd_structure()