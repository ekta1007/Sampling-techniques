#d all the srch_ids - optimized file
import timeit
start = timeit.timeit()
import random , csv
from itertools import chain
with open("train.csv", "r") as source:
	header=source.readline() # header
	all_srch_ids=[line.split(',')[0] for line in source]
# count of all lines in this file, except the header
count_all=len(all_srch_ids)
print " Total records is : %d " % count_all
# lengths of all samples
unique_srch_id=list(set(all_srch_ids)) # all unique search ids
train_sample_len=int(len(unique_srch_id)*.2)
test_sample_len=int(len(unique_srch_id)*0.2)
cv_sample_len=int(len(unique_srch_id)*.6)
#cv_sample_len=len(unique_srch_id)-(train_sample_len+test_sample_len) # if we were to use all the records in the base input file
print " printing statistics " 
print "total unique records %d , train %d, test %d, cv %d" %(len(unique_srch_id), train_sample_len, test_sample_len, cv_sample_len)

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
print "created dict of all train, test and cv"
#list of all srch_ids
all_srch_ids_used=list(chain.from_iterable(dict_sample.values()))

# optimize this even more
import csv
train_random_choice=[]
test_random_choice=[]
cv_random_choice=[]
with open("train.csv", "r") as source:
    source.readline()# skip header
    xx=source.readline()
    #print xx
    print "started the while loop"
    while len(xx) !=0 :
#print "started the while loop"
        #xx=source.readline()
        xx_key=xx.split(',')[0]
        xx_full=xx.replace('\n','')
       # print xx,xx_key, xx_full
        if xx_key in all_srch_ids_used :
            if xx_key in dict_sample['train']:
                train_random_choice.append(xx_full)
#        if xx_key in all_srch_ids_used :
            elif xx_key in dict_sample['test']:
              test_random_choice.append(xx_full)
 #       if xx_key in all_srch_ids_used :
            elif xx_key in dict_sample['cv']:
                cv_random_choice.append(xx_full)
        xx=source.readline()
        #print xx
        #print "came here"
print "2nd time read was success !"
	
# Now create the sample files from the input file again.
# now save all this in csv files
with open("output_test1.csv", "wb") as sink:
    sink.write(header)
    sink.write("\n".join(test_random_choice))
with open("output_train1.csv", "wb") as sink:
    sink.write(header)
    sink.write("\n".join(train_random_choice))
with open("output_cv1.csv", "wb") as sink:
    sink.write(header)
    sink.write("\n".join(cv_random_choice))

print 'print total sample len %d ' % (len(test_random_choice)+len(cv_random_choice)+len(train_random_choice))
print "test  %d , train %d  cv %d " % (len(test_random_choice),len(train_random_choice),len(cv_random_choice)) 

end = timeit.timeit()
print end - start

