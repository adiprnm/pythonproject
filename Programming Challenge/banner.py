'''
---------------------------------
| Programming Challenge: Banner |
---------------------------------

Challenge source: http://usingpython.com/python-programming-challenges/
Description:
This challenge require the programmer to print the input
into a beautiful form, like banner. For example:

Input the banner text: Python is fun!

**********   ******   ********
* Python *   * is *   * fun! *
**********   ******   ********

'''

def print_banner(text):
	word_list = text.split(" ")
	
	def print_margin(word_list):
		for word in word_list:
			for i in range(len(word)+4):
				print('*', end='')
			print('  ', end='')
		print("")
	
	def print_text(word_list):
		for word in word_list:
			print('* %s *  ' % word, end='')
		print("")
	
	print_margin(word_list)
	print_text(word_list)
	print_margin(word_list)

def main():
	text = input("Input the banner text: ")
	print_banner(text)
	
if __name__ == '__main__':
	main()