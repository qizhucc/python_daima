#cell-1
import jieba
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import jieba.analyse

text= open('gjc.txt','r',encoding='utf-8').read()

tags = jieba.analyse.extract_tags(text,3)
print(tags)

words = jieba.lcut_for_search(text)
cuted = ' '.join(words)
stopword = ['王者','IP']  # 设置停止词，也就是你不想显示的词，这里这个词是我前期处理没处理好，你可以删掉他看看他的作用
fontpath=r'C:\Windows\Fonts\simfang.ttf'

aimask=np.array(Image.open("o_002.jpg"))
genclr=ImageColorGenerator(aimask)

wc = WordCloud(font_path=fontpath,  # 设置字体
               background_color="white",  # 背景颜色
               max_words=600,  # 词云显示的最大词数
               max_font_size=100,  # 字体最大值
               min_font_size=5, #字体最小值
               random_state=42, #随机数
               collocations=False, #避免重复单词
               mask=aimask, #造型遮盖
               color_func=genclr,
               width=1600,height=1200,margin=2, #图像宽高，字间距，需要配合下面的plt.figure(dpi=xx)放缩才有效
              ).generate(cuted)


#cell-4

plt.figure(dpi=150) #通过这里可以放大或缩小
plt.imshow(wc)
plt.axis("off") #隐藏坐标
plt.show()  # 显示图片