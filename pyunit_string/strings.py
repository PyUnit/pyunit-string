#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/3/30 9:52
# @Author: Jtyoui@qq.com
# @site: 对字符串模块进行加强封装
import numbers
import json
import re


class Strings:

    def __init__(self, value: str = '', **kwargs):
        """
        kwargs 参数包括：
            - json_ :将字符串类型转为json格式
            - file  : 文件路径
        """
        self._kwargs = kwargs
        self.value = value

    @staticmethod
    def _change_str(other):
        if isinstance(other, numbers.Real):
            other = str(other)
        elif isinstance(other, numbers.Complex):
            other = str(other)
            if '(' in other:
                other = other[1:-1]
        return other

    def __add__(self, other):
        other = self._change_str(other)
        obj = self.value + other
        return Strings(obj)

    def __iadd__(self, other):
        """加强+=模式，增加数字类型"""
        other = self._change_str(other)
        self.value += other
        return self

    def join(self, iterable):
        """增加数字类型"""
        iterable = map(lambda x: str(x), iterable)
        self.value = self.value.join(iterable)
        return self

    def upper(self):
        self.value = self.value.upper()
        return self

    def json_dump(self, json_=None, file=None, **kwargs):
        """获取json格式

        :param json_: 需要转为json格式的数据
        :param file: 需要保存json数据的文件路径
        :param kwargs: 其余参数
        :return: json格式
        """
        json_ = json_ or self._kwargs.get('json_', {})
        file = file or self._kwargs.get('file')
        if file is not None:
            with open(file, mode='w', encoding='utf-8') as fp:
                obj = json.dump(json_, fp, **kwargs)
        else:
            obj = json.dumps(json_, **kwargs)
        return obj

    def json_load(self, json_=None, file=None, **kwargs):
        """加载json格式

        :param json_: 加载json格式的数据
        :param file: 需要加载json数据的文件路径
        :param kwargs: 其余参数
        :return: json格式
        """
        json_ = json_ or self._kwargs.get('json_', {})
        file = file or self._kwargs.get('file')
        if file is not None:
            with open(file, mode='r', encoding='utf-8') as fp:
                obj = json.load(fp, **kwargs)
        else:
            obj = json.loads(json_, **kwargs)
        return obj

    def __str__(self):
        return self.value

    def replace(self, old: str, new: str, count: int = 0, **kwargs):
        """正则替换"""
        obj = re.sub(old, new, self.value, count=count, **kwargs)
        return Strings(obj)

    def length(self):
        return len(self.value)

    def find(self, sub, start=0, end=None) -> list:
        """找到sub所有的索引，返回是所有索引的集合"""
        end = end or self.length()
        ls = []
        while start <= end:
            index = self.value.find(sub, start, end)
            if index > -1:
                ls.append(index)
                start = index + 1
            else:
                break
        return ls
