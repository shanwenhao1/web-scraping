# 创建爬虫

## BeautifulSoup

BeautifulSoup将HTML内容转换成对象(树形结构)

- BS中的find函数
    - find(tag, attributes, recursive, text, limit, keywords)
    - findAll(tag, attributes, recursive, text, limit, keywords)
        - recursive默认为True, 递归查找所有标签及字标签; False为只查找一级标签
        - text根据标签的文本内容去匹配