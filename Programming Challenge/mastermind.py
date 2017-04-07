import random

def create_random_number():
	nums = ''
	for i in range(4):
		nums += str(random.randint(0, 9))
	return nums
	
def check_input(guessed, actual):
	total_correct_num = 0
	index = 0
	for i in range(0, 4):
		if guessed[i] == actual[i]:
			total_correct_num += 1
				
	return total_correct_num

def process(random_num, turn):
	while True:
		turn += 1
		print("%d> " % turn, end='')
		guessed_num = input()
		number_correct = check_input(guessed_num, random_num)
		for i in range(number_correct):
			print('*', end='')
		print()
		if number_correct == 4:
			print("Well done! That took you [%d] attempts!" % turn)
			break
	
	
def main():
	turn = 0
	random_num = create_random_number()
	process(random_num, turn)

if __name__ == '__main__':
	main()