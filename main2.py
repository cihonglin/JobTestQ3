#/usr/bin/python
# encoding: utf-8
from collections import Counter
from collections import defaultdict
from string import maketrans
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
		dictionary_dict[x] = 0
		i +=1

	return dictionary_dict

def doTranslate(inputStr,inTabStr,ouTabStr):
	trantab = maketrans(inTabStr + inTabStr.upper(), ouTabStr + ouTabStr.upper())
	return inputStr.translate(trantab);

#	dictionaryDictList 字典轉段列表
# 	questionCountList 問題列表
# 	dictionaryList 字典列表
#
def getKey(dictionaryDictList,questionCountList,dictionaryList): 
	dict_obj_list = {}
	key = {}
	not_key = {}
	trans_tab = {}
	#print not_in_key_list
	trans_tab['value'] = []#dictionaryDictList.values()
	trans_tab['key'] = []#dictionaryDictList.keys()

	ct = 0
	for show in dictionaryList:
		tmp_ques_list=[]
		unchk_char_list={}
		# 計算與字典完全相同字串 
		if show in questionCountList.keys():
			for char in show:
				if char not in trans_tab['value']:
					dictionaryDictList[char] = char
					trans_tab['key'].append(char)
					trans_tab['value'].append(char)
		else:
			#比對字典相同長度並唯一字串
			for dict_word in questionCountList:
				if len(dict_word) == len(show):
					tmp_ques_list.append(dict_word)
				
			dict_obj_list[show] = tmp_ques_list

			if len(tmp_ques_list) == 1 :
				key[show] = tmp_ques_list
			else:
				not_key[show] = tmp_ques_list
			  
	#將確定的字元寫入轉換表
	if len(key) > 1:
		for key_camp_list in key:
			i=0
			for key_camp_char in key_camp_list:
				if key_camp_char not in trans_tab['key']:
					dictionaryDictList[key_camp_char] = key[key_camp_list][0][i]
					trans_tab['key'].append(key_camp_char)
					trans_tab['value'].append(key[key_camp_list][0][i])
				i += 1

	#intab_str = "".join(trans_tab['value'])
	#outab_str = "".join(trans_tab['key'])				

	return {'dictionaryDictList':dictionaryDictList,'key':trans_tab['key'],'value':trans_tab['value']}

#取得包含重複字元的字串
def getMutliCharString(inputStringList): 
	mulie_char_string = []

	for input_string in inputStringList:

		if len(input_string) > len(Counter(input_string)) :
			mulie_char_string.append(input_string)
	return mulie_char_string

def getMutliCharKey():
	pass

def formatDictionaryDictList(dictionaryDictList):
	key = []
	value = []
	for index in dictionaryDictList:
		if dictionaryDictList[index] != 0:
			key.append(index)
			value.append(dictionaryDictList[index])

	return {'key':key,'value':value}



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


get_key_result = getKey(dictionary_dict_list,question_count_list,dictionary_list)

#print get_key_result.items()
#print get_key_result

intab_list = get_key_result['key']
outab_list = get_key_result['value']


intab_str = "".join(get_key_result['key'])
outab_str = "".join(get_key_result['value'])


ques_mutli_list = getMutliCharString(question_count_list)

dict_mutli_list = getMutliCharString(dictionary_list)

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
				dictionary_dict_list[str(ques_str[j])] = chk_char

				j+=1
		else:
			
			ct_ques_str = Counter(ques_str)
			ct_chk_str = Counter(chk_string)
			
			if(ct_ques_str.values() == ct_chk_str.values()):
				fa=fb=fc=fd=0
				#for 
				ctq_ch = ct_ques_str.most_common(1)[0][0]
				ctq_ct = ct_ques_str.most_common(1)[0][1]
				ccs_ch = ct_chk_str.most_common(1)[0][0]
				ccs_ct = ct_chk_str.most_common(1)[0][1]

				fa = ques_str.find(ctq_ch)
				fb = chk_string.find(ccs_ch)
				if( fa == fb):

					fc = ques_str.find(ctq_ch,(fa+1))+fa
					fd = chk_string.find(ccs_ch,(fb+1))+fb
					if(fc == fd):
						char_index_ct = 0
						for ques_str_char in ques_str:
							dictionary_dict_list[ques_str_char] = chk_string[char_index_ct]

							char_index_ct += 1

						dictionary_dict_list[ctq_ch] = ccs_ch

		i += 1


a = formatDictionaryDictList(dictionary_dict_list)

intab_string = "".join(a['key'])
outab_string = "".join(a['value'])

print intab_string
print outab_string


print question_str

print "\n**********************************\n"

print doTranslate(question_str,outab_string,intab_string)









