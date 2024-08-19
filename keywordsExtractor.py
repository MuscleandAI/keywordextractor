import jieba
import numpy as np
import heapq

class keywordExtractor():
    def __init__(self):
        idf_dict = {}
        data_list = []
        with open("../dict/idf.txt") as f:
            for line in f:
                ll = line.strip().split(" ")
                if len(ll) != 2:
                    continue
                if ll[0] not in idf_dict:
                    idf_dict[ll[0]] = float(ll[1])
                data_list.append(float(ll[1]))
        self.__idf_dict = idf_dict
        self.median = np.median(data_list)
    
    def get_idf(self,word):
        return self.__idf_dict.get(word, self.median)
    
    def predict(self, query, top_n = 1):
        if len(query) <= 2:
            return [query]
    
        # 切词
        word_list = list(jieba.cut(query))
        if len(word_list) < top_n:
            return word_list
        
        # 默认赋值
        idf_list = []
        for word in word_list:
            idf_list.append(self.get_idf(word))
           
        # 可以进行一些藏经相关的业务调整
        
        # 归一化
        weight_list = [i / max(idf_list) for i in idf_list]
        zip_list = zip(range(len(weight_list)), weight_list)
        n_large_idx = [i[0] for i in heapq.nlargest(top_n, zip_list, key=lambda x:x[1])]

        return [word_list[i] for i in n_large_idx], weight_list
    
if __name__ == "__main__":
    keyword_extractor = keywordExtractor()
    keys = keyword_extractor.predict("我想知道天然气领域的k206输油泵机组电机风道清灰流程", 3)[0]
    str = ''.join(keys)
    print(str)
    input = '404|如在防爆区域用可燃气体检测仪检测无报警，作业现场安全；确认高压室检修泵电机柜处于检修状态：断路器拉至检修位置，合接地刀；电伴热系统断电，均悬挂“禁止合闸、有人工作”标识牌。405|已告知相关的交叉作业负责人。|406|检查个人防护用品齐全、工作所需材料、工具齐全。'
    key2 = keyword_extractor.predict(input.strip().strip('\n'),3)[0]
    str2 = ''.join(set(key2))
    print(str2)