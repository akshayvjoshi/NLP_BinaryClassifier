import nltk
import os
import re
from nltk import bigrams
from nltk.probability import FreqDist
from pprint import pprint



def get_unigram_file(path):
	"Function to get the unigram model of the given file"
	
	fh=open(path,"r")
	lines = fh.read()
	lines = re.sub("[()+.,\']",'',lines)
	words = nltk.tokenize.word_tokenize(lines)
	freq_dist_unigram = FreqDist(words)
	probdict =dict(freq_dist_unigram)
	#print probdict	
	return probdict
	

if __name__ == "__main__":
    #temp = get_unigram('pos','/home/chintu/NLP/hw1/dataset',set([1,2,3,4]))
    temp = get_unigram('/home/avj/Documents/NLP/NLP_BinaryClassifier/dataset/2/pos/cv200_2915.txt')
    #print temp

