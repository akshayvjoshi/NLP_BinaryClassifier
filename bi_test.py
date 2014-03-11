from sets import Set
from get_unigram import get_unigram
from get_bigram import get_bigram
from nltk import *
import re
import os
from math import *

def convert(Prob_dist_uni, Prob_dist_bi):
	
	for item in Prob_dist_bi.iterkeys():
		#val = Prob_dist_bi[item]
		#print item		
		if item[0] in Prob_dist_uni.keys():	
			Prob_dist_bi[item] = Prob_dist_bi[item]/Prob_dist_uni[item[0]]
		else:
			Prob_dist_bi[item] = 0.0
	return Prob_dist_bi


def perplexity(Prob_dist_uni, Prob_dist_bi, filename):
	fh = open(filename, 'r')
        lines = fh.read()
        lines = re.sub("[()+.,\']",'',lines)
	
	split_lines = lines.splitlines()
	text = ''.join(split_lines)
	bg = bigrams(text.split(" "))
	#freq_dist_bigram = FreqDist(bg)

	#N = 0
	#for v in Prob_dist.values():
	#	N=N+v
	prob = float(0)
	v= len(bg)
	for pair in bg:
		if pair in Prob_dist_bi.keys():
			 if pair[0] in Prob_dist_uni.keys():
				prob = prob + log10(float(Prob_dist_bi[pair]))
		  	        #print prob
		else:	
			prob = prob + 0.0

	perplex = float(-1)*(float(1)/float(v))*prob
	perplex = 10000*(10**perplex)
	#print perplex
	return perplex

myset = Set([1,2,3,4,5]);
temp = myset
fp = open('results_bigram','w+')
Pos_Dict_uni= dict()
Pos_Dict_bi= dict()
Neg_Dict_uni= dict()
Neg_Dict_bi= dict()
for x in myset:
	temp.remove(x)
        Pos_Dict_uni = get_unigram('pos','/home/avj/Documents/NLP/NLP_BinaryClassifier/dataset',temp)
	Pos_Dict_bi = get_bigram('pos','/home/avj/Documents/NLP/NLP_BinaryClassifier/dataset',temp)
	# Calculate pos_perplexity
	print len(Pos_Dict_bi)
	print len(Pos_Dict_uni)
        Neg_Dict_uni = get_unigram('neg','/home/avj/Documents/NLP/NLP_BinaryClassifier/dataset',temp)
        Neg_Dict_bi = get_bigram('neg','/home/avj/Documents/NLP/NLP_BinaryClassifier/dataset',temp)
	print len(Neg_Dict_bi)
	print len(Neg_Dict_uni)
	# Calculate neg_perplexity
	fpath = '/home/avj/Documents/NLP/NLP_BinaryClassifier/dataset/'+str(x)
	test_file_p = os.listdir(fpath +'/pos')
	test_file_n = os.listdir(fpath+'/neg') 
	fp.writelines("Test folder:"+str(x)+"\n")
	#test positive folder under test folder
	
	Pos_Dict_bi = convert(Pos_Dict_uni, Pos_Dict_bi)
	Neg_Dict_bi = convert(Neg_Dict_uni, Neg_Dict_bi)
	y_true = list()
	y_pred = list()
	for test in test_file_p:
		pos_perp = perplexity(Pos_Dict_uni, Pos_Dict_bi, fpath+"/pos/"+test)
		neg_perp = perplexity(Neg_Dict_uni, Neg_Dict_bi, fpath+"/pos/"+test)
		if pos_perp < neg_perp:
                        y_true.append(int(1))
			y_pred.append(int(1))
                        print "original pos\t"+test+"\tpred pos\n" 
			#fp.writelines("original pos\t"+test+"\tpred pos\n")
		else:
                        y_true.append(int(1))
			y_pred.append(int(0))
                        print "original pos\t"+test+"\tpred neg\n" 
			#fp.writelines("original pos\t"+test+"\tpred neg\n")
	#test negative folder under test folder
	
	for test in test_file_n:
		
                pos_perp = perplexity(Pos_Dict_uni, Pos_Dict_bi, fpath+"/neg/"+test) 
                #print pos_perp
	
		neg_perp = perplexity(Neg_Dict_uni, Neg_Dict_bi, fpath+"/neg/"+test) 
        	#print neg_perp
	        if pos_perp < neg_perp:
                        y_true.append(int(0))
			y_pred.append(int(1))
                        print "original neg\t"+test+"\tpred pos\n" 
			#fp.writelines("original neg\t"+test+"\tpred pos\n")
                else:
                        y_true.append(int(0))
			y_pred.append(int(0))
			print "original neg\t"+test+"\tpred neg\n" 
                        #fp.writelines("original neg\t"+test+"\tpred neg\n")
		 
 	print "in progress"	

	target_names = ['pos', 'neg']
	from sklearn.metrics import classification_report
	print(classification_report(y_true, y_pred, target_names=target_names))
	break
	temp.add(x)

fp.close()	
#print Pos_Dict
