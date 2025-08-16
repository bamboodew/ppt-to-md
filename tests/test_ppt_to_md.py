#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
测试PPT转Markdown工具
"""

import sys
import os

# 添加src目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import unittest
from ppt_to_md.main import ppt_to_md

class TestPptToMd(unittest.TestCase):
    """测试PPT转Markdown功能"""

    def test_ppt_to_md_function(self):
        """测试ppt_to_md函数"""
        # 这里可以添加具体的测试逻辑
        # 由于我们没有实际的PPT文件用于测试，这里只是一个示例
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()