import nltk
from numpy import dot,random

# Movie review result: +1 for pos, -1 for neg
numIter = [1]*100
learning_rate = 0.2

def WeightUpdate(weights,train_data,err):
	" Update the weights"
	for i in [1]*len(train_data):
		weights[i] += (float)(learning_rate)*(float)(err)*(train_data[i]) 



def Perceptron():
	"Perceptron Model"
vector = list()
flag = 0

with open('training21.csv','r',1) as fh:
	for lines in fh:
		#lines = fh.readline()
		vector = list(lines.split(','))
		vector[-1] = vector[-1].rstrip()
		#print vector[-1]
		if vector[0] == 'pos':
			expected_res = 1
		else:
			expected_res = -1

		training_data = vector[1:]
		
		training_data = [float(i) for i in training_data]
		#training_data[1] = float(0)		
		wt = float(1)/float(len(training_data));
		#print wt
		
		#weights = [wt]*len(training_data);
		if flag == 0:
			weights = random.rand(len(training_data));
			flag = 1
		
		for idx in numIter:
			result = dot(weights,training_data);
			if result >= 0:
				res = 1
			else:
				res = -1
		
			if res != expected_res:
				err = expected_res - res
				WeightUpdate(weights,training_data,err)
#print len(lines)
#print vector 
#print len(vector)


true_label = list()
pred_label = list()
with open('test_2_1.csv','r',1) as fhandle:
	for lines in fhandle:
		vector = list(lines.split(','))
                vector[-1] = vector[-1].rstrip()
		if vector[0] == 'pos':
                	true_label.append(1)
		else:
			true_label.append(0)
		test_data = vector[1:]
					
                test_data = [float(i) for i in test_data]
		#test_data[1] = float(0)
		result = dot(weights,test_data)
	        if result >= 0:
			pred_label.append(1)
		else:
			pred_label.append(0)
				

target_names = ['1', '0']
from sklearn.metrics import classification_report
print(classification_report(true_label, pred_label, target_names=target_names))

		
'''
f=open('train_weights','w+')
for item in weights:
	f.write("%s\n" % item)
	
f.close
	
print weights

'''

#pprint(weights)
#print training_data 
#print len(training_data)
