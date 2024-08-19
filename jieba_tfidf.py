from jieba.analyse.tfidf import TFIDF
default_tfidf = TFIDF()
text='检查个人防护用品齐全、工作所需材料、工具齐全。'
docs_list = [text]
for doc in docs_list:
    keywords=default_tfidf.extract_tags(doc, topK=3, withWeight=False, allowPOS=())
    print(keywords)
