#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/3/30 9:54
# @Author: Jtyoui@qq.com
import os
from pyunit_string import Strings


def add_test():
    """测试字符串增加int类型"""
    s = Strings('b')
    s += 1 + 1j
    s += 1
    s += 'a'
    upper = s.upper()
    print(upper, type(upper))


def join_test():
    s = Strings('#')
    b = s.join([1, 2, 3, 4])
    print(b, type(b))


def json_dump_test():
    ds = ['伟']
    s = Strings(json_=ds)
    b = s.json_dump(file='./json.json', ensure_ascii=False)
    print(b)


def json_load_test():
    ds = '["伟"]'
    s = Strings(json_=ds)
    b = s.json_load(encoding='utf-8')
    print(b, type(b))

    print('---------------------------------')

    s = Strings()
    c = s.json_load(file='./json.json')
    print(c, type(c))
    os.remove('./json.json')


def replace_test():
    import re
    s = Strings('#$ba$#')
    b = s.replace('[#$A]', '', flags=re.I)
    print(b, type(b))


def length_test():
    s = Strings('acb')
    print(s.length())


def find_test():
    s = Strings('aaa')
    ls = s.find('a')
    print(ls)


if __name__ == '__main__':
    add_test()
    join_test()
    json_dump_test()
    json_load_test()
    replace_test()
    length_test()
    find_test()
