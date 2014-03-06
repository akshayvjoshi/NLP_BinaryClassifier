import nltk
from nltk import bigrams
from nltk.probability import FreqDist
from pprint import pprint
from math import *

fh=open("/home/chintu/NLP/hw1/txt_sentoken/pos/cv000_29590.txt","r")
lines = fh.read()
split_lines = lines.splitlines()
text = ''.join(split_lines)
bg = bigrams(text.split(" "))
freq_dist_unigram = FreqDist(text.split(" "))
freq_dist_bigram = FreqDist(bg)

bigram_prob = dict();
for k,v in freq_dist_bigram.items():
	#print k[0],v
	bigram_prob[k] = float(v)/float(freq_dist_unigram.get(k[0]))
	#print float(v)/float(freq_dist_unigram.get(k[0]))
pprint(bigram_prob)

