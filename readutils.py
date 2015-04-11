#########################################################################################
#: a module housing text utilities to preprocess data
#: Author :Nitin Hardeniya 
#########################################################################################

import sys
import csv
from nltk.tokenize.regexp import RegexpTokenizer
import nltk
import re
from nltk import SnowballStemmer
stemmer = SnowballStemmer("english") 
import json
from pprint import pprint
import os



def loadstopwords(filename):
	
	""" loading the stopwords from a file and loading into a python list
		Returns a set of stopwords 
	"""
	stopwords = set( [line.strip().lower() for line in open(filename).readlines()] )
	return stopwords


def readreviews(filename,header=True, fieldsep="\t"):
	''' 
		Reads traing file for LDA 
		Parameters:
			- filename: input filename
			- header: True if the header line is present; False otherwise.
			- fieldsep: separator
		Return:
			- a list of entry (where each entry is a tuple of ID, list of tokens, sale/nosale).
	'''
	review_data = list()
	prevsid = ""
	#filehandle = open(filename, "r")
	stopwords = loadstopwords("english.stop.txt")

	
	pdsnotthere=0
	title_notthere=0
	tokenizer = RegexpTokenizer('[a-z]\w+')
	with open(filename, 'rU') as filename:
		filehandle = csv.reader(filename,delimiter='\t', quotechar='"')
		#print filehandle
		for line in filehandle:
			#lineparts = line.split(fieldsep)
			fields=line
			if header:
				header=False
				continue

			if len(fields)!=12:
				continue

			print len(fields)

			"""
			print len(fields)
			print fields
			"""
			HotelID=fields[0]
			hotelname=fields[1]
			HotelURL=fields[2]
			Address=fields[3]
			ImgURL=fields[4]
			Author=fields[5]
			Price=fields[6]
			location=fields[7]
			Title=fields[8]
			ReviewID=fields[9]
			Content=fields[10]
			Rating_ovarall=fields[11]

			review_content=Title+' '+Content
			review_discription=review_content

			words = [ token for token in tokenizer.tokenize(review_discription) if token not in stopwords ]
			review_data.append( words)

	return review_data

