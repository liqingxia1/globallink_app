import os, time


def clearlog():
    print(">>>>>>>>>>  【执行测试前，日志清除】  <<<<<<<<<<")
    cmd_c = 'adb logcat -c'
    os.popen(cmd_c)
    time.sleep(5)
    os.system("adb kill-server")

def getlog():
    time.sleep(2)
    print(">>>>>>>>>>  【执行测试后，日志打印】  <<<<<<<<<<")
    try:
        path = os.path.dirname(os.getcwd())
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))  # 获取当前时间
        log = os.path.join(path, 'case\log\\' + now + r"log.txt")  # 日志文件名添加当前时间
        logcmd = "adb logcat -d | findstr  RUIMD>"+ log
        os.system(logcmd)

        ruquim = os.path.join(path, 'case\log\\ruquimLog.txt')
        os.system("adb logcat -d | findstr ServerReqUimResponse >"+ruquim)
        time.sleep(3)
    except:
        pass
    os.system("adb kill-server")
