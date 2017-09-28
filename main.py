#/usr/bin/python
# encoding: utf-8
from collections import Counter
import re


def string_process(input_string):
	input_string.splitlines()
	lower_string = input_string.lower();
	string_list = re.findall(r"[a-z]*",lower_string)
	string_list.sort()
	return string_list

ques_str = '''Dtuma mu fj fqh pcqd wscux dxvmtd mu uctjv fjv umkxjax. Mhu acddcj xkxdxjhu fqx nmhas (wsmas ocgxqju dxkcvi fjv sfqdcji), qsihsd (fjv mhu fuucamfhxv acjaxnhu hxdnc, dxhxq, fjv fqhmatkfhmcj), vijfdmau, fjv hsx ucjma rtfkmhmxu cp hmdbqx fjv hxehtqx. Hsx wcqv vxqmgxu pqcd Oqxxz μουσική (dctumzx; "fqh cp hsx Dtuxu"). 

Hsx aqxfhmcj, nxqpcqdfjax, umojmpmafjax, fjv xgxj hsx vxpmjmhmcj cp dtuma gfqi faacqvmjo hc atkhtqx fjv ucamfk acjhxeh. Dtuma qfjoxu pqcd uhqmahki cqofjmlxv acdncumhmcju (fjv hsxmq qxaqxfhmcj mj nxqpcqdfjax), hsqctos mdnqcgmufhmcjfk dtuma hc fkxfhcqma pcqdu. Dtuma afj bx vmgmvxv mjhc oxjqxu fjv utboxjqxu, fkhsctos hsx vmgmvmjo kmjxu fjv qxkfhmcjusmnu bxhwxxj dtuma oxjqxu fqx cphxj utbhkx, ucdxhmdxu cnxj hc nxqucjfk mjhxqnqxhfhmcj, fjv caafumcjfkki acjhqcgxqumfk. Wmhsmj hsx fqhu, dtuma dfi bx akfuumpmxv fu f nxqpcqdmjo fqh, f pmjx fqh, fjv ftvmhcqi fqh. Mh dfi fkuc bx vmgmvxv fdcjo fqh dtuma fjv pckz dtuma. Hsxqx mu fkuc f uhqcjo acjjxahmcj bxhwxxj dtuma fjv dfhsxdfhmau. Dtuma dfi bx nkfixv fjv sxfqv kmgx, dfi bx nfqh cp f vqfdfhma wcqz cq pmkd, cq dfi bx qxacqvxv. 

Hc dfji nxcnkx mj dfji atkhtqxu, dtuma mu fj mdncqhfjh nfqh cp hsxmq wfi cp kmpx. Fjamxjh Oqxxz fjv Mjvmfj nsmkcucnsxqu vxpmjxv dtuma fu hcjxu cqvxqxv scqmlcjhfkki fu dxkcvmxu fjv gxqhmafkki fu sfqdcjmxu. Acddcj ufimjou utas fu "hsx sfqdcji cp hsx unsxqxu" fjv "mh mu dtuma hc di xfqu" ncmjh hc hsx jchmcj hsfh dtuma mu cphxj cqvxqxv fjv nkxfufjh hc kmuhxj hc. Scwxgxq, 20hs-axjhtqi acdncuxq Ycsj Afox hsctosh hsfh fji uctjv afj bx dtuma, ufimjo, pcq xefdnkx, "Hsxqx mu jc jcmux, cjki uctjv." Dtumackcomuh Yxfj-Yfartxu Jfhhmxl utddfqmlxu hsx qxkfhmgmuh, ncuh-dcvxqj gmxwncmjh: "Hsx bcqvxq bxhwxxj dtuma fjv jcmux mu fkwfiu atkhtqfkki vxpmjxv—wsmas mdnkmxu hsfh, xgxj wmhsmj f umjokx ucamxhi, hsmu bcqvxq vcxu jch fkwfiu nfuu hsqctos hsx ufdx nkfax; mj uscqh, hsxqx mu qfqxki f acjuxjutu ... Bi fkk faactjhu hsxqx mu jc umjokx fjv mjhxqatkhtqfk tjmgxqufk acjaxnh vxpmjmjo wsfh dtuma dmosh bx.'''


dict_str = '''a according accounts aleatoric all also although always among an ancient and any are art articulation arts as associated auditory be between border by cage can classified common composer compositions concept concepts connection consensus context controversial creation culturally culture cultures defined definedwhich defining definition derives divided dividing does dramatic dynamics ears elements even example film fine folk for form forms from genres governs greek harmonies harmony heard horizontally however implies important improvisational in indian intercultural interpretation into is it its jeanjacques john life lines listen live many mathematics may medium melodies melody meter might mousike muses music musicologist my nattiez no noise not notion occasionally of often only open or ordered organized part pass people performance performing personal philosophers pitch place played pleasant point postmodern qualities ranges rarely recorded recreation relationships relativist rhythm same saying sayings short significance silence single social society sometimes sonic sound spheres strictly strong subgenres subtle such summarizes tempo texture that thcentury the their there this thought through timbre to tones universal vary vertically viewpoint way what which whose within word work'''


#print "Question String => \n " + ques_str + "\n"

#print "Dictionary String => \n " + dict_str + "\n"

#dictionary_dict = {'a':'a','b':'b','c':'c','d':'d','e':'e','f':'f','g':'g','h':'h','i':'i','j':'j','k':'k','l':'l','m':'m','n':'n','o':'o','p':'p','q':'q','r':'r','s':'s','t':'t','u':'u','v':'v','w':'w','x':'x','y':'y','z':'z'}



dictionary_dict = {}
i=0
while i < 26:
	x = chr(97+i)
	print x
	dictionary_dict[x] = []
	i +=1


#print dictionary_dict


question_list = string_process(ques_str)
#print question_list

question_count_list = Counter(question_list)

dictionary_list = string_process(dict_str)

#print dictionary_list

#print question_list_count

#print question_count_list.most_common()

var_obj = {}

for show in question_count_list:
	if show != '':
		tmp_dict_list=[]
		for dict_word in dictionary_list:
			if len(dict_word) == len(show):
				tmp_dict_list.append(dict_word)

		var_obj[show] = tmp_dict_list
				#print show +" -> "+ dict_word
#for aa in var_obj:
#	print aa

#print var_obj['fjv'];

for question_count_item in question_count_list.most_common():
	if(question_count_item[0] != ''):
		#print var_obj[question_count_item[0]]
		for compare_str in var_obj[question_count_item[0]]:
			print question_count_item[0] + '=>' + compare_str
			campare_index = 0
			for campare_char in question_count_item[0]:
				#print campare_char + " => " + compare_str[campare_index]

				campare_index += 1



	#print show + " => " + str(question_list_count[show])
"""

process_question_dict = {}

process_question_dict_item = {}
question_quesion_count_list = {1:[]}


for string_obj in question_list:
	if process_question_dict.has_key(string_obj):
		process_question_dict[string_obj] += 1
		#print "pass"
	else:
		#process_question_dict_item = {'string':string_obj,'count':1}
		process_question_dict[string_obj]  = 1
"""

#print process_question_dict

#for question_word in process_question_dict:

#	question_quesion_count_list[process_question_dict[question_word]] = temp_obj
	#print  question_word + "=>" + str(process_question_dict[question_word])

#print question_quesion_count_list

#Cid = dict((v, k) for k, v in process_question_dict.iteritems())



#print question_list
#print dict_list


#lower_dict_string = dict_str.lower();

#dict_list = lower_dict_string.split(' ')

#print dictionary_dict