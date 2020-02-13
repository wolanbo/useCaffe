#include "classifier.h"

int main(int argc, char** argv) {
	/*if (argc != 6) {
		std::cerr << "Usage: " << argv[0]
		<< " deploy.prototxt network.caffemodel"
		<< " mean.binaryproto labels.txt img.jpg" << std::endl;
		return 1;
	}*/

	//::google::InitGoogleLogging(argv[0]);

	string model_file   = "/home/lan/桌面/useCaffe/myModel/MiniNet_Test.protxt";
	string trained_file = "/home/lan/桌面/useCaffe/myModel/MiniNet_iter_20000.caffemodel";
	string mean_file    = "/home/lan/桌面/useCaffe/myModel/train_data_means.binaryproto";
	string label_file   = "/home/lan/桌面/useCaffe/myModel/labels.txt";

	Classifier classifier(model_file, trained_file, mean_file, label_file);

	string file = "/home/lan/桌面/use-caffe/myModel/img.bmp";

	std::cout << "---------- Prediction for " << file << " ----------" << std::endl;

	cv::Mat img = cv::imread(file, -1);
	CHECK(!img.empty()) << "Unable to decode image " << file;
	std::vector<Prediction> predictions = classifier.Classify(img);

	/* Print the top N predictions. */
	for (size_t i = 0; i < predictions.size(); ++i) {
		Prediction p = predictions[i];
		std::cout << std::fixed << std::setprecision(4)
			  << p.second << " - \"" << p.first << "\"" << std::endl;
	}
}

