# ~*~ coding:utf-8
# 版本说明：1.0
# 功能说明：{封装默认文件路径}
import os
class Config_File(object):
    base_file=os.path.dirname(__file__)
    data_file=base_file+r"\Data"
    getcase_file=base_file+"\GetCase"

if __name__ == '__main__':
    c=Config_File()
    print(c.data_file)