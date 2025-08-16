#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
测试PPT转Markdown工具包导入
"""

import sys
import os

# 添加src目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

try:
    from ppt_to_md.main import ppt_to_md
    print("成功导入ppt_to_md模块")
    print("ppt_to_md函数:", ppt_to_md)
except ImportError as e:
    print("导入失败:", e)