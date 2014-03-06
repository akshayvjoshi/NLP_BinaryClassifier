from sets import Set
from get_unigram import get_unigram
import nltk
import re
import os
from math import *

def perplexity(Prob_dist, filename):
	fh = open(filename, 'r')
        lines = fh.read()
        lines = re.sub("[()+.,\']",'',lines)
        words = nltk.tokenize.word_tokenize(lines)
	N = 0
	for v in Prob_dist.values():
		N=N+v
	prob = float(0)
	v= len(words)
	for word in words:
		if word in Prob_dist.keys():
			prob = prob + log10(float(Prob_dist[word])/float(N))
		else:
				
			prob = prob + 0.0

	perplex = float(-1)*(float(1)/float(v))*prob
	perplex = 10**perplex
	print perplex
	return perplex

myset = Set([1,2,3,4,5]);
temp = myset

Pos_Dict= dict()
Neg_Dict= dict()
for x in myset:
	temp.remove(x)
        Pos_Dict = get_unigram('pos','/home/chintu/NLP/hw1/dataset',temp)
	# Calculate pos_perplexity
	print len(Pos_Dict)
        Neg_Dict = get_unigram('neg','/home/chintu/NLP/hw1/dataset',temp)
	print len(Neg_Dict)
	# Calculate neg_perplexity
	fpath = '/home/chintu/NLP/hw1/dataset/'+str(x)
	test_file_p = os.listdir(fpath +'/pos')
	test_file_n = os.listdir(fpath+'/neg') 
	print "Test folder:",x
	#test positive folder under test folder
	
	for test in test_file_p:
		pos_perp = perplexity(Pos_Dict, fpath+"/pos/"+test)
		neg_perp = perplexity(Neg_Dict, fpath+"/pos/"+test)
		if pos_perp < neg_perp:
			print "original pos\t"+test+"\tpred pos"
		else:
			print "original pos\t"+test+"\tpred neg"
	#test negative folder under test folder
	'''
	for test in test_file_n:
		
                pos_perp = perplexity(Pos_Dict, fpath+"/neg/"+test) 
                print pos_perp
	
		neg_perp = perplexity(Neg_Dict, fpath+"/neg/"+test) 
        	print neg_perp
	        if pos_perp < neg_perp:
                        print "original neg\t"+test+"\tpred pos"
                else:
                        print "original neg\t"+test+"\tpred neg"
		 
 	'''
	temp.add(x)
	break
	
#print Pos_Dict
