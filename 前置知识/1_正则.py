import re

#获取包含关键字的句子
text_string='文本的主要来源无疑是网络。我们要把网络中的文本获取形成一个文本数据库。利用一个爬虫爬取到网络中的信息。爬取' \
            '的策略又广度爬取和深度爬取。根据用户的需求，爬虫可以有主题爬虫和通用爬虫之分。'
regex='爬虫'
p_string=text_string.split('。')
for line in p_string:
    if re.search(regex,line) is not None:
        print(line)

import re

#获取包含关键字的句子
text_string='文本的主要来源无疑是网络。我们要把网络中的文本获取形成一个文本数据库。利用一个爬虫爬取到网络中的信息。爬取' \
            '的策略又广度爬取和深度爬取。根据用户的需求，爬虫可以有主题爬虫和通用爬虫之分。'
regex='爬虫'
p_string=text_string.split('。')
regex="文本"
for line in p_string:
    if re.search(regex,line) is not None:
        print(line)

#匹配任意一个字符 符号.可以匹配任意字符
import re
text_string='文本的主要来源无疑是网络。我们要把网络中的文本获取形成一个文本数据库。利用一个爬虫爬取到网络中的信息。爬取' \
            '的策略又广度爬取和深度爬取。根据用户的需求，爬虫可以有主题爬虫和通用爬虫之分。'
regex='爬'
p_string=text_string.split('。')
regex='爬.'
for line in p_string:
    if re.search(regex,line) is not None:
        print(line)


#匹配起始和结尾字符串 起始 ^a 结尾a$
import re
text_string='文本的主要来源无疑是网络。我们要把网络中的文本获取形成一个文本数据库。利用一个爬虫爬取到网络中的信息。爬取' \
            '的策略又广度爬取和深度爬取。根据用户的需求，爬虫可以有主题爬虫和通用爬虫之分。'
regex='^文本'
p_string=text_string.split('。')
for line in p_string:
    if re.search(regex,line) is not None:
        print(line)

regex='信息$'
p_string=text_string.split('。')
for line in p_string:
    if re.search(regex,line) is not None:
        print(line)

#使用中括号匹配多个字符 [abc]
import re
text_string=['[重要的]今年第七号台风23日登陆广东东部沿海地区','上海发布车库销售监管通知：违规者暂停网签资格',
             '[紧要的]中国对印连发强硬信息，印度急需结束对峙']
regex='^\[[重紧]..\]'
for line in text_string:
    if re.search(regex,line) is not None:
        print(line)
    else:
        print('not match')