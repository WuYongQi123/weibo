#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'Nick Suo'

from django import forms


class UserInfoPostForm(forms.Form):
    username = forms.CharField(
        error_messages={'required': '用户名不能为空', 'invalid': '用户名格式错误'}
    )
    email = forms.EmailField(
        error_messages={'required': '邮箱不能为空', 'invalid': '邮箱格式错误'}
    )
    password = forms.CharField(
        error_messages={'required': '密码不能为空', 'invalid': '密码格式错误'}
    )
    name = forms.CharField(
        error_messages={'required': '显示名称不能为空', 'invalid': '显示名称格式错误'}
    )
    head_img = forms.ImageField(
        error_messages={'required': '头像不能为空', 'invalid': '显头像格式错误'}
    )
    sex = forms.IntegerField(
        error_messages={'required': '请选择性别', 'invalid': '性别选择错误'}
    )
    age = forms.IntegerField(
        required=False,
        error_messages={'required': '请输入年龄', 'invalid': '年龄输入格式错误'}
    )
    brief = forms.CharField(
        required=False,
        max_length=140,
        error_messages={'required': '输入简介让别人更快认识你', 'invalid': '简介输入格式错误'}
    )


class NewWeiBo(forms.Form):
    wb_type = forms.IntegerField(
        error_messages={'required': '请选择微博类型', 'invalid': '微博类型格式错误'}
    )
    text = forms.CharField(
        max_length=141,
        error_messages={'required': '微博类型不能为空', 'invalid': '微博内容超过140个最大字数'}
    )
    perm = forms.IntegerField(
        error_messages={'required': '请选择微博查看权限', 'invalid': '选择微博查看权限错误'}
    )
    date = forms.DateField(
        required=False,
    )
    pictures = forms.CharField(
        required=False,
    )
    video = forms.CharField(
        required=False,
    )
    forward = forms.IntegerField(
        required=False,
    )


class picturevideoForm(forms.Form):
    PVFile = forms.FileField()


