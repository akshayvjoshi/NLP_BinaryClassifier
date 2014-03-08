from sets import Set
from get_unigram import get_unigram
from get_unigram_file import get_unigram_file
import nltk
import re
import os
from math import *
from nltk.probability import FreqDist
from collections import OrderedDict

def build(master_dict, path, l, fh):
	master = ()
	master = sorted(master_dict)

	m_dict = OrderedDict()
	for item in master:
		m_dict[item] = 0	

	temp = get_unigram_file(path)
	m_dict.update(temp)
	values = list()
	for val in m_dict.itervalues():
		values.append(str(val))
	#print len(values)	
	fh.write(l+","+",".join(values))
	fh.write('\n')


def build_training_vector(master_dict, train_set, path, label, fold):
	fh = open('training'+str(fold)+'.csv', 'w+')
	for x in train_set:
		for l in label:
			files = os.listdir(path+'/'+str(x)+'/'+l)
			for f in files:
				
				build(master_dict, path+'/'+str(x)+'/'+l+'/'+f, l, fh)
				#print f
				'''
				temp = get_unigram_file(path+'/'+str(x)+'/'+l+'/'+f)
				master_dict.update(temp)
				values = list()
				for val in master_dict.itervalues():
					values.append(str(val))
				#print len(values)	
				fh.write(l+","+",".join(values))
				fh.write('\n')
				#print master_dict
				'''
			
		
	fh.close()
	fh = open('test'+str(fold)+'.csv', 'w+')
	for l in label:
		files = os.listdir(path+'/'+str(fold)+'/'+l)
		for f in files:
			build(master_dict, path+'/'+str(fold)+'/'+l+'/'+f, l, fh)
	fh.close()

myset = Set([1,2,3,4,5]);
temp = myset
#fp = open('results_unigram','w+')
master_dict= dict()
Pos_Dict = dict()
Neg_Dict= dict()
path = '/home/avj/Documents/NLP/NLP_BinaryClassifier/dataset'
for x in myset:
	temp.remove(x)
        Pos_Dict = get_unigram('pos', path, temp)
        Neg_Dict = get_unigram('neg', path, temp)
	master_dict.update(Pos_Dict)
	master_dict.update(Neg_Dict)
	for val in master_dict.iterkeys():
		master_dict[val] = 0
	#print master_dict
	master = ()
	master = sorted(master_dict)

	m_dict = OrderedDict()
	for item in master:
		m_dict[item] = 0	
	#print m_dict
	label = set()
	label = ('pos', 'neg')
	build_training_vector(m_dict, temp, path, label, x)
	temp.add(x)
	print x	

#fh.close()	
#print Pos_Dict
