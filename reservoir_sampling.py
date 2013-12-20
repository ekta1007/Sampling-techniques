# This function samples random lines from a log file (or any txt file for that matters)
# Reservoir_sampling function - code from Wiki

import random
def reservoir_sampling(file_handle,SAMPLE_COUNT)
        # To force the value of the seed so the results are repeatable
        #random.seed(12345)
 
        sample_lines = []
        for index, line in enumerate(open(file_handle)):
                # Generate the reservoir
                if index < SAMPLE_COUNT:
                        sample_lines.append(line)
                else:                  
                        # Randomly replace elements in the reservoir with a decreasing probability         
                        # Choose an integer between 0 and index (inclusive)               
                        r = random.randint(0, index)               
                        if r < SAMPLE_COUNT:                       
                                sample_lines[r] = line
        print sample_lines
