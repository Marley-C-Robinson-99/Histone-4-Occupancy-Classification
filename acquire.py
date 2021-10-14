import pandas as pd
import numpy as np
import os
import re
from Bio import SeqIO
###################################         ACQUIRE        ###################################
def get_H4_data():
    '''
        Gets Histone-4 occupancy data from the local machine if possible, if not present 
        grabs txt from http://www.jaist.ac.jp/~tran/nucleosome/ten_dataset/dataset02.txt
        and outputs a dataframe containing the Sequence ID, the Sequence actual, and the pos/neg label
    '''
    # Defining filename and url
    filename = 'dataset02.txt'
    url = 'http://www.jaist.ac.jp/~tran/nucleosome/ten_dataset/dataset02.txt'

    # Initializing empty lists of SequenceID, Sequences, and Pos/Neg labels
    ids = []
    seqs = []
    labels = []

    # Checking for existing cached file
         #Formatted in 3 lines:
         #The first line is the ID,
         #the second is the gene
         #the third is the class
    if os.path.isfile(filename):
        f = open(filename)

        # Parsing lines into usable data
        for i, line in enumerate(f):
            if i % 3 == 0:
                ids.append(str(line).replace('>', '')) # replacing > char
            if i % 3 == 1:
                line = re.sub('[^ATCGatcg]', '', line) # getting rid of all non-nucleotide chars
                seqs.append(line)
            if i%3 == 2:
                labels.append(int(line[0])) # appending labels to list
        f.close()

        # Creating dataframe based on parsed text file lists
        df = pd.DataFrame({'id': ids, 'sequence': seqs, 'label': labels})

        return df
    else:
        cmd = "curl -O {}".format(url)
        os.system(cmd)  # executes a curl -O on the url
        f = open(filename)
        
        # Parsing lines into usable data
        for i, line in enumerate(f):
            if i % 3 == 0:
                ids.append(str(line).replace('>', ''))
            if i % 3 == 1:
                line = re.sub('[^ATCGatcg]', '', line)
                seqs.append(line)
            if i%3 == 2:
                labels.append(int(line[0]))
        f.close()

        # Creating dataframe based on parsed text file lists
        df = pd.DataFrame({'id': ids, 'sequence': seqs, 'label': labels})

        return df