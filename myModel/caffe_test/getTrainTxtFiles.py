import os

def mk_train_txt_file(imgDirPath, txtFilePath):
	fileNames = os.listdir(imgDirPath)
	with open(txtFilePath, "w") as f:
		for fileName in fileNames:
			if (fileName.split("_")[0] == "10194" and fileName.split(".")[-1] == "bmp"):
				label = "0"
				f.write(fileName + " " + label + "\n")
			elif (fileName.split("_")[0] == "10195" and fileName.split(".")[-1] == "bmp"):
				label = "1"
				f.write(fileName + " " + label + "\n")
			elif (fileName.split("_")[0] == "10196" and fileName.split(".")[-1] == "bmp"):
				label = "2"
				f.write(fileName + " " + label + "\n")
			elif (fileName.split("_")[0] == "10197" and fileName.split(".")[-1] == "bmp"):
				label = "3"
				f.write(fileName + " " + label + "\n")
			elif (fileName.split("_")[0] == "10198" and fileName.split(".")[-1] == "bmp"):
				label = "4"
				f.write(fileName + " " + label + "\n")
			elif (fileName.split("_")[0] == "10199" and fileName.split(".")[-1] == "bmp"):
				label = "5"
				f.write(fileName + " " + label + "\n")
	f.close()


if __name__ == "__main__":
	imgDirPath = "/data/lanhaibo/caffe_test/trian_data_dir"
	txtFilePath = "/data/lanhaibo/caffe_test/train_label.txt"
	mk_train_txt_file(imgDirPath, txtFilePath)

	imgDirPath = "/data/lanhaibo/caffe_test/test_data_dir"
	txtFilePath = "/data/lanhaibo/caffe_test/test_label.txt"
	mk_train_txt_file(imgDirPath, txtFilePath)
