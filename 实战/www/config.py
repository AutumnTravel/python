#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Configuration
'''

__author__ = 'Michael Liao'

import config_default#����Ĭ������

class Dict(dict):#�����Ӧ�����Ǻܳ����ˣ����ǰ�dict��ӹ�һ�£�ʹ���µ�Dict�ഴ����ʵ��������x.y�ķ�ʽ��ȡֵ�͸�ֵ
    '''
    Simple dict but support access as x.y style.
    '''
    def __init__(self, names=(), values=(), **kw):#�����������ʼ������
        super(Dict, self).__init__(**kw)#�ȵ��ø���ĳ�ʼ�������洢��ֵ��
        for k, v in zip(names, values):#Ȼ���Լ�����forѭ�������洢��ֵ�ԣ�why?
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

def merge(defaults, override):#�ں�Ĭ�����ú��Զ�������
    r = {}
    for k, v in defaults.items():
        if k in override:
            if isinstance(v, dict):
                r[k] = merge(v, override[k])
            else:
                r[k] = override[k]
        else:
            r[k] = v
    return r

def toDict(d):#��d���dict�ļ�ֵ�Դ��������Զ����Dict�У�Ȼ�󷵻�һ���µ�DictҲ����D
    D = Dict()
    for k, v in d.items():#��forѭ������d�ļ�ֵ�ԣ�Ȼ�����Щ��ֵ�Դ����µ�Dict
        D[k] = toDict(v) if isinstance(v, dict) else v#����ֵ�������һ��dict���ǾͰ����ֵ����toDict����Ȼ���ٴ���Dict
    return D#�������ɵ���Dict

configs = config_default.configs

try:
    import config_override#�����Զ�������
    configs = merge(configs, config_override.configs)#�ں�Ĭ�����ú��Զ�������
except ImportError:#�����Զ�������ʧ�ܾ�ֱ��pass
    pass

configs = toDict(configs)#���ںϺ�����ý���toDict��������