'''

-------------------------------------
| Programming Challenge: Mastermind |
-------------------------------------

Description:
Mastermind is a command line-based game. It generates 4 numbers randomly.
Player's mission is to guess what number that has been generated. The
program will show the total correct number, but it doesn't show which
number is correct. For example:

----Mastermind----
Guess the 4 numbers in as few tries as possible
1> 1442
*
2> 2443

3> 1321
*
4> 1214
**
5> 1134
****
Well done... That took you [5] attempts!

'''
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
	print("----Mastermind----")
	print("Guess the 4 numbers in as few tries as possible")
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