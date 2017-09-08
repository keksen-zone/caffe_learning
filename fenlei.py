#coding=utf-8 
       
import os
import sys

root='/home/sakurakouji/文档/caffe/'
sys.path.insert(0,root+'python')
import caffe
os.chdir(root)
 
import numpy as np 
 
net_file=root + 'examples/lovelive/deploy.prototxt'    #deploy文件 
caffe_model=root + 'examples/lovelive/test_iter_400.caffemodel'  #训练好的 caffemodel 
mean_file=root + 'examples/lovelive/mean.npy'


dir = root+'examples/lovelive/train/Kotori/'
filelist=[]
filenames = os.listdir(dir)
for fn in filenames:
   fullfilename = os.path.join(dir,fn)
   filelist.append(fullfilename)
 
 
# img=root+'data/DRIVE/test/60337.jpg'   #随机找的一张待测图片 
 
def Test(img):
      
    net = caffe.Net(net_file,caffe_model,caffe.TEST)   #加载model和network 
       
    #图片预处理设置 
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})  #设定图片的shape格式(1,3,28,28) 
    transformer.set_transpose('data', (2,0,1))    #改变维度的顺序，由原始图片(28,28,3)变为(3,28,28) 
    transformer.set_mean('data', np.load(mean_file).mean(1).mean(1))    #减去均值，前面训练模型时没有减均值，这儿就不用 
    transformer.set_raw_scale('data', 255)    # 缩放到【0，255】之间 
    transformer.set_channel_swap('data', (2,1,0))   #交换通道，将图片由RGB变为BGR 
       
    im=caffe.io.load_image(img)                   #加载图片 
    net.blobs['data'].data[...] = transformer.preprocess('data',im)      #执行上面设置的图片预处理操作，并将图片载入到blob中 
       
    #执行测试 
    out = net.forward() 
       
    labels = np.loadtxt(labels_filename, str, delimiter='\t')   #读取类别名称文件 
    prob= net.blobs['prob'].data[0].flatten() #取出最后一层（prob）属于某个类别的概率值，并打印,'prob'为最后一层的名称
    print prob 
    order=prob.argsort()[-1]  #将概率值排序，取出最大值所在的序号 ,9指的是分为0-9十类 
    #argsort()函数是从小到大排列 
    print 'the class is:',labels[order]   #将该序号转换成对应的类别名称，并打印 
    f=file("/home/sakurakouji/文档/caffe/examples/lovelive/gailv.txt","a+")
    f.writelines(img+' '+labels[order]+'\n')
 
labels_filename = root +'examples/lovelive/words.txt'    #类别名称文件，将数字标签转换回类别名称 
 
for i in range(0, len(filelist)):
    img= filelist[i]
    Test(img)
