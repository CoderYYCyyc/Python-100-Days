"""
读取PDF文件

Version: 0.1
Author: 骆昊
Date: 2018-03-26
"""

from PyPDF2 import PdfReader

with open('Day01-15/code/Day15/res/Docker入门教程.pdf', 'rb') as f:
    reader = PdfReader(f, strict=False)
    print(f'总页数: {len(reader.pages)}')
    # 检查是否加密，如果加密，则提供正确的密码
    if reader.is_encrypted:
        reader.decrypt('')
    current_page = reader.pages[5]
    # print(current_page)
    print(current_page.extract_text())
