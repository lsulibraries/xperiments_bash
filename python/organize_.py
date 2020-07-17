import os, shutil



def organize_cpd_structure():
    filelist = [os.path.abspath(i) for i in os.listdir()]
    for line in filelist:
        if '_' not in line:
            print('{}'.format(line))

            filename, ext = os.path.splitext(line)
            print('cpd file : {}'.format(filename))
            os.makedirs(filename, exist_ok=True)
    for line in filelist:
        if '_0' in line:
            directory = line.split('_')
            shutil.move(line, '{}/'.format(directory[0]))
    filelist = [os.path.abspath(i) for i in os.listdir()]
    for line in filelist:
        if '.xml' in line:
            shutil.move(line, '{}/'.format(line[:-4]))
 

organize_cpd_structure()