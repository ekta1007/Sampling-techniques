# This function samples random lines from a log file (or any txt file for that matters)
# Reservoir_sampling function - code from Wiki

# To optimize this file, think about how one could store the "sampled" lines in file as strings, and then randomly replace these lines, without having to store it as a list 1st.
import random
def reservoir_sampling(file_handle,SAMPLE_COUNT):
        # To force the value of the seed so the results are repeatable
        #random.seed(12345)
 
        sample_lines = []
        for index, line in enumerate(file_handle):
                # Generate the reservoir
                if index < SAMPLE_COUNT:
                        sample_lines.append(line)
                else:                  
                        # Randomly replace elements in the reservoir with a decreasing probability         
                        # Choose an integer between 0 and index (inclusive)               
                        r = random.randint(0, index)               
                        if r < SAMPLE_COUNT:                       
                                sample_lines[r] = line
        # now storing the sample lines in a file
        with open('C:/Users/Ekta.Grover/Desktop/train_logs_sampled.txt', 'w') as f:
                for i in range(0,SAMPLE_COUNT):
                        f.write(str(sample_lines[i]))
# usage : reservoir_sampling(file_handle,SAMPLE_COUNT)

