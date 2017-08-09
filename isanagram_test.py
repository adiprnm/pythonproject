from isanagram import is_anagram

def test_isanagram():
	word1_list = ['', 'abba', 'kasur', 'hobbah', 'bala', 'nukt..uk', 'kawan', 'mantap']
	word2_list = ['', 'baba', 'sukarfdas', 'abohbh', 'abal', 'kuktun', 'naack!', 'tampan']
	expected = [True, True, False, True, True, False, False, True]
	for i in range(len(word1_list)):
		reality = is_anagram(word1_list[i], word2_list[i])
		if reality == expected[i]:
			print("Test %d: passed" % (i+1))
		else:
			print("Error on test %d: expected %s, got %s" % ((i+1), expected[i], reality))

test_isanagram()