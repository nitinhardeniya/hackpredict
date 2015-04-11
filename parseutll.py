
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




def parsereviews(indir,outfile):
	''' 
		Reads review_data file for LDA 
		Parameters:
			- filename: input filename
			- header: True if the header line is present; False otherwise.
			- fieldsep: separator
		Return:
			- a list of entry (where each entry is a tuple of ID, list of tokens, sale/nosale).
	'''
	review_data = list()
	prevsid = ""
	tokenizer = RegexpTokenizer('[a-z]\w+')
	ignorelines=0
	totalline=0
	fo=open(outfile,'a')
	outfile='Reviews_'
	fohigh=open(outfile+'high.csv','a')
	foverybad=open(outfile+'verybad.csv','a')
	fobad=open(outfile+'bad.csv','a')
	fomed=open(outfile+'med.csv','a')

	for path, subdirs, files in os.walk(indir):
		for filename in files:
			fabspath = os.path.join(path, filename)
			with open(fabspath) as data_file:  
				try:  
					data = json.load(data_file)
					reviews_list= data["Reviews"]
					hotelinfo= data["HotelInfo"]
					hotelname=hotelinfo['Name'].encode('ascii', 'ignore')
					HotelURL=hotelinfo['HotelURL'].encode('ascii', 'ignore')
					Price=hotelinfo['Price'].encode('ascii', 'ignore')
					Address=hotelinfo['Address'].encode('ascii', 'ignore')
					HotelID=hotelinfo['HotelID'].encode('ascii', 'ignore')
					ImgURL=hotelinfo['ImgURL'].encode('ascii', 'ignore')
					for rev in reviews_list:
						ratings=rev['Ratings']
						location=rev['AuthorLocation'].encode('ascii', 'ignore')
						Title=rev['Title'].encode('ascii', 'ignore')
						Author=rev['Author'].encode('ascii', 'ignore')
						ReviewID=rev['ReviewID'].encode('ascii', 'ignore')
						Content=rev['Content'].encode('ascii', 'ignore')
						Ratings=rev['Ratings']
						#print Ratings
						#Cleanliness	Overall	Service	Value	Rooms
						#print HotelID+'\t'+Author+'\t'+Title+'\t'+ReviewID+'\t'+Content+'\t'+Ratings['Overall']
						#print type(Ratings['Overall'])
						totalline+=1
						fo.write(HotelID+'\t'+hotelname+'\t'+HotelURL+'\t'+Address+'\t'+ImgURL+'\t'+Author+'\t'+Price+'\t'+location+'\t'+Title+'\t'+ReviewID+'\t'+Content+'\t'+str(Ratings['Overall'])+'\n')			
						if Ratings['Overall'] in ['5.0','4.0']:
							fohigh.write(HotelID+'\t'+hotelname+'\t'+HotelURL+'\t'+Address+'\t'+ImgURL+'\t'+Author+'\t'+Price+'\t'+location+'\t'+Title+'\t'+ReviewID+'\t'+Content+'\t'+str(Ratings['Overall'])+'\n')
						elif Ratings['Overall'] in ['0.0']:
							foverybad.write(HotelID+'\t'+hotelname+'\t'+HotelURL+'\t'+Address+'\t'+ImgURL+'\t'+Author+'\t'+Price+'\t'+location+'\t'+Title+'\t'+ReviewID+'\t'+Content+'\t'+str(Ratings['Overall'])+'\n')
						elif Ratings['Overall'] in ['1.0','2.0']:
							fobad.write(HotelID+'\t'+hotelname+'\t'+HotelURL+'\t'+Address+'\t'+ImgURL+'\t'+Author+'\t'+Price+'\t'+location+'\t'+Title+'\t'+ReviewID+'\t'+Content+'\t'+str(Ratings['Overall'])+'\n')
						else:
							fomed.write(HotelID+'\t'+hotelname+'\t'+HotelURL+'\t'+Address+'\t'+ImgURL+'\t'+Author+'\t'+Price+'\t'+location+'\t'+Title+'\t'+ReviewID+'\t'+Content+'\t'+str(Ratings['Overall'])+'\n')
						
				except:
						ignorelines+=1
						print 'error'

	print totalline
	print ignorelines

if __name__ == '__main__':
	parsereviews(indir=sys.argv[1],outfile=sys.argv[2])
