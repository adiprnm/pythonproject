from re import sub

def file_to_list(filename):
	result = ''
	f = open(filename, 'rU')
	for text in f:
		result += text
	f.close()
	result = result.replace('\n', ' ')
	result = sub("[^a-zA-Z ]", "", result)
	# print(repr(result))
	# hapustitik(result.split(' '))
	result = result.split(' ')
	
	new_list = []
	for word in result:
		word = word.lower()
		if word == " " or not word.isalpha():
			result.pop(result.index(word))		
		else:
			new_list.append(word)
	return new_list

def get_dicts(my_list):
	dicts = {}
	for element1 in my_list:
    	# check whether element1 is already in dicts keys
	    if element1 in dicts.keys():
	    	continue
	    else:
	    	count = my_list.count(element1)
	    	dicts[element1] = count
	return dicts