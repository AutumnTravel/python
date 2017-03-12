#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Models for user, blog, comment.
'''

__author__ = 'Michael Liao'

import time, uuid

from orm import Model, StringField, BooleanField, FloatField, TextField

def next_id():
    #�����С���Ľ���˵uuid4()����������������ģ���Ҳ��������֤�ˣ���߻��þ�����
    #time.time()���Ƿ��ص�ǰʱ���
    #������������þ�������һ���͵�ǰʱ���йصĶ�һ�޶���id������Ϊ���ݿ����ÿһ�е�����
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
    __table__ = 'users'				#�������

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')#����idΪ����������next_id��������Ĭ��ֵ
    email = StringField(ddl='varchar(50)')	#����
    passwd = StringField(ddl='varchar(50)')	#����
    admin = BooleanField()			#����Ա��ݣ�ֵΪ1��ʾ���û�Ϊ����Ա��ֵΪ0��ʾ���û����ǹ���Ա
    name = StringField(ddl='varchar(50)')	#����
    image = StringField(ddl='varchar(500)')	#Ӧ����ͷ���
    created_at = FloatField(default=time.time)	#����ʱ��Ĭ��Ϊ��ǰʱ�䣬Ҳ��Ҫ����time.time��������

class Blog(Model):
    __table__ = 'blogs'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')	#����id
    user_name = StringField(ddl='varchar(50)')	#������
    user_image = StringField(ddl='varchar(500)')#�����ϴ���ͼƬ
    name = StringField(ddl='varchar(50)')	#������
    summary = StringField(ddl='varchar(200)')	#���¸�Ҫ
    content = TextField()			#��������
    created_at = FloatField(default=time.time)

class Comment(Model):
    __table__ = 'comments'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')	#����id
    user_id = StringField(ddl='varchar(50)')	#������id
    user_name = StringField(ddl='varchar(50)')	#����������
    user_image = StringField(ddl='varchar(500)')#�������ϴ���ͼƬ
    content = TextField()			#��������
created_at = FloatField(default=time.time)