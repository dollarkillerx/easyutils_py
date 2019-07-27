# easyutils_py
python3 easyutils 

### 简介
Python3 常用工具库 提高生产力

骐骥千里,非一日之功  慢慢丰富这个库

``` 
.
├── LICENSE
├── README.md
├── encryption.py # 加密解密相关
└── file.py  # 文件操作相关
``` 

## 文件操作

## 加密解密
- md5 编码
    `str = md5_encode(str)`
- 获取文件后缀
    `postfix = get_postfix(str)`
- 获取文件随机文件名称
    `new_rand_name = get_rand_file(postfix)`
- 文件拷贝
    `file_copy(oldPath,newPath)`
- 获取文件 上的序号
    `num = file_get_num(str)`
- 创建目录 (如果不存在则会创建)
    `file_mkdir(path)`
    