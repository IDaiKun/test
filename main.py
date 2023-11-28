import os
import re
import shutil


def copy_file(src, dst):
    shutil.copy(src, dst)

def main():
    input1 = input("源文件地址(需要写最后的文件名)：")
    out1 = input("移动到的地址(不需要写最后的文件名)：")

    sourseFileRoute = input1
    sink1FileRoute = out1

    if not os.path.exists(sink1FileRoute):
        os.mkdir(sink1FileRoute)
    sinkFileRoute = os.path.join(sink1FileRoute, os.path.basename(sourseFileRoute))


    try:
        copy_file(sourseFileRoute, sinkFileRoute)
        print("文件复制成功")
    except Exception as e:
        print("异常")

if __name__ == "__main__":
    main()
