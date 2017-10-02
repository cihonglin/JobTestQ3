#/usr/bin/python
# encoding: utf-8
from string import maketrans
import time
import json

def openFile(fileName):
	fo = open(fileName,"r+")
	if(fo):
		print " open file "+fileName+"..."
		fc = fo.read()
		fo.close()
		return fc
	else:
		print fileName+" not exists"
		return False

def doTranslate(inputStr,inTabStr,ouTabStr):
	trantab = maketrans(inTabStr + inTabStr.upper(), ouTabStr + ouTabStr.upper())
	return inputStr.translate(trantab);

trans_string = openFile("translate.txt")
answer_string = openFile("answer.txt")


if(trans_string != False and answer_string != False):
	data = json.loads(trans_string)

	input_string = data['key']
	output_string = data['value']
	print "\n**********************************"
	print "*    encryption result string    *"
	print "**********************************\n"
	print doTranslate(answer_string,input_string,output_string)

	#now_time_format = time.strftime("%Y%m%d%H%M%S", time.localtime()) 