# coding=utf-8
import os
import time

today = time.strftime("%Y-%m-%d",time.localtime(time.time()))
print today
path = "/Users/qian_ying/Downloads/"
cmd_android = "grep '\"passRate\":0' "+str(path)+"testAndroid1111.log >  "+str(path)+"android_fail_"+str(today)+".log"
cmd_iOS = "grep '\"passRate\":0' "+str(path)+"testiOS1111.log >  "+str(path)+"iOS_fail_"+str(today)+".log"
print cmd_android
print cmd_iOS
os.system(cmd_android)
os.system(cmd_iOS)