import nltk
import os
import re
from nltk import bigrams
from nltk.probability import FreqDist
from pprint import pprint



def get_unigram(Classlabel,path):
	"Function to get the unigram model of the given Classlabel(pos/neg) using files in the path"
	filepath = path+"/"+Classlabel
	files = os.listdir(filepath);
	Prob_dict = dict();
	for fil in files:
		fh=open(filepath+"/"+fil,"r")
		lines = fh.read()
		lines = re.sub("[()+.,\']",'',lines)
		words = nltk.tokenize.word_tokenize(lines)
		freq_dist_unigram = FreqDist(words)
		Prob_dict.update(freq_dist_unigram)
	prob_sum = 0
	num_words = 0
	for elem in Prob_dict.values():
		num_words += elem

	for k in Prob_dict:
		val = Prob_dict[k] 
		Prob_dict[k] = float(val)/float(num_words)
		prob_sum = prob_sum + Prob_dict[k]
	#print Prob_dict	
	print prob_sum
	return Prob_dict
	

if __name__ == "__main__":
    #temp = get_unigram('pos','/home/chintu/NLP/hw1/dataset/1')
    temp = get_unigram('neg','/home/chintu/NLP/hw1/dataset/1')
    #print temp

