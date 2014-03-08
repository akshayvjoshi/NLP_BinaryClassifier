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
fp = open('results_unigram','w+')
Pos_Dict= dict()
Neg_Dict= dict()
for x in myset:
	temp.remove(x)
        Pos_Dict = get_unigram('pos','/home/avj/Documents/NLP/NLP_BinaryClassifier/dataset',temp)
	# Calculate pos_perplexity
	print len(Pos_Dict)
        Neg_Dict = get_unigram('neg','/home/avj/Documents/NLP/NLP_BinaryClassifier/dataset',temp)
	print len(Neg_Dict)
	# Calculate neg_perplexity
	fpath = '/home/avj/Documents/NLP/NLP_BinaryClassifier/dataset/'+str(x)
	test_file_p = os.listdir(fpath +'/pos')
	test_file_n = os.listdir(fpath+'/neg') 
	fp.writelines("Test folder:"+str(x)+"\n")
	#test positive folder under test folder
	
	for test in test_file_p:
		pos_perp = perplexity(Pos_Dict, fpath+"/pos/"+test)
		neg_perp = perplexity(Neg_Dict, fpath+"/pos/"+test)
		if pos_perp < neg_perp:
			fp.writelines("original pos\t"+test+"\tpred pos\n")
		else:
			fp.writelines("original pos\t"+test+"\tpred neg\n")
	#test negative folder under test folder
	
	for test in test_file_n:
		
                pos_perp = perplexity(Pos_Dict, fpath+"/neg/"+test) 
                #print pos_perp
	
		neg_perp = perplexity(Neg_Dict, fpath+"/neg/"+test) 
        	#print neg_perp
	        if pos_perp < neg_perp:
                        fp.writelines("original neg\t"+test+"\tpred pos\n")
                else:
                        fp.writelines("original neg\t"+test+"\tpred neg\n")
		 
 	print "in progress"	
	temp.add(x)

fp.close()	
#print Pos_Dict
