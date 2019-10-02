# @Time : 2019/10/2 15:29 

# @Author : MZ

# @File : MM.py 

# @Software: PyCharm

class MM(object):
    def __init__(self,dict_path):
        self.dictionary=set()
        self.maximum=0
        with open(dict_path,'r',encoding='utf8') as f:
            for line in f:
                line=line.strip()
                if not line:
                    continue
                self.dictionary.add(line)
                if len(line)>self.maximum:
                    self.maximum=len(line)
    def cut(self,text):
        result=[]
        index=0
        single='!'#未匹配到的连续词
        while index<len(text):
            word=None
            for size in range(self.maximum,0,-1):
                if size>len(text)-index:
                    continue
                piece=text[index:index+size]
                if piece in self.dictionary:
                    if len(single)>1:
                        result.append(single)
                        single='！'
                    word=piece
                    result.append(word)
                    index=index+size
                    break
            if word is None:
                single=single+piece
                index=index+1
        if len(single) > 1:
            result.append(single)
        return result

if __name__ == '__main__':
    text="中国人民解放军南京长江大桥"
    tokenizer=MM('../../data/imm_dic.utf8')
    print(tokenizer.cut(text))

