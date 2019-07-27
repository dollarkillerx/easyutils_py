'''
File 常用工具
'''
# 获取文件后缀
import os
import random
import re
import shutil
import time

from encryption import md5_encode

# 获取文件后缀
def get_postfix(str):
    try:
        id = str.index('.')
        return str[id:]
    except:
        print(str)
        exit()


# 获取随机文件名称
def get_rand_file(postfix):
    t = time.time()
    nowTime = lambda: int(round(t * 1000))
    rand = random.random()
    tim = nowTime()
    sd = str(tim) + str(rand)
    name = md5_encode(sd)
    return name + postfix


# 文件拷贝
def file_copy(oldPath, newPath):
    shutil.copy(oldPath, newPath)


# cartoon 定制r
# 获取数字 去掉0
def file_get_num(str):
    try:
        # 获取数字
        num = re.findall('(\d+)', str)
        if len(num) == 0:
            return
        # 去掉0
        return num[0].replace('0', '')
    except:
        print(num)
        print(str)
        return


# 创建目录
def file_mkdir(path):
    # 如果文件不存在则创建文件
    if not os.path.exists(path):
        os.makedirs(path)