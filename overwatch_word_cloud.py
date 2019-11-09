'''
Created on Aug 20, 2019

@author: ywkim
'''


import praw
import numpy as np
from PIL import Image
from datetime import datetime
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

reddit = praw.Reddit('search_bot')
subreddit = reddit.subreddit('OverwatchUniversity')


if __name__ == "__main__":
    date = str(datetime.today())[:10]
    text = ''
    for submission in subreddit.top(limit=100):
        op_text = submission.selftext.lower()
        text += op_text

    # ow_logo_mask = np.array(Image.open('overwatch_logo_transparent.png'))

    stopwords = set(STOPWORDS)
    for word in ['will', 'https', 'gfycat', 'game', 'team', 'play', 'player']:
        stopwords.add(word)
    wc = WordCloud(background_color="white", max_words=100, width=800, height=400,
                   stopwords=stopwords, contour_width=3, contour_color='steelblue')

    wc.generate(text)

    #  wc.to_file("overwatch_univ_word_cloud.png", dpi=300)

    plt.figure(figsize=(20, 10))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    #plt.show()
    plt.savefig('overwatch_univ_word_cloud_' + date + '.png', dpi=300)