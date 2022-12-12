
echo "欢迎!"

echo "正在制作标签集"
python /Users/sakurakouji/Desktop/tmp/lmdb_tag.py
echo "正在制作数据集"
sh /Users/sakurakouji/Desktop/tmp/create_imagenet.sh
echo "正在计算均值文件"
 /Users/sakurakouji/Desktop/workspace/caffe/build/tools/compute_image_mean /Users/sakurakouji/Desktop/tmp/ilsvrc12_train_lmdb /Users/sakurakouji/Desktop/tmp/mean.binaryproto
echo "正在转换均值文件为指定格式,这将在后续步骤中用到"
python /Users/sakurakouji/Desktop/tmp/binaryproto2npy.py
echo "已完成，将在20秒后开始训练。过程视数据集大小可能耗时较长，请耐心等待"

sleep 20

sudo /Users/sakurakouji/Desktop/workspace/caffe/build/tools/caffe train -solver /Users/sakurakouji/Desktop/tmp/solver.prototxt

echo "训练完成"
