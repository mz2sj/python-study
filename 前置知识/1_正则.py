import re

text_string='文本的主要来源无疑是网络。对方的的。好文本。'
regex='文本'
p_string=text_string.split('。')
for line in p_string:
    if re.search(regex,line) is not None:
        print(line)
