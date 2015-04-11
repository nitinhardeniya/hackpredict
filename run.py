
#########################################################################################
#: Batch Run for training the LDA using gensim 
#: Author :Nitin Hardeniya 
#########################################################################################

import sys
import os
from train_lda import trainLda
import matplotlib.pyplot as plt

import sys
import logging
import os
import numpy
from gensim import corpora, models, similarities
from threading import Thread
from readutils import readreviews


def run():
	trainfile=sys.argv[1]
	outdir_name=sys.argv[2]
	reports_dir=sys.argv[3]
	start=18
	end=19
	step=1
	
	
	print 'training .....'

	if(not os.path.exists(outdir_name)):os.mkdir(outdir_name)

	if(not os.path.exists(reports_dir)):os.mkdir(reports_dir)
	#outdir=outdir_name+'_'+pds
	outdir=os.path.join(outdir_name)
	numTopics=20
	docs = readreviews(trainfile)
	print len(docs )
	print docs[1:10]
	trainLda(docs,numTopics,reports_dir, dictoutfile="dictionary.txt", modeloutfile="model.txt")

	

if __name__ == '__main__':
	run()