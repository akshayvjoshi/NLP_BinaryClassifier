import nltk
import os
import re
from nltk import bigrams
from nltk.probability import FreqDist
from pprint import pprint



def get_bigram(Classlabel,path,IterSet):
	"Function to get the unigram model of the given Classlabel(pos/neg) using files in the path"
	#filepath = path
	#files = os.listdir(filepath);
	Prob_dict = dict();
	
	for idx in IterSet:
		fpath = path + "/" + str(idx) + "/" + Classlabel
		print fpath
		files = os.listdir(fpath)
		for fil in files:
			fh=open(fpath+"/"+fil,"r")
			lines = fh.read()
			lines = re.sub("[()+.,\']",'',lines)
			
			split_lines = lines.splitlines()
			text = ''.join(split_lines)
			bg = bigrams(text.split(" "))
			freq_dist_bigram = FreqDist(bg)
			Prob_dict.update(freq_dist_bigram)
	'''
	prob_sum = 0
	num_words = 0
	for elem in Prob_dict.values():
		num_words += elem
	
	for k in Prob_dict:
		val = Prob_dict[k] 
		Prob_dict[k] = val#/float(num_words)
		#prob_sum = prob_sum + Prob_dict[k]
	#print Prob_dict	
	#print prob_sum
	'''
	return Prob_dict
	

if __name__ == "__main__":
    #temp = get_unigram('pos','/home/chintu/NLP/hw1/dataset',set([1,2,3,4]))
    temp = get_unigram('neg','/home/chintu/NLP/hw1/dataset',set([1,2,3,4]))
    #print temp

