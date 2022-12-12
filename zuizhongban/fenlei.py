#coding=utf-8 
       
import os
import sys
import shutil

root='/Users/sakurakouji/Desktop/tmp/'
caffe_root='/Users/sakurakouji/Desktop/workspace/caffe/'
sys.path.insert(0,caffe_root+'python')
import caffe
os.chdir(root)
 
import numpy as np 
 
net_file=root + 'deploy.prototxt'   
caffe_model=root + 'test_iter_500.caffemodel'  
mean_file=root + 'mean.npy'

dir = root+'faces/'
dir_org = root+'pics/'

filelist=[]
filenames = os.listdir(dir)
for fn in filenames:
    filelist.append(fn)
#   fullfilename = os.path.join(dir,fn)
#   filelist.append(fullfilename)
 

def Test(dir,img):
    img_org=img
    net = caffe.Net(net_file,caffe_model,caffe.TEST)   
    img=dir+img   
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})  
    transformer.set_transpose('data', (2,0,1))    
    transformer.set_mean('data', np.load(mean_file).mean(1).mean(1))    
    transformer.set_raw_scale('data', 255)    
    transformer.set_channel_swap('data', (2,1,0))   
       
    im=caffe.io.load_image(img)               
    net.blobs['data'].data[...] = transformer.preprocess('data',im)      
       
 
    out = net.forward() 
       
    labels = np.loadtxt(labels_filename, str, delimiter='\t')  
    prob= net.blobs['prob'].data[0].flatten() 
    print prob 
    order=prob.argsort()[-1]  
    print 'the class is:',labels[order]   
#    f=file("/Users/sakurakouji/Desktop/workspace/caffe/examples/lovelive/gailv.txt","a+")
#    f.writelines(img+' '+labels[order]+'\n')

    #shutil.move(img,root+'classify/'+labels[order]+'/')
    shutil.move(dir_org+img_org,root+'classify/'+labels[order]+'/')
 
labels_filename = root +'words.txt'    
 
for i in range(0, len(filelist)):
    img= filelist[i]
    Test(dir,img)
