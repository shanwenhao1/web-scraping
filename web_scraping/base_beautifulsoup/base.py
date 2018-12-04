#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4
# @Author  : Wenhao Shan

from urllib.request import urlopen
from bs4 import BeautifulSoup

url_path = "http://www.pythonscraping.com/pages/warandpeace.html"

html = urlopen(url_path)
bs_obj = BeautifulSoup(html, "html5lib")

# 用findAll函数抽取只包含在<span class="green"></span>标签里的文字
name_list = bs_obj.findAll("span", {"class": "green"})
for name in name_list:
    print(name)
    # .get_text() 只返回字符串(去除标签、超链接、段落等)
    print(name.get_text())
