#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'xwlyy'

'''
async web application.
'''

#logging�����þ������һЩ��Ϣ������˵�����server started at http://127.0.0.1:9000...
#python3 app.py֮������������п���������Ϣ��logging�������Ϣ���԰�������������ִ�е����̣��Ժ��ڳ���Ҳ�ǳ��а���
#logging.basicConfig������Ҫ�������Ϣ�ȼ���INFOָ������ͨ��Ϣ��INFO�Լ�INFO���ϵı���˵WARNING������ϢҲ�ᱻ���
import logging; logging.basicConfig(level=logging.INFO)
#������첽IO��֧�֣���������Щ����Ϥ�Ļ�������ϰһ�¡�asyncio����һС��
#���Լ����첽IO�����Ҳ���Ǻ��������ر���loop���÷�һֱ�����Ϳ�ģ��ֽ׶��Ҿ���֪�����Ķ���֪����ô�þ͹��ˣ�����̫������
import asyncio, os, json, time
#datetime���������os��json��time��ʱ��û�õ����õ�����˵
from datetime import datetime
#aiohttp�ǻ���asyncioʵ�ֵ�HTTP��ܣ�webӦ������������http����Ķ��󣬶�web�������Ҳ���Ǻ�����
#��������һ���������Ķ�����ʱ���Ҷ����Ȱ������Ϊһ��������Ϊ���������������Զ������Ϊ����϶���û���
#Ȼ��۲������÷�������������ڴ����е�������ʲô���ã��������ܴ����ƶϳ����Ǹ�ʲô
from aiohttp import web

#���崦��http��������ķ���
def index(request):
    #��ʵ��������˼�������Ϊ���ѵȺź����������Ϊ��Ӧ��body����
    return web.Response(body=b'<h1>Awesome</h1>')
async def init(loop):
    #��web�����м�����Ϣѭ��������һ��֧���첽IO�Ķ���
    app = web.Application(loop=loop)
    #�������ͨ��GET��ʽ�������ĶԸ�Ŀ¼������ת����index��������
    app.router.add_route('GET', '/', index)
    #����127.0.0.1��ַ��9000�˿�
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    #�Ժ�����logging��Ҫ���������۶����ֽ׶λ���������ʲô�ã���Խ������Խ����
    logging.info('server started at http://127.0.0.1:9000...')
    #�Ѽ���http��������Э�̷��ظ�loop���������ܳ�������http����Ӧ���������ɣ���Ҳ��̫ȷ��
    return srv
#loop��Ҳ���Ǻܶ��������Ǿ仰��֪�����Ķ���֪����ô�þ͹���
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()