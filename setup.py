import os

#builds into the same directory as the setup file
path = os.path.realpath(__file__+r"/..")

def build():
    if os.path.exists(path+"/albatrostools.c"):
        os.system("gcc-9 -O3 -o \""+ path + "/libalbatrostools.so\" -fPIC --shared \"" + path + "/albatrostools.c\" -fopenmp")
    else:
        print("Cannot find the file albatrostools.c in the directory "+path)
    
def install():
    #os.environ["LD_LIBRARY_PATH"] = os.environ["LD_LIBRARY_PATH"]+":"+path #this gives an error since it can't access LD_LIBRARY_PATH
    #os.system("echo $LD_LIBRARY_PATH")
    if os.path.exists(path+"/albatrostools.py"):
        import albatrostools #this also doesn't do what I want it to. It only imports for this file.
    else:
        print("Cannot find file albatrostools.py in the directory "+path)