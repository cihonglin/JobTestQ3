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
		dictionary_dict[x] = []
		i +=1

	return dictionary_dict

def getKey(dictionaryDictList,questionCountList,dictionaryList):
	dict_obj_list = {}
	key = {}
	not_key = {}
	trans_tab = {}
	not_in_key_list = dictionaryDictList
	print not_in_key_list
	trans_tab['value'] = []#dictionaryDictList.values()
	trans_tab['key'] = []#dictionaryDictList.keys()
	"""
	if len(dictionaryDictList) > 0 :
		print "dict_keys"
		print dictionaryDictList.keys()
		
		print "dict_values"
		print dictionaryDictList.values()
	"""
	ct = 0
	for show in dictionaryList:
		tmp_ques_list=[]
		unchk_char_list={}
		#排除與字典完全相同字串 
		if show in questionCountList.keys():
			for char in show:
				if char not in trans_tab['key']:
					trans_tab['key'].append(char)
					trans_tab['vlaue'].append(char)
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
				dictionaryDictList[key_camp_char] = key[key_camp_list][0][i]
				if key_camp_char not in trans_tab['key']:
					trans_tab['key'].append(key_camp_char)
					trans_tab['value'].append(key[key_camp_list][0][i])
				i += 1
				#ct += 1

	#print not_key

	
	if len(not_key) > 1:
		for find_key_list in not_key: #saying 
			#temp_find_key_list = []
			#print not_key[find_key_list]
			#for find_key_char in find_key_list: #s
				#print find_key_char
			for chk_value in not_key[find_key_list]:
				#print "[%s] %s => %s " %(find_key_list, find_key_char,chk_value)
				temp_find_key_list = []
				j=0
				for chk_chr in find_key_list:
					if ( (chk_value[j] not in trans_tab['value']) 
						and ( chk_value[j] != find_key_list[j] ) 
						and (chk_value[j] not in not_in_key_list[find_key_list[j]]) ):
						if find_key_list == 'saying':
							print not_in_key_list[find_key_list[j]]
							print "find_key_list< %s > %d [%s] =>  chk_value < %s > [%s] " %(find_key_list , j, find_key_list[j] , chk_value, chk_value[j])
						#not_in_key_list[find_key_list[j]].append(chk_value[j])
					j+=1
					#print temp_find_key_list
				#not_in_key_list[find_key_list[j]] = temp_find_key_list
				

	#if ((find_key_char not in trans_tab['value']) and (find_key_char != find_key_list[0]) ):# and (find_key_list[0] not in not_in_key_list[find_key_char])):
	#	temp_find_key_list.append(find_key_list[0])
	#	#print find_key_char + " <> " + find_key_list[0]
	
	#not_in_key_list[find_key_char] = temp_find_key_list

	#print not_in_key_list
	return {'dictionaryDictList':dictionaryDictList,'intab':trans_tab['value'],'outab':trans_tab['key']}
	
def doTranslate(inputStr,inTabStr,ouTabStr):
	trantab = maketrans(inTabStr + inTabStr.upper(), ouTabStr + ouTabStr.upper())
	return inputStr.translate(trantab);


ques_str = '''Dtuma mu fj fqh pcqd wscux dxvmtd mu uctjv fjv umkxjax. Mhu acddcj xkxdxjhu fqx nmhas (wsmas ocgxqju dxkcvi fjv sfqdcji), qsihsd (fjv mhu fuucamfhxv acjaxnhu hxdnc, dxhxq, fjv fqhmatkfhmcj), vijfdmau, fjv hsx ucjma rtfkmhmxu cp hmdbqx fjv hxehtqx. Hsx wcqv vxqmgxu pqcd Oqxxz μουσική (dctumzx; "fqh cp hsx Dtuxu"). 

Hsx aqxfhmcj, nxqpcqdfjax, umojmpmafjax, fjv xgxj hsx vxpmjmhmcj cp dtuma gfqi faacqvmjo hc atkhtqx fjv ucamfk acjhxeh. Dtuma qfjoxu pqcd uhqmahki cqofjmlxv acdncumhmcju (fjv hsxmq qxaqxfhmcj mj nxqpcqdfjax), hsqctos mdnqcgmufhmcjfk dtuma hc fkxfhcqma pcqdu. Dtuma afj bx vmgmvxv mjhc oxjqxu fjv utboxjqxu, fkhsctos hsx vmgmvmjo kmjxu fjv qxkfhmcjusmnu bxhwxxj dtuma oxjqxu fqx cphxj utbhkx, ucdxhmdxu cnxj hc nxqucjfk mjhxqnqxhfhmcj, fjv caafumcjfkki acjhqcgxqumfk. Wmhsmj hsx fqhu, dtuma dfi bx akfuumpmxv fu f nxqpcqdmjo fqh, f pmjx fqh, fjv ftvmhcqi fqh. Mh dfi fkuc bx vmgmvxv fdcjo fqh dtuma fjv pckz dtuma. Hsxqx mu fkuc f uhqcjo acjjxahmcj bxhwxxj dtuma fjv dfhsxdfhmau. Dtuma dfi bx nkfixv fjv sxfqv kmgx, dfi bx nfqh cp f vqfdfhma wcqz cq pmkd, cq dfi bx qxacqvxv. 

Hc dfji nxcnkx mj dfji atkhtqxu, dtuma mu fj mdncqhfjh nfqh cp hsxmq wfi cp kmpx. Fjamxjh Oqxxz fjv Mjvmfj nsmkcucnsxqu vxpmjxv dtuma fu hcjxu cqvxqxv scqmlcjhfkki fu dxkcvmxu fjv gxqhmafkki fu sfqdcjmxu. Acddcj ufimjou utas fu "hsx sfqdcji cp hsx unsxqxu" fjv "mh mu dtuma hc di xfqu" ncmjh hc hsx jchmcj hsfh dtuma mu cphxj cqvxqxv fjv nkxfufjh hc kmuhxj hc. Scwxgxq, 20hs-axjhtqi acdncuxq Ycsj Afox hsctosh hsfh fji uctjv afj bx dtuma, ufimjo, pcq xefdnkx, "Hsxqx mu jc jcmux, cjki uctjv." Dtumackcomuh Yxfj-Yfartxu Jfhhmxl utddfqmlxu hsx qxkfhmgmuh, ncuh-dcvxqj gmxwncmjh: "Hsx bcqvxq bxhwxxj dtuma fjv jcmux mu fkwfiu atkhtqfkki vxpmjxv—wsmas mdnkmxu hsfh, xgxj wmhsmj f umjokx ucamxhi, hsmu bcqvxq vcxu jch fkwfiu nfuu hsqctos hsx ufdx nkfax; mj uscqh, hsxqx mu qfqxki f acjuxjutu ... Bi fkk faactjhu hsxqx mu jc umjokx fjv mjhxqatkhtqfk tjmgxqufk acjaxnh vxpmjmjo wsfh dtuma dmosh bx.'''

dict_str = '''a according accounts aleatoric all also although always among an ancient and any are art articulation arts as associated auditory be between border by cage can classified common composer compositions concept concepts connection consensus context controversial creation culturally culture cultures defined definedwhich defining definition derives divided dividing does dramatic dynamics ears elements even example film fine folk for form forms from genres governs greek harmonies harmony heard horizontally however implies important improvisational in indian intercultural interpretation into is it its jeanjacques john life lines listen live many mathematics may medium melodies melody meter might mousike muses music musicologist my nattiez no noise not notion occasionally of often only open or ordered organized part pass people performance performing personal philosophers pitch place played pleasant point postmodern qualities ranges rarely recorded recreation relationships relativist rhythm same saying sayings short significance silence single social society sometimes sonic sound spheres strictly strong subgenres subtle such summarizes tempo texture that thcentury the their there this thought through timbre to tones universal vary vertically viewpoint way what which whose within word work'''

#print "Question String => \n " + ques_str + "\n"
#print "Dictionary String => \n " + dict_str + "\n"

dictionary_dict_list = dictionaryDict() #dictionaryDictList
#print dictionary_dict
question_list = stringProcess(ques_str) #questionList
#print question_list
question_count_list = Counter(question_list) #questionCountList
#print question_count_list.keys()
dictionary_list = stringProcess(dict_str) #dictionaryList
#print dictionary_list


get_key_result = getKey(dictionary_dict_list,question_count_list,dictionary_list)

#print get_key_result.items()
#print get_key_result


intab_str = "".join(get_key_result['intab'])
outab_str = "".join(get_key_result['outab'])

translate_result = doTranslate(ques_str,intab_str,outab_str)

#question_list2 = stringProcess(translate_result)

#question_count_list2 = Counter(question_list2)

#get_key_result2 = getKey(get_key_result['dictionaryDictList'],question_list2,question_count_list2,dictionary_list)

#print get_key_result2.items()

"""
print "dictionary dict list keys => "
print get_key_result['dictionaryDictList'].keys()
print "dictionary dict list values => "
print get_key_result['dictionaryDictList'].values()
print "intab string => "
print intab_str
print "out tab string => "
print outab_str
print "\n"
"""
#print translate_result

#print unset_key.values()

"""
for x in unset_key:
	if dictionary_dict_list[x] != []:
		unset_key[x] = dictionary_dict_list[x]
	else:
		j=0
		for y in unset_key[x]:
			if dictionary_dict_list[y] != []:
				del unset_key[x][j]

			j += 1
			
======================================
#print "unset key list => "
#print unset_key
#print "\n"

	#print "[ " +x + " ]  =>  " + ','.join(unset_key[x]) + '\n'

#for x in unset_key:
	#if dictionary_dict_list[x] != []:
		#unset_key[x] = dictionary_dict_list[x]
		#del unset_key
	#else:
		#for chk_key in unset_key[x]:
			#print chk_key
			#if dictionary_dict_list[chk_key] != [] :
				#print unset_key[x]
				#print dictionary_dict_list[chk_key]
				#print chk_key + " =>" 
	
#print unset_key

#print dictionary_dict_list

#for dict_obj_item in dict_obj_list




#print var_obj


var_obj = {}
for show in question_count_list:
	if show != '':
		tmp_ques_list=[]
		for dict_word in dictionary_list:
			if len(dict_word) == len(show):
				tmp_ques_list.append(dict_word)

		var_obj[show] = tmp_ques_list
		#print "[ " +show + " ]  =>  " + ','.join(tmp_ques_list) + '\n'
		
#print "[ " + str(var_obj['dtuma']) + " ] " 

#print var_obj
for question_count_item in question_count_list.most_common(): 
	if(question_count_item[0] != ''):
		#print var_obj['dtuma']
		for compare_str in var_obj[question_count_item[0]]:
			#if question_count_item[0] == 'dtuma':
			#	print question_count_item[0] + '=>' + compare_str
			campare_index = 0
			tmp_dictionary_dict = []
			for campare_char in question_count_item[0]:
				#tmp_dictionary_dict = dictionary_dict[campare_char]
				#if campare_char ==  'd':
					#print question_count_item[0] + " <> " + compare_str + " => " + campare_char + " <> " + compare_str[campare_index]
				if not(compare_str[campare_index] in dictionary_dict[campare_char]) :
					dictionary_dict[campare_char].append(compare_str[campare_index])

					#if campare_char ==  'd':
					#	print compare_str[campare_index]
				campare_index += 1

			dictionary_dict[campare_char].sort()
			#dictionary_dict[campare_char] = tmp_dictionary_dict
"""
#for char in dictionary_dict:
	#print char + " =>" + ','.join(dictionary_dict[char])


	#print 

