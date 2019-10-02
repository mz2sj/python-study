# @Time : 2019/10/2 13:14

# @Author : MZ

# @File : RMM.py 

# @Software: PyCharm
class IMM(object):
    def __init__(self,dic_path):
        self.dictionary=set()
        self.maximum=0
        # 读取字典
        with open(dic_path,'r',encoding='utf-8') as f:
            for line in f:
                line=line.strip()
                if not line:
                    continue
                self.dictionary.add(line)
                if(len(line)>self.maximum):
                    self.maximum=len(line)

    def reverse_word(self,word):
        return word[::-1]

    def cut(self,text):
        result=[]
        single=''
        index=len(text)
        while index>0:
            word=None
            for size in range(self.maximum,0,-1):
                if index-size<0:
                    continue
                piece=text[(index-size):index]
                if piece in self.dictionary:
                    if len(single)>0:
                        result.append(self.reverse_word(single))
                    single=''
                    word=piece
                    result.append(word)
                    index-=size
                    break
            if word is None:
                index-=1
                #未匹配到的单字
                single=single+piece
        if len(single)>0:
            result.append(self.reverse_word(single))
        return result[::-1]
if __name__ == '__main__':
    text='南京长江大桥人民解放军'
    tokenizer=IMM('../../data/imm_dic.utf8')
    print(tokenizer.cut(text))