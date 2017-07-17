# -*- coding: utf-8 -*-
from os import path
from PIL import Image
import numpy as np
import matplotlib 
from wordcloud import *
import itchat
import re
matplotlib.use('Agg')



d = path.dirname('.')
text = open(path.join(d,'text.txt')).read()

#set the background image
alice_coloring = np.array(Image.open(path.join(d,"kawayi.jpg")))

stopwords = set(STOPWORDS)
stopwords.add('say')



wc = WordCloud(background_color="white",max_words=1000,mask=alice_coloring,stopwords=stopwords,max_font_size=500,random_state=42)

#Generate word cloud 
wc.generate(text)

fig1 = matplotlib.pyplot.gcf()
# create coloring from image
image_colors = ImageColorGenerator(alice_coloring)
matplotlib.pyplot.imshow(wc,interpolation="bilinear")

matplotlib.pyplot.axis("off")

fig1.savefig('test3.png', dpi=100)
#show
matplotlib.pyplot.figure()


# recolor wordcloud and show 
#we could also give color_func = image_colors directly in the constructors





# figure
matplotlib.pyplot.imshow(wc.recolor(color_func=image_colors),interpolation="bilinear")
matplotlib.pyplot.axis("off")
matplotlib.pyplot.figure()

fig1.savefig('test2.png', dpi=100)
# color 
matplotlib.pyplot.imshow(alice_coloring,cmap=matplotlib.pyplot.cm.gray,interpolation="bilinear")
matplotlib.pyplot.axis("off")
fig1.savefig('test.png', dpi=100)



'''
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('tessstttyyy.png', dpi=100)
'''
