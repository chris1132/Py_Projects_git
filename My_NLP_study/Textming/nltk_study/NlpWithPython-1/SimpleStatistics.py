from nltk.book import *
# text1.concordance("monstrous")
# text2.common_contexts(["monstrous","very"])
# text2.similar("monstrous")
# text4.dispersion_plot(["citizens","democracy","freedom","duties","America"])
# print(sorted(set(text3)))

'''
fdist = FreqDist(samples) 创建包含给定样本的频率分布
fdist.inc(sample) 增加样本
fdist['monstrous'] 计数给定样本出现的次数
fdist.freq('monstrous') 给定样本的频率
fdist.N() 样本总数
fdist.keys() 以频率递减顺序排序的样本链表
for sample in fdist: 以频率递减的顺序遍历样本
fdist.max() 数值最大的样本
fdist.tabulate() 绘制频率分布表
fdist.plot() 绘制频率分布图
fdist.plot(cumulative=True) 绘制累积频率分布图
fdist1 < fdist2 测试样本在 fdist1 中出现的频率是否小于 fdist2
'''
'''
频率分布
'''
# FreqDist计算text1里的单词出现的次数，以元祖形式组合（“live”，500）
# f = FreqDist(text1)
#
# f.plot(20,cumulative=True)

# 出现一次的词
# v = f.hapaxes()

# 出现次数最多的词
# v = f.keys()
# print(f["whale"])
'''
细粒度的选择词
'''
# v = set(text1)
# words = [ w for w in v if len(w)>15]

# f = FreqDist(text5)
# w这个单次长度>7 并且 出现次数>7
# word = [w for w in set(text5) if len(w)>7 and f[w]>7]

'''
词语搭配和双连词
'''
# from nltk import bigrams
# bigrams(['the','end','begin','said'])
# print(text4.collocations())
