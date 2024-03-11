import sys
import time


def progress_bar():
    for i in range(1,101):
        print("\r",end="")
        # 将每个变数的数字转换成对应的进度条
        print("Download progress:{}%".format(i),"▋"*(i//2),end="")
        sys.stdout.flush()
        time.sleep(0.05) 

if __name__ == '__main__':
    print("-------祈祷代码不报错--------\n")
    progress_bar()