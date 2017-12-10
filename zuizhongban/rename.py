import os

def rename():
    path='/Users/shenxudong/Desktop/tmp/pics';
    filelist=os.listdir(path)
#    print filelist
    count=0;
    for files in filelist:
        Olddir=os.path.join(path,files);
        filename=os.path.splitext(files)[0];
        filetype=os.path.splitext(files)[1];
        Newdir=os.path.join(path,"test"+str(count)+filetype);
#        Newdir=os.path.join(path,"test"+str(count)+filetype);
        os.rename(Olddir,Newdir);
        count+=1;

rename();