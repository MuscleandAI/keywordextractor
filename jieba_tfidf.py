from jieba.analyse.tfidf import TFIDF
default_tfidf = TFIDF()
text='404|如在防爆区域用可燃气体检测仪检测无报警，作业现场安全；确认高压室检修泵电机柜处于检修状态：断路器拉至检修位置，合接地刀；电伴热系统断电，均悬挂“禁止合闸、有人工作”标识牌。405|已告知相关的交叉作业负责人。|406|检查个人防护用品齐全、工作所需材料、工具齐全。'
docs_list = [text]
for doc in docs_list:
    keywords=default_tfidf.extract_tags(doc, topK=3, withWeight=False, allowPOS=())
    print(keywords)