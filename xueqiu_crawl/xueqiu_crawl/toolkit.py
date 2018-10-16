# -*- coding: utf-8 -*-
# ------------------------------------------
#   版本：1.0
#   日期：2018-10-13
#   作者：殷帅　yscoder@foxmail.com
# ------------------------------------------

import codecs
import re


class Toolkit():
    @staticmethod
    def save2file(filename, content):
        # 保存为文件
        filename = filename + ".txt"
        f = open(filename, 'a')
        f.write(content)
        f.close()

    @staticmethod
    def save2filecn(filename, content):
        # 保存为文件
        filename = filename + ".txt"
        f = codecs.open(filename, 'a', encoding='utf-8')
        f.write(content)
        f.close()

    @staticmethod
    def getUserData(cfg_file):
        f = open(cfg_file, 'r')
        account = {}
        for i in f.readlines():
            ctype, passwd = i.split('=')
            # print ctype
            # print passwd
            account[ctype.strip()] = passwd.strip()
        return account

    @staticmethod
    def filename_filter(filename_old):
        filename = re.sub('[\/:*?"<>|]', '-', filename_old)
        return filename
