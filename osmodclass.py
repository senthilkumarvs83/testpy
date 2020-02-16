import os, random, string

currpath = 'C:\\Senthil\\testdirs'
newdir= 'MyFolder'
newpath = os.path.join(currpath, newdir)
def makeDirectory():
    # newpath = os.path.join(currpath, newdir)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        print('Directory created')
    elif os.path.exists(newpath):
        print('directory exists!')

def fillFile(filehandle):
    if filehandle.closed:
        print('File handle is no longer open !!!')
        return

    filehandle.write(''.join(random.choice(string.ascii_letters) + str(i) for i in range(500)))
    filehandle.flush()
    
def createFiles():
    # newpath = os.path.join(currpath, newdir)
    if not os.path.exists(newpath):
        print('Path does not exist, aborting...')
        return
    else:
        os.chdir(newpath)
    
    for filename in range(0,10):
        filehandle = open(newpath + 'filename' + str(filename) + '.txt', 'w')
        fillFile(filehandle)
        filehandle.flush()
        filehandle.close()
    print('10 files created in the mentioned directory!')
    
def walkDirs(currpath):
    
    print("Going to walk "), currpath
    os.chdir(currpath)
    print('Now in directory')
    for root,dirs,files in os.walk(currpath, topdown=True): 
        print(root)
        print(dirs) 
        print(files) 


# makeDirectory()
createFiles()
# walkDirs(newpath)

