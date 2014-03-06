import os
from shutil import *

curdir = os.getcwd()
filedir = os.getcwd()+"/txt_sentoken/"
print filedir
pos_filedir = filedir + "pos/"
neg_filedir = filedir + "neg/"

pos_files = sorted(os.listdir(pos_filedir))
neg_files = sorted(os.listdir(neg_filedir))

if not os.path.exists("dataset"):
	os.makedirs("dataset")

num_folds = 5
for i in range(1,num_folds+1):
	dir_path = curdir+"/dataset/"+str(i);
	if not os.path.exists(dir_path):
		os.makedirs(dir_path)

	if not os.path.exists(dir_path + "/pos"):
                os.makedirs(dir_path + "/pos")	

	if not os.path.exists(dir_path + "/neg"):
                os.makedirs(dir_path + "/neg")	

	# Left and right folder number limits for 200 file set
	l = 200*(i-1)
	r = 200*i - 1
	while l<=r:
		# Copy the file with index l into the pos folder
		src = pos_filedir+pos_files[l]
		dst = dir_path+"/pos/"
		copy(src,dst)

		# Copy the file with index l into the neg folder
		src = neg_filedir+neg_files[l]
		dst = dir_path+"/neg/"
		copy(src,dst)
		l+=1
				
	
