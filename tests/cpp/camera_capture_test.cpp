#include <opencv2/opencv.hpp>
using namespace cv;
using namespace std;

int main()
{
	VideoCapture capture(0);
	int fps = capture.get(CV_CAP_PROP_FPS);
	int width = capture.get(CV_CAP_PROP_FRAME_WIDTH);
	int height = capture.get(CV_CAP_PROP_FRAME_HEIGHT);
	printf("INFO: camera current fps=%d, width=%d, height=%d\n", fps, width, height);

	capture.set(CV_CAP_PROP_FPS, 19);

	while (true)
	{
		Mat frame;
		capture >> frame;
		imshow("frame", frame);
		waitKey(100); //延时30
	}
	return 0;
}
