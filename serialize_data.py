# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: serialize_data.py
# @Author: myloe
# @Time: Jan 11, 2021
# ---

import inspect
import pickle as p

def dumps_data(file,space):
    """
    将数据序列化至文件
    @param file: 文件
    @param space: 写入空间 locals()
    @return:
    """
    tmp_vars = {}
    tmp_vars.update(space)
    serialize_vars = dict()
    for var in tmp_vars.keys():
        if not var.startswith("_") and not inspect.ismodule(tmp_vars[var]) and var != 'tmp_vars' and not inspect.isfunction(tmp_vars[var]):
            try:
                p.dumps(tmp_vars[var])
                serialize_vars.update({var: tmp_vars[var]})
            except Exception as e:
                serialize_vars.update({var: f'变量{var}未成功序列化'})
    with open(file, "wb+") as f:
        x = p.dumps(serialize_vars)
        f.write(x)

def loads_data(file,space):
    """
    将序列化的数据写入到指定文件
    @param file: 待写入的文件
    @param space: 写入空间 locals()
    @return:
    """
    with open(file, "rb+") as f:
        res = p.load(f)
        for key in res:
            space[key] = res[key]


用法：            
1. 把文件放在路径下  
2. 
import serialize_data as f
f.dumps_data(dataframe,path)

import serilize_data as f
f.loads_data(dataframe,path)

