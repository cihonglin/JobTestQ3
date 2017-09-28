#/usr/bin/python
# encoding: utf-8
from collections import Counter
from collections import defaultdict
import re


def string_process(input_string):
	input_string.splitlines()
	lower_string = input_string.lower();
	string_list = re.findall(r"[A-z]*",lower_string)
	string_list.sort()
	return_obj = []
	for i in string_list:
		if i != '':
			return_obj.append(i)
	return return_obj

def dictionary_dict():
	dictionary_dict = {}
	i=0
	while i < 26:
		x = chr(97+i)
		#print x
		dictionary_dict[x] = []
		i +=1

	return dictionary_dict

	

ques_str = '''Dtuma mu fj fqh pcqd wscux dxvmtd mu uctjv fjv umkxjax. Mhu acddcj xkxdxjhu fqx nmhas (wsmas ocgxqju dxkcvi fjv sfqdcji), qsihsd (fjv mhu fuucamfhxv acjaxnhu hxdnc, dxhxq, fjv fqhmatkfhmcj), vijfdmau, fjv hsx ucjma rtfkmhmxu cp hmdbqx fjv hxehtqx. Hsx wcqv vxqmgxu pqcd Oqxxz μουσική (dctumzx; "fqh cp hsx Dtuxu"). 

Hsx aqxfhmcj, nxqpcqdfjax, umojmpmafjax, fjv xgxj hsx vxpmjmhmcj cp dtuma gfqi faacqvmjo hc atkhtqx fjv ucamfk acjhxeh. Dtuma qfjoxu pqcd uhqmahki cqofjmlxv acdncumhmcju (fjv hsxmq qxaqxfhmcj mj nxqpcqdfjax), hsqctos mdnqcgmufhmcjfk dtuma hc fkxfhcqma pcqdu. Dtuma afj bx vmgmvxv mjhc oxjqxu fjv utboxjqxu, fkhsctos hsx vmgmvmjo kmjxu fjv qxkfhmcjusmnu bxhwxxj dtuma oxjqxu fqx cphxj utbhkx, ucdxhmdxu cnxj hc nxqucjfk mjhxqnqxhfhmcj, fjv caafumcjfkki acjhqcgxqumfk. Wmhsmj hsx fqhu, dtuma dfi bx akfuumpmxv fu f nxqpcqdmjo fqh, f pmjx fqh, fjv ftvmhcqi fqh. Mh dfi fkuc bx vmgmvxv fdcjo fqh dtuma fjv pckz dtuma. Hsxqx mu fkuc f uhqcjo acjjxahmcj bxhwxxj dtuma fjv dfhsxdfhmau. Dtuma dfi bx nkfixv fjv sxfqv kmgx, dfi bx nfqh cp f vqfdfhma wcqz cq pmkd, cq dfi bx qxacqvxv. 

Hc dfji nxcnkx mj dfji atkhtqxu, dtuma mu fj mdncqhfjh nfqh cp hsxmq wfi cp kmpx. Fjamxjh Oqxxz fjv Mjvmfj nsmkcucnsxqu vxpmjxv dtuma fu hcjxu cqvxqxv scqmlcjhfkki fu dxkcvmxu fjv gxqhmafkki fu sfqdcjmxu. Acddcj ufimjou utas fu "hsx sfqdcji cp hsx unsxqxu" fjv "mh mu dtuma hc di xfqu" ncmjh hc hsx jchmcj hsfh dtuma mu cphxj cqvxqxv fjv nkxfufjh hc kmuhxj hc. Scwxgxq, 20hs-axjhtqi acdncuxq Ycsj Afox hsctosh hsfh fji uctjv afj bx dtuma, ufimjo, pcq xefdnkx, "Hsxqx mu jc jcmux, cjki uctjv." Dtumackcomuh Yxfj-Yfartxu Jfhhmxl utddfqmlxu hsx qxkfhmgmuh, ncuh-dcvxqj gmxwncmjh: "Hsx bcqvxq bxhwxxj dtuma fjv jcmux mu fkwfiu atkhtqfkki vxpmjxv—wsmas mdnkmxu hsfh, xgxj wmhsmj f umjokx ucamxhi, hsmu bcqvxq vcxu jch fkwfiu nfuu hsqctos hsx ufdx nkfax; mj uscqh, hsxqx mu qfqxki f acjuxjutu ... Bi fkk faactjhu hsxqx mu jc umjokx fjv mjhxqatkhtqfk tjmgxqufk acjaxnh vxpmjmjo wsfh dtuma dmosh bx.'''


dict_str = '''a according accounts aleatoric all also although always among an ancient and any are art articulation arts as associated auditory be between border by cage can classified common composer compositions concept concepts connection consensus context controversial creation culturally culture cultures defined definedwhich defining definition derives divided dividing does dramatic dynamics ears elements even example film fine folk for form forms from genres governs greek harmonies harmony heard horizontally however implies important improvisational in indian intercultural interpretation into is it its jeanjacques john life lines listen live many mathematics may medium melodies melody meter might mousike muses music musicologist my nattiez no noise not notion occasionally of often only open or ordered organized part pass people performance performing personal philosophers pitch place played pleasant point postmodern qualities ranges rarely recorded recreation relationships relativist rhythm same saying sayings short significance silence single social society sometimes sonic sound spheres strictly strong subgenres subtle such summarizes tempo texture that thcentury the their there this thought through timbre to tones universal vary vertically viewpoint way what which whose within word work'''


#print "Question String => \n " + ques_str + "\n"

#print "Dictionary String => \n " + dict_str + "\n"

dictionary_dict_list = dictionary_dict()
#print dictionary_dict
question_list = string_process(ques_str)
#print question_list
question_count_list = Counter(question_list)

dictionary_list = string_process(dict_str)
#print dictionary_list


dict_obj_list = {}
unset_key = dictionary_dict()
key = {}

for show in dictionary_list:
	tmp_ques_list=[]
	for dict_word in question_count_list:
		if len(dict_word) == len(show):
			tmp_ques_list.append(dict_word)

	dict_obj_list[show] = tmp_ques_list

	if len(tmp_ques_list) == 1 :
		key[show] = tmp_ques_list
	else:
		for tmp_dict_word in tmp_ques_list:
			campare_index = 0
			for tmp_dict_char in tmp_dict_word:
				
				if not(tmp_dict_word[campare_index] in unset_key[show[campare_index]]) :
					unset_key[show[campare_index]].append(tmp_dict_word[campare_index])
				
				campare_index += 1

	

	#print "[ " +show + " ]  =>  " + ','.join(tmp_ques_list) + '\n'

#print key

for key_camp_list in key:
	#print camp_list + " => " 
	#print key[camp_list]
	i=0
	for key_camp_char in key_camp_list:
		dictionary_dict_list[key_camp_char] = key[key_camp_list][0][i]
		#print camp_char + "=>" +  key[camp_list][0][i]
		i += 1

print "dictionary dict list => "
print dictionary_dict_list
print "\n"
#print unset_key.values()

for x in unset_key:
	if dictionary_dict_list[x] != []:
		unset_key[x] = dictionary_dict_list[x]
	else:
		j=0
		for y in unset_key[x]:
			if dictionary_dict_list[y] != []:
				del unset_key[x][j]

			j += 1

print "unset key list => "
print unset_key
print "\n"

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

"""
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

