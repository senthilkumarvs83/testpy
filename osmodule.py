import os
import shutil
import string
import random


def CreateDir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)
        
def FillFile(filehandle):
    if filehandle.closed:
        print('File handle is no longer open !!!')
        return

    filehandle.write(''.join(random.choice(string.ascii_letters) + str(i) for i in range(5000)))
    filehandle.flush()
        
    
def CreateFiles(dirname):
    
    if not os.path.exists(dirname):
        print('Path does not exist, aborting...')
        return
    else:
        os.chdir(dirname)
    
    for filename in range(0,10):
        filehandle = open(dirname + 'filename' + str(filename) + '.txt', 'w')
        FillFile(filehandle)
        filehandle.flush()
        filehandle.close()

def CreateDirLevels(dirname_to_go_into, level = 3):
    
    if os.path.exists(os.path.dirname(dirname_to_go_into)):
        os.makedirs(dirname_to_go_into)
        os.chdir(dirname_to_go_into)
    
    dirname = "level"
    '''filename = "file"'''
    
    for dirlevel in range(0,level):
        createdir = dirname + str(dirlevel)
        '''createfile = filename + str(dirlevel)'''
        os.chdir(dirname_to_go_into)
        CreateDir(createdir)
        CreateFiles(createdir)
        
    WalkDirLevels(dirname_to_go_into)
        
def WalkDirLevels(dirname):
    
    print("Going to walk "), dirname
    
    os.chdir(dirname)
    
    for _, dirs, _ in os.walk(dirname, topdown=True):
        if len(dirs) != 0:
            for pickdir in dirs:
                print(pickdir)
                print(len(pickdir)*' '+'|')
                for _, _, files in os.walk(pickdir, topdown=True):
                    if len(files) != 0:
                        for pickfile in files:
                            print(len(pickdir)*' '+ 5*'_' + pickfile)
            
            
        
def main():

    dirname = "C:\Senthil\testdirs"
    
    if os.path.exists(dirname):
        shutil.rmtree(dirname, ignore_errors=True)

    CreateDirLevels(dirname, 20)
    

if __name__ == '__main__':
    main()