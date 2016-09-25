#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'Nick Suo'

# 数据库配置
DBSetting = {
    'NAME': 'weiboDB',
    'USER': 'root',
    'PASSWORD': 'suoning',
    'HOST': '192.168.0.138',
    'PORT': '',
}

# rabbitMQ 配置
rabbitMQ = {
    'host': '192.168.0.180',
    'no_ack': False,            # 是否启用 acknowledgment 消息不丢失， False/True, False 为启用状态
    'New_weibo': 'newweibo',    # 添加微博队列名字
}

# session 配置
session = {
    'status': True,         # 是否启用session
    'encryption': True,     # 是否加密session
    'host': '192.168.0.160',
    'port': '6379',
    'DB': 0,
    'passwd': 'wuyongqi123',
    'name': 'xja9sqa9sniul8',
    'time_out': 20,         # 单位秒
}




