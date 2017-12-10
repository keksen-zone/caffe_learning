
echo "欢迎~"
echo "在此部分中将会对图片进行重命名，并将面部提取出来"
echo "请将待分类图片放入pics文件夹中"

echo "正在重命名"
python /Users/shenxudong/Desktop/tmp/rename.py
echo "完成对文件的重命名操作"
echo "正在进行面部提取"
python /Users/shenxudong/Desktop/tmp/face_detect.py

echo "已完成当前操作，提取的面部图象位于faces文件夹中"
echo "未检测到面部的图象位于not_detected文件夹中，这些图象最后需要手动进行分类"
echo "进行下一步操作之前，需要手动对部分样本进行分类"