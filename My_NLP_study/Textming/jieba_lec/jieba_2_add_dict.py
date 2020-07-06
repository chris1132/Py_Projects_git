import jieba
import jieba.posseg as posseg

test_sent = "汪朝晖是创新办主任也是云计算方面的专家;"
test_sent2 =test_sent+ "例如我输入一个带“深度学习”的标题，在自定义词库中也增加了此词为N类型"

words = jieba.cut(test_sent,cut_all=False)
print("1------:","/".join(words))

jieba.load_userdict("dict/userdict.txt")
word2 = jieba.cut(test_sent,cut_all=False)
print("2------:","/".join(word2))

result = posseg.cut(test_sent2)
for r in result:
    print("------:",r.word," ",r.flag)


