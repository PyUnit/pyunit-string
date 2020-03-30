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
    s = s + 9.9
    print(s, type(s))

    print('---------------------')
    s = Strings('b')
    b = s + [1, 2, 3]
    print(b, type(b), s)

    print('---------------------')
    s = Strings('b')
    s += [1, 2, 3, 4]
    print(s, type(s))


def join_test():
    s = Strings('#')
    b = s.join([1, 2, 3, 4j, 3.2])
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


def mul_test():
    s = Strings('abc')
    b = s * (1, 2, 4)
    print(b, type(b))

    print('-----------------')
    s = Strings('张三爱李四,王老五爱张三')
    c = s * {'张三': 3, '李四': 2, '讨厌': 2}
    print(c, type(c))


if __name__ == '__main__':
    add_test()
    join_test()
    json_dump_test()
    json_load_test()
    replace_test()
    length_test()
    find_test()
    mul_test()
