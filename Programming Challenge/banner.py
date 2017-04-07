def cetak_banner(text):
	word_list = text.split(" ")
	
	def cetak_tepi(word_list):
		for word in word_list:
			for i in range(len(word)+4):
				print('*', end='')
			print('  ', end='')
		print("")
	
	def cetak_teks(word_list):
		for word in word_list:
			print('* %s *  ' % word, end='')
		print("")
	
	cetak_tepi(word_list)
	cetak_teks(word_list)
	cetak_tepi(word_list)

def main():
	text = input("Input the banner text: ")
	cetak_banner(text)
	
if __name__ == '__main__':
	main()