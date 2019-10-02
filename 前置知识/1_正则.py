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

#使用转义字符 \
import re
if re.search('\\\\','I have one nee\dle') is not None:
    #前两个和后两个分别转义为\,然后\\表示真正的匹配\
    print('match it')
else:
    print('not match')
#原生字符串 r
import re
if re.search(r'\\','I have one nee\dle') is not None:
    print('match it')
else:
    print('match it')

#抽取文本中的数字 [0-9] [a-z] {3}重复三次
import re
strings=['War of 1812','There are 5280 feet to a mile','Happy New Year 2016!']
year_strings=[]
for string in strings:
    if re.search('[1-2][0-9]{3}',string):
        year_strings.append(string)
print(year_strings)

#查找出指定匹配字符
import re
year_string='2016 was a good year ,but 2017 will be better!'
years=re.findall('[2][0-9]{3}',year_string)
print(years)