# Have been plain lazy to merge the optimal changes of this file with the sample_expedia.py - so placing this as a placeholder till I do make the time.

#with  all the srch_ids - optimized file
import random , csv
from itertools import chain
with open("train.csv", "r") as source:
	header=source.readline() # header
	all_srch_ids=[line.split(',')[0] for line in source]
# count of all lines in this file, except the header
count_all=len(all_srch_ids)
print " Total records is : %d " % count_all
# lenghts of all samples
unique_srch_id=list(set(all_srch_ids)) # all unique search ids
train_sample_len=int(len(unique_srch_id)*.05)
test_sample_len=int(len(unique_srch_id)*.05)
cv_sample_len=int(len(unique_srch_id)*.05)
print " printing statistics " 
print "total unique records %d , train %d, test %d, cv %d" %(len(unique_srch_id), train_sample_len, test_sample_len, cv_sample_len)

#cv_sample_len=len(unique_srch_id)-(train_sample_len+test_sample_len)
#print len(unique_srch_id)
#print train_sample_len, test_sample_len , cv_sample_len
# create a dict with random srch_ids of this len for all three and then write the corresponding files with these srch_ids
dict_sample={'train':[],'test':[],'cv':[]}
dict_sample['train']=random.sample(unique_srch_id,train_sample_len)
for x in dict_sample['train']:
     unique_srch_id.remove(x)
dict_sample['test']=random.sample(unique_srch_id,test_sample_len)
for x in dict_sample['test']:
     unique_srch_id.remove(x)
dict_sample['cv']=random.sample(unique_srch_id,cv_sample_len)
print "dict created"
#list of all srch_ids
all_srch_ids_used=list(chain.from_iterable(dict_sample.values()))
print "len of all srch ids used %d" % len(all_srch_ids_used)

#import csv
with open("train.csv", "r") as source:
	source.readline()# skip header
	list_all=[line.replace('\n','') for line in source if line.split(',')[0] in all_srch_ids_used ]
print "len list_all read %d " % len(list_all)
print "reading success"
# I will modify this to read only the lines that have the search id in either of these three files

	
# Now create the sample files from the input file again.
"""with open("D:/Expedia/data/train.csv", "r") as source:
	source.readline()# skip header
	list_all=[line.replace('\n','') for line in source] # instead of this I could also split all the files and combine them later."""
train_random_choice=[]
test_random_choice=[]
cv_random_choice=[]
for i in range(0,train_sample_len):
    for j in range(0,len(list_all)):
        if dict_sample['train'][i]==list_all[j].split(',')[0]:
            train_random_choice.append(list_all[j])
for i in range(0,test_sample_len):
    for j in range(0,len(list_all)):
        if dict_sample['test'][i]==list_all[j].split(',')[0]:
            test_random_choice.append(list_all[j])
for i in range(0,cv_sample_len):
    for j in range(0,len(list_all)):
        if dict_sample['cv'][i]==list_all[j].split(',')[0]:
            cv_random_choice.append(list_all[j])            
print " writing the individual files sucess- wil write csv files now "
# now save all this in csv files
with open("output_test.csv", "wb") as sink:
    sink.write(header)
    sink.write("\n".join(test_random_choice))
with open("output_train.csv", "wb") as sink:
    sink.write(header)
    sink.write("\n".join(train_random_choice))
with open("output_cv.csv", "wb") as sink:
    sink.write(header)
    sink.write("\n".join(cv_random_choice))

print 'print total sample len %d ' % (len(test_random_choice)+len(cv_random_choice)+len(train_random_choice))
print "test  %d , train %d  cv %d " % (len(test_random_choice),len(train_random_choice),len(cv_random_choice)) 
print "job over !" 

