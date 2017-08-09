import sys

def print_usage():
	print("Usage: %s word1 word2" % sys.argv[0])

def is_anagram(a, b):
	a, b = sorted(list(a)), sorted(list(b))
	if a != b:
		return False
	return True

def main():
	if len(sys.argv) != 3:
		print_usage()
	else:
		print("Is anagram?", is_anagram(sys.argv[1], sys.argv[2]))

if __name__ == '__main__':
	main()
