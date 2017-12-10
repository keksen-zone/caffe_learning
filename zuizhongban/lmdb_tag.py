import os  
  
def IsSubString(SubStrList,Str):  
    flag=True  
    for substr in SubStrList:  
        if not(substr in Str):  
            flag=False  
      
    return flag  
  

def GetFileList(FindPath,FlagStr=[]):  
    FileList=[]  
    FileNames=os.listdir(FindPath)  
    if len(FileNames)>0:  
        for fn in FileNames:  
            if len(FlagStr)>0:  
                if IsSubString(FlagStr,fn):  
                    fullfilename=os.path.join(FindPath,fn)  
                    FileList.append(fullfilename)  
            else:  
                fullfilename=os.path.join(FindPath,fn)  
                FileList.append(fullfilename)  
      
    if len(FileList)>0:  
        FileList.sort()  
          
    return FileList  
  
  
  
train_txt=open('train.txt','w')  

imgfile=GetFileList('train/Eli')
for img in imgfile:  
    str1=img+' '+'0'+'\n'       
    train_txt.writelines(str1)  
      
  
imgfile=GetFileList('train/Hanayo')  
for img in imgfile:  
    str2=img+' '+'1'+'\n'  
    train_txt.writelines(str2)  
 
  
imgfile=GetFileList('train/Honoka')  
for img in imgfile:  
    str3=img+' '+'2'+'\n'  
    train_txt.writelines(str3)  

imgfile=GetFileList('train/Kotori')
for img in imgfile:  
    str4=img+' '+'3'+'\n'       
    train_txt.writelines(str4)  
      
  
imgfile=GetFileList('train/Maki')  
for img in imgfile:  
    str5=img+' '+'4'+'\n'  
    train_txt.writelines(str5)  
 
  
imgfile=GetFileList('train/Nico')  
for img in imgfile:  
    str6=img+' '+'5'+'\n'  
    train_txt.writelines(str6)  

imgfile=GetFileList('train/Nozomi')
for img in imgfile:  
    str7=img+' '+'6'+'\n'       
    train_txt.writelines(str7)  
      
  
imgfile=GetFileList('train/Rin')  
for img in imgfile:  
    str8=img+' '+'7'+'\n'  
    train_txt.writelines(str8)  
 
  
imgfile=GetFileList('train/Umi')  
for img in imgfile:  
    str9=img+' '+'8'+'\n'  
    train_txt.writelines(str9)  
train_txt.close()  
  
  

test_txt=open('val.txt','w')  

imgfile=GetFileList('val/Eli')
for img in imgfile:  
    str11=img+' '+'0'+'\n'  
    test_txt.writelines(str11)  
      
  
imgfile=GetFileList('val/Hanayo')  
for img in imgfile:  
    str22=img+' '+'1'+'\n'  
    test_txt.writelines(str22)  
 
  
imgfile=GetFileList('val/Honoka')  
for img in imgfile:  
    str33=img+' '+'2'+'\n'  
    test_txt.writelines(str33)  

imgfile=GetFileList('val/Kotori')
for img in imgfile:  
    str44=img+' '+'3'+'\n'  
    test_txt.writelines(str44)  
      
  
imgfile=GetFileList('val/Maki')  
for img in imgfile:  
    str55=img+' '+'4'+'\n'  
    test_txt.writelines(str55)  
 
  
imgfile=GetFileList('val/Nico')  
for img in imgfile:  
    str66=img+' '+'5'+'\n'  
    test_txt.writelines(str66)  

imgfile=GetFileList('val/Nozomi')
for img in imgfile:  
    str77=img+' '+'6'+'\n'  
    test_txt.writelines(str77)  
      
  
imgfile=GetFileList('val/Rin')  
for img in imgfile:  
    str88=img+' '+'7'+'\n'  
    test_txt.writelines(str88)  
 
  
imgfile=GetFileList('val/Umi')  
for img in imgfile:  
    str99=img+' '+'8'+'\n'  
    test_txt.writelines(str99)  
test_txt.close()  
  
print("succeed")
