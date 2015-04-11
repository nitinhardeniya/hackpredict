####################################################################################################
#	Prints topics for a new document using a trained LDA model
#: Author :Nitin Hardeniya 
#########################################################################################

from gensim.models import LdaModel
from gensim.corpora import Dictionary
import logging
import sys
import re


"""
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(funcName)s,%(lineno)d %(message)s',
					 filename=logfile,
					 filemode='a',
					 level=logging.DEBUG)
"""
class GetTopics:
	''' A class housing apis to retrieve topics for a new document'''
	

	def __init__(self, ldaModelFile, dictionaryfile, stopfile="english.stop.txt"):
		'''
			Const
			Parameters:
				ldaModelFile: the model file that was trained 
				dictionaryfile: id2word mapping file
		'''
		logging.info("[Start] Loading the dictionary " + dictionaryfile)
		self.id2word = Dictionary.load(dictionaryfile)
		logging.info("[Stop] Loading the dictionary " + dictionaryfile)

		logging.info("[Start] Loading the model file " + ldaModelFile)
		self.ldamodel = LdaModel.load(ldaModelFile)
		logging.info("[Done] Loading the model file " + ldaModelFile)

		logging.info("[Start] Loading all topics")
		self.alltopics = self.ldamodel.show_topics(-1)
		logging.info("[Start] Loading all topics")

		self.stopwords = self.loadStop(stopfile)


	def loadStop(self, stopfile='data/english.stop.txt'):
		''' Returns dictionary of stopwords '''
		return set( [word.strip().lower() for word in open(stopfile).readlines()] )


	def getTokens(self, string, delimiter=''):
		'''
			Gets an array of tokens in the given string
			Parameters:
				string: text that needs to be tokenized
				delimter: delimiter for splitting
			Returns:
				a list of tokens
		'''
		tokens = [tok for tok in string.lower().split() if tok not in self.stopwords]
		return tokens
		#return self.id2word.doc2bow(tokens)

	
	def getTopicsStr(self, string):
		'''
			Gets topics for the text specified.
		'''
		doc = self.getTokens(string)
		return self.getTopics(doc)


	def getTopics(self, tokens):
		'''
			Gets topics for the list of tokens
			Parameters:
				- tokens: list of tokens of a document
			Return:
				- a list of topics
		'''
		doc = self.id2word.doc2bow(tokens)
		doc_topics = self.ldamodel[doc]
		sorted_doc_topics = sorted(doc_topics, key=lambda tup: tup[1], reverse=True)
		rel_topics = list()
		for topic in sorted_doc_topics:
			rel_topics.append( (topic[1], self.alltopics[topic[0]], topic[0] ) )
		return rel_topics


	def numTopics(self):
		'''
			Returns:
				- number of topics
		'''
		return len(self.alltopics)


	def getTopicWithNum(self, topicNum):
		''' Gets the topic.
			Parameters:
				- topicNum: topic number for which word distribution is returned (between 0 to self.numTopics()-1)
			Returns:
				- A list of words in the order of relevance.
		'''
		if topicNum == -1:
			return self.alltopics
		else:
			return self.alltopics[topicNum]
			



def main():
	lda = GetTopics(sys.argv[1], sys.argv[2])
	#text = ' '.join( [ line.strip() for line in  open(sys.argv[3]).readlines() ] )
	print lda.getTopicWithNum(-1)

if(__name__=="__main__"):
	if(len(sys.argv) < 2):
		print "Wrong Syntax."
		print "The right syntax is: "
		print "\tpython " + sys.argv[0] + " <lda model file> <gensim generated dictionary file, ending with *_wordids.txt> <new doc filename>"
		sys.exit(-1)

	main()
