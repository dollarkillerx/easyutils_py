'''
encryption 加密解密 相关常用工具
'''
# md5加密
import hashlib


def md5_encode(str):
    seed = hashlib.md5()
    str = str.encode(encoding="utf-8")
    seed.update(str)
    return seed.hexdigest()