# This function samples random lines from a log file (or any txt file for that matters)
# Reservoir_sampling function - code from Wiki

import random
def reservoir_sampling(file_handle,SAMPLE_COUNT):
        # To force the value of the seed so the results are repeatable
        #random.seed(12345)
 
        sample_titles = []
        for index, line in enumerate(file_handle):
                # Generate the reservoir
                if index < SAMPLE_COUNT:
                        sample_titles.append(line)
                else:                  
                        # Randomly replace elements in the reservoir with a decreasing probability         
                        # Choose an integer between 0 and index (inclusive)               
                        r = random.randint(0, index)               
                        if r < SAMPLE_COUNT:                       
                                sample_titles[r] = line
        # now storing the sample lines in a file
        with open('C:/Users/Ekta.Grover/Desktop/train_logs_sampled.txt', 'w') as f:
                for i in range(0,SAMPLE_COUNT):
                        f.write(str(sample_titles[i]))
# usage : reservoir_sampling(file_handle,SAMPLE_COUNT)

