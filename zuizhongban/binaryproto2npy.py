#coding=utf-8
import numpy as np
import sys
import os


caffe_root='/Users/sakurakouji/Desktop/workspace/caffe/'
sys.path.insert(0,caffe_root+'python')
import caffe
os.chdir(caffe_root)

MEAN_PROTO_PATH = '/Users/sakurakouji/Desktop/tmp/mean.binaryproto'
MEAN_NPY_PATH = '/Users/sakurakouji/Desktop/tmp/mean.npy'

blob = caffe.proto.caffe_pb2.BlobProto()       
data = open(MEAN_PROTO_PATH, 'rb' ).read()      
blob.ParseFromString(data)                    

array = np.array(caffe.io.blobproto_to_array(blob))
mean_npy = array[0]
np.save(MEAN_NPY_PATH ,mean_npy)
