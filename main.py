#/usr/bin/python
# encoding: utf-8
from collections import Counter
from collections import defaultdict
from string import maketrans
import difflib
import re

#字串處理
def stringProcess(inputString):
	inputString.splitlines()
	lower_string = inputString.lower();
	string_list = re.findall(r"[A-z]*",lower_string)
	string_list.sort()
	
	return_obj = []
	for i in string_list:
		if i != '':
			return_obj.append(i)
	return return_obj

def dictionaryDict():
	dictionary_dict = {}
	i=0
	while i < 26:
		x = chr(97+i)
		#print x
		dictionary_dict[x] = '*'
		i +=1

	return dictionary_dict

def doTranslate(inputStr,inTabStr,ouTabStr):
	trantab = maketrans(inTabStr + inTabStr.upper(), ouTabStr + ouTabStr.upper())
	return inputStr.translate(trantab);


def getTransString(dictionaryDictList):
	key_string = "".join(dictionaryDictList.keys())
	val_string = "".join(dictionaryDictList.values())

	return {'key':key_string,'value':val_string}

#	從唯一並同樣長度字元 取得對照表
#	dictionaryDictList 字典轉段列表
# 	questionCountList 問題列表
# 	dictionaryList 字典列表
#
def getKey(dictionaryDictList,questionCountList,dictionaryList): 
	#dict_obj_list = {}
	key = {}
	not_key = {}

	ct = 0
	for dict_string in dictionaryList:
		tmp_ques_list=[]
		unchk_char_list={}
		# 計算與字典完全相同字串 
		if dict_string in questionCountList.keys():
			for char in dict_string:
				if char not in dictionaryDictList.values():
					dictionaryDictList[char] = char
		else:
			#比對字典相同長度並唯一字串
			for dict_word in questionCountList:
				if len(dict_word) == len(dict_string):
					tmp_ques_list.append(dict_word)
				
			#dict_obj_list[dict_string] = tmp_ques_list

			if len(tmp_ques_list) == 1 :
				key[dict_string] = tmp_ques_list
			else:
				not_key[dict_string] = tmp_ques_list
			  
	#將確定的字元寫入轉換表
	if len(key) > 1:
		for key_camp_list in key:
			i=0
			for key_camp_char in key_camp_list:
				if key[key_camp_list][0][i] not in dictionaryDictList.values():
					dictionaryDictList[key_camp_char] = key[key_camp_list][0][i]
				i += 1

	return dictionaryDictList

#取得包含重複字元的字串
def getMutliCharString(inputStringList): 
	mulie_char_string = []

	for input_string in inputStringList:

		if len(input_string) > len(Counter(input_string)) :
			mulie_char_string.append(input_string)
	return mulie_char_string

# 比對字典檔與翻譯文檔 包含重複字元字串
#	dictionaryDictList 字典轉段列表
# 	questionCountList 問題列表
# 	dictionaryList 字典列表
def getMutliCharKey(dictionaryDictList,questionCountList,dictionaryList):

	intab_str = "".join(dictionaryDictList.keys())
	outab_str = "".join(dictionaryDictList.values())

	ques_mutli_list = getMutliCharString(questionCountList)
	dict_mutli_list = getMutliCharString(dictionaryList)

	ques_mutli_ct_list = {}
	for dict_mutli_string in dict_mutli_list:
		tmp_ct_list = []
		for ques_mutli_string in ques_mutli_list:
			if len(ques_mutli_string) == len(dict_mutli_string):
				tmp_ct_list.append(ques_mutli_string)

		ques_mutli_ct_list[dict_mutli_string] = tmp_ct_list

	for ques_str in ques_mutli_ct_list:

		i = 0
		for chk_string in ques_mutli_ct_list[ques_str]:
			trans_chk_string = doTranslate(chk_string,outab_str,intab_str)
			if(trans_chk_string == ques_str):
				j=0
				for chk_char in chk_string:
					if chk_char not in dictionaryDictList.values():
						dictionaryDictList[str(ques_str[j])] = chk_char

					j+=1
			else:

				ct_ques_str = Counter(ques_str)
				ct_chk_str = Counter(chk_string)
				#if(ct_ques_str.values() == ct_chk_str.values()):

				fa=fb=fc=fd=0
				ctq_ch = ct_ques_str.most_common(1)[0][0] #char 
				ctq_ct = ct_ques_str.most_common(1)[0][1] #nums

				ccs_ch = ct_chk_str.most_common(1)[0][0] #char
				ccs_ct = ct_chk_str.most_common(1)[0][1] #nums				

				fa = ques_str.find(ctq_ch)
				fb = chk_string.find(ccs_ch)
				if( fa == fb ):

					fc = ques_str.find(ctq_ch,(fa+1))
					fd = chk_string.find(ccs_ch,(fb+1))

					if(fc == fd):
						char_index_ct = 0
						for ques_str_char in ques_str:
							if chk_string[char_index_ct] not in dictionaryDictList.values():
								dictionaryDictList[ques_str_char] = chk_string[char_index_ct]

							char_index_ct += 1
						#if ccs_ch not in dictionaryDictList.values():
						#	dictionaryDictList[ctq_ch] = ccs_ch

			i += 1
	return dictionaryDictList

# 相似字比對
#	dictionaryDictList 字典轉段列表
def getCharInSimilarString(dictionaryDictList):
	translate_string = getTransString(dictionaryDictList)
	intab_string = translate_string['key']
	outab_string = translate_string['value']

	unlocate_input = []
	unlocate_output = []
	i=0
	for index in dictionaryDictList:
		x = chr(97+i)
		if x not in dictionaryDictList.values():
			unlocate_input.append(x)

		if dictionaryDictList[index] == '*':
			unlocate_output.append(index)
		i +=1

	unlocate_input_mark = len(unlocate_output)*'*'	

	sub_trans_list = []
	for char in unlocate_input:
		print "char : " + char 
	 	for words in question_count_list.keys():
	 		if words.find(char) != -1:
	 			sub_trans_list.append(words)

	dict_trans_list = {}
	for xi in sub_trans_list:
		trans_string = doTranslate(xi,outab_string+"".join(unlocate_input),intab_string+unlocate_input_mark)
		dict_trans_list[trans_string] = xi
	pre_translate_string = ",".join(dict_trans_list.keys())
	pre_translate_list = pre_translate_string.replace("*","[A-z]").split(",")
	pre_trans_list = {}

	for pre_trans_str in pre_translate_list:
		key = dict_trans_list[pre_trans_str.replace("[A-z]","*")]
		pre_trans_list[key] = re.findall(pre_trans_str,dict_str)

	for reverse_string in pre_trans_list:
		if len(pre_trans_list[reverse_string]) == 1:
			i=0
			for reverse_char in pre_trans_list[reverse_string][0]:
				if reverse_string[i] not in dictionaryDictList.values():
					dictionaryDictList[reverse_char[i]] = reverse_string[i]
					i+=1

	return dictionaryDictList


question_str = '''Dtuma mu fj fqh pcqd wscux dxvmtd mu uctjv fjv umkxjax. Mhu acddcj xkxdxjhu fqx nmhas (wsmas ocgxqju dxkcvi fjv sfqdcji), qsihsd (fjv mhu fuucamfhxv acjaxnhu hxdnc, dxhxq, fjv fqhmatkfhmcj), vijfdmau, fjv hsx ucjma rtfkmhmxu cp hmdbqx fjv hxehtqx. Hsx wcqv vxqmgxu pqcd Oqxxz μουσική (dctumzx; "fqh cp hsx Dtuxu"). 

Hsx aqxfhmcj, nxqpcqdfjax, umojmpmafjax, fjv xgxj hsx vxpmjmhmcj cp dtuma gfqi faacqvmjo hc atkhtqx fjv ucamfk acjhxeh. Dtuma qfjoxu pqcd uhqmahki cqofjmlxv acdncumhmcju (fjv hsxmq qxaqxfhmcj mj nxqpcqdfjax), hsqctos mdnqcgmufhmcjfk dtuma hc fkxfhcqma pcqdu. Dtuma afj bx vmgmvxv mjhc oxjqxu fjv utboxjqxu, fkhsctos hsx vmgmvmjo kmjxu fjv qxkfhmcjusmnu bxhwxxj dtuma oxjqxu fqx cphxj utbhkx, ucdxhmdxu cnxj hc nxqucjfk mjhxqnqxhfhmcj, fjv caafumcjfkki acjhqcgxqumfk. Wmhsmj hsx fqhu, dtuma dfi bx akfuumpmxv fu f nxqpcqdmjo fqh, f pmjx fqh, fjv ftvmhcqi fqh. Mh dfi fkuc bx vmgmvxv fdcjo fqh dtuma fjv pckz dtuma. Hsxqx mu fkuc f uhqcjo acjjxahmcj bxhwxxj dtuma fjv dfhsxdfhmau. Dtuma dfi bx nkfixv fjv sxfqv kmgx, dfi bx nfqh cp f vqfdfhma wcqz cq pmkd, cq dfi bx qxacqvxv. 

Hc dfji nxcnkx mj dfji atkhtqxu, dtuma mu fj mdncqhfjh nfqh cp hsxmq wfi cp kmpx. Fjamxjh Oqxxz fjv Mjvmfj nsmkcucnsxqu vxpmjxv dtuma fu hcjxu cqvxqxv scqmlcjhfkki fu dxkcvmxu fjv gxqhmafkki fu sfqdcjmxu. Acddcj ufimjou utas fu "hsx sfqdcji cp hsx unsxqxu" fjv "mh mu dtuma hc di xfqu" ncmjh hc hsx jchmcj hsfh dtuma mu cphxj cqvxqxv fjv nkxfufjh hc kmuhxj hc. Scwxgxq, 20hs-axjhtqi acdncuxq Ycsj Afox hsctosh hsfh fji uctjv afj bx dtuma, ufimjo, pcq xefdnkx, "Hsxqx mu jc jcmux, cjki uctjv." Dtumackcomuh Yxfj-Yfartxu Jfhhmxl utddfqmlxu hsx qxkfhmgmuh, ncuh-dcvxqj gmxwncmjh: "Hsx bcqvxq bxhwxxj dtuma fjv jcmux mu fkwfiu atkhtqfkki vxpmjxv—wsmas mdnkmxu hsfh, xgxj wmhsmj f umjokx ucamxhi, hsmu bcqvxq vcxu jch fkwfiu nfuu hsqctos hsx ufdx nkfax; mj uscqh, hsxqx mu qfqxki f acjuxjutu ... Bi fkk faactjhu hsxqx mu jc umjokx fjv mjhxqatkhtqfk tjmgxqufk acjaxnh vxpmjmjo wsfh dtuma dmosh bx.'''

dict_str = '''a according accounts aleatoric all also although always among an ancient and any are art articulation arts as associated auditory be between border by cage can classified common composer compositions concept concepts connection consensus context controversial creation culturally culture cultures defined definedwhich defining definition derives divided dividing does dramatic dynamics ears elements even example film fine folk for form forms from genres governs greek harmonies harmony heard horizontally however implies important improvisational in indian intercultural interpretation into is it its jeanjacques john life lines listen live many mathematics may medium melodies melody meter might mousike muses music musicologist my nattiez no noise not notion occasionally of often only open or ordered organized part pass people performance performing personal philosophers pitch place played pleasant point postmodern qualities ranges rarely recorded recreation relationships relativist rhythm same saying sayings short significance silence single social society sometimes sonic sound spheres strictly strong subgenres subtle such summarizes tempo texture that thcentury the their there this thought through timbre to tones universal vary vertically viewpoint way what which whose within word work'''

#print "Question String => \n " + ques_str + "\n"
#print "Dictionary String => \n " + dict_str + "\n"

dictionary_dict_list = dictionaryDict() #dictionaryDictList
#print dictionary_dict
question_list = stringProcess(question_str) #questionList
#print question_list
question_count_list = Counter(question_list) #questionCountList
#print question_count_list.keys()
dictionary_list = stringProcess(dict_str) #dictionaryList
#print dictionary_list

#step 1
dictionary_dict_list = getKey(dictionary_dict_list,question_count_list,dictionary_list)

#print "".join(dictionary_dict_list.keys())
#print "".join(dictionary_dict_list.values())

#step 2
dictionary_dict_list = getMutliCharKey(dictionary_dict_list,question_count_list,dictionary_list)

#step3
dictionary_dict_list = getCharInSimilarString(dictionary_dict_list)


translate_string = getTransString(dictionary_dict_list)
intab_string = translate_string['key']
outab_string = translate_string['value']
trans_result = doTranslate(question_str,outab_string,intab_string)


print "\n**********************************"
print "*          input strings         *"
print "**********************************\n"
print question_str

print "\n**********************************"
print "*       translate char list      *"
print "**********************************\n"
print " input: "+" ".join(dictionary_dict_list.keys())
print "output: "+" ".join(dictionary_dict_list.values())

print "\n**********************************"
print "*    translate result string     *"
print "**********************************\n"
print trans_result



