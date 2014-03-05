import nltk
from nltk import bigrams
from nltk.probability import FreqDist

fh=open("/home/chintu/NLP/hw1/txt_sentoken/pos/cv000_29590.txt","r")
lines = fh.read()
split_lines = lines.splitlines()
text = ''.join(split_lines)
bg = bigrams(text.split(" "))
freq_dist_unigram = FreqDist(text.split(" "))
freq_dist_bigram = FreqDist(bg)
print freq_dist_bigram

