#include <iostream>
#include <sstream>
#include <io.h>
#include <Windows.h>
#include "opencv2/opencv.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
using namespace cv;
using namespace std;
int main(void)
{
	for (int i = 0; i <= 126; i++)
	{
		//string test1 = "test";
		string test2 = ".jpg";
		string testtmp;
		stringstream ss;
		ss << i;
		ss >> testtmp;
		string test3 = testtmp + test2;
		//cout << test3 << endl;

		string a = test3;
		vector<Rect> face;
		Mat src, dst, tmp;
		CascadeClassifier cascade;
		cascade.load("lbpcascade_animeface.xml");
		if (!cascade.load("lbpcascade_animeface.xml")) { cout << "--(!)Error loading face cascade\n"; cin.get(); return -1; };

		src = imread("./lovelive/Umi/" + testtmp + ".jpg");
		cvtColor(src, tmp, COLOR_BGR2GRAY);
		equalizeHist(tmp, tmp);
		cascade.detectMultiScale(tmp, face, 1.1, 2, 0 | CASCADE_SCALE_IMAGE, Size(30, 30));

		for (vector<Rect>::const_iterator iter = face.begin(); iter != face.end(); iter++)
		{
			rectangle(tmp, *iter, Scalar(0, 0, 255), 2, 8);
		}
		for (size_t i = 0; i < face.size(); i++)
		{
			Point rec(face[i].x, face[i].y);
			Point rec2(face[i].x + face[i].width, face[i].y + face[i].height);
			Mat face_img = src(Range(face[i].y, face[i].y + face[i].height), Range(face[i].x, face[i].x + face[i].width));
			//imwrite("./3/" + a, face_img);
			Mat xiangao, tmp;
			//face_img = imread("lun06b.bmp");
			xiangao.create(face_img.size(), face_img.type());
			tmp = face_img;

			//cvtColor(tmp, xiangao, COLOR_BGR2GRAY);
		//	blur(xiangao, xiangao, Size(3, 3));
			//Canny(xiangao, xiangao, 3, 9, 3);

			//imshow("window", xiangao);
			imwrite("./ll/Umi/" + a, face_img);
		}
		//imshow("window", tmp);
	}
	waitKey(0);
	return 0;
}