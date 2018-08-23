from datetime import datetime
import os
import time

local_date = time.strftime(r"%Y-%m-%d", time.localtime())

def driverPath():
	return r"D:\software\chromedriver2.40\chromedriver.exe"

def baseUrl():
	return "http://yan.eeseetech.cn/admin/main"

def username():
	return "ttt@qq.com"

def password():
	return "eeseetech"

def storekeeperName():
	return "测试上海店铺"

def detailAddress():
	return "1108弄"

def storeName():
	return "测试店铺"

def remoteUrl():
	return "http://localhost:4723/wd/hub"

def webviewContext():
	return "WEBVIEW_com.tencent.mm:tools"

def nativeContext():
	return "NATIVE_APP"

def shopkeeperIphone():
	return "17317460712"

def verificationCode():
	return "123456"

def customerName():
	return "测试上海客户"

def customerIphone():
	return "18721987875"

def salerName():
	return "测试上海访销"

def belongCompany():
	return "上海意视"

def salerIphone():
	return "18721987875"

def getCurrentTime():
	format = "%Y-%m-%d %H:%M:%S"
	return datetime.now().strftime(format)

#Get time diff
def timeDiff(starttime,endtime):
	format = "%Y-%m-%d %H:%M:%S"
	return datetime.strptime(endtime,format) - datetime.strptime(starttime,format)

def folderPath():
	folder_path = '%s/results/%s' % (
		os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))),
		local_date)
	return folder_path

def picturePath():
	pic_folder = folderPath() + '/pictures/'
	if os.path.exists(pic_folder):
		print('The picture folder has already existed')
	else:
		os.makedirs(pic_folder)
	local_time = time.strftime('%Y%m%d%H%M%S')
	pic_path = pic_folder + local_time + ".png"
	return pic_path