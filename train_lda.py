
#########################################################################################
#: The main utill to train the LDA using gensim 
# more info http://radimrehurek.com/gensim/
#: Author :Nitin Hardeniya 
#########################################################################################

import sys
import logging
import os
import numpy
from gensim import corpora, models, similarities
from threading import Thread
from readutils import readreviews


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', filename="logs_training.txt", level=logging.INFO)
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)


def trainLda(docs,numTopics,reports_dir, dictoutfile="dictionary.txt", modeloutfile="model.txt"):
	''' 
		Trains an lda on the list of documents.
		docs: a list of document words {list of list of words}
		numTopics: number of topics of the lda to be trained
		dictoutfile: output file where dictionary is saved
		modeloutfile: output file where trained model is saved
		perplexity.txt : To evaluate the topics model for different no of topics
	'''
	print docs
	#print len(docs)
	perplexity=open(os.path.join(reports_dir,'_perplexity.txt'),'a')
	topicsTopwordsfile=open(os.path.join(reports_dir,'_'+str(numTopics)+'.txt'),'w')
	topicswordsfile=open(os.path.join(reports_dir,'_'+str(numTopics)+'allwords.txt'),'w')

	dictionary = corpora.Dictionary(docs)
	corpus = [dictionary.doc2bow(doc) for doc in docs]
	tfidf =models.TfidfModel(corpus)
	# tfidf convert 
	corpus_tfidf = tfidf[corpus]
	
	#print corpus
	#passes=50
	logging.info("Starting model training")
	model = models.ldamodel.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=numTopics)
	model.print_topics(50)
	
	for i in range(0, model.num_topics):
		word=model.print_topic(i)
		topicsTopwordsfile.write("topic"+str(i)+'-'*100+'\n')
		topicsTopwordsfile.write(word+'\n')
	
	

	# saving perplexity and other for the model selection
	perplex = model.bound(corpus)

	#@to-do
	#Per_word_Perplexity=numpy.exp2(-perplex / sum(cnt for document in corpus for cnt in document))


	perplexity.write("Topics :"+str(numTopics)+'\t'+str(perplex)+'\n')
	#perplexity.write("Per-word Perplexity :"+str(numTopics)+'\t'+str(Per_word_Perplexity)+'\n')


	logging.info("Done model training")

	# Save the model
	dictionary.save(dictoutfile)
	model.save(modeloutfile)
	

def training():

	''' Wrote a batch fuction that will call trainLDA for different ranges
		start=(int) :start in the range of topics we want to try 
		end=(int) : end in the range of topics we want to try 
		step =(int) :stepsize in the range of topics we want to try 
	'''
	
	if(not os.path.exists(outdir)):	os.mkdir(outdir)
	reports_dir=os.path.join(outdir, 'reports'+PDS)
	if(not os.path.exists(reports_dir)):os.mkdir(reports_dir)
	

	
	docs = readreviews(dealfile)


	

def main():
	#training()
	#parsereviews(sys.argv[1],sys.argv[2])
	return 

if(__name__ == "__main__"):
	main()
