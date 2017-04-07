'''
---------------------------------------------
| Programming Challenge: Average Calculator |
---------------------------------------------

Challenge source: http://usingpython.com/python-programming-challenges/
Description:
Just to clarify, you're not creating a mediocre calculator, but
a program for calculating averages.

The user should be able to enter a series of numbers, and the
program should print the average of these numbers. You can use
floating point number variables, or store the input in a list.

Your program might be used to calculate average temperatures
for a week, or a batting average for a cricket team, among others.
You could even expand the program to print the mean, median, and
mode averages.

'''

import math

def calculate(inputs, n):
	def mean():
		sum = 0
		for num in inputs:
			sum += num
		return sum/n
	def modus():
		unique = set(inputs)
		num_total = []
		for i in unique:
			num_total.append(inputs.count(i))
		maximum = max(num_total)
		modus = []
		for i in unique:
			if inputs.count(i) == maximum:
				modus.append(i)
		return set(modus)
			
	def median():
		sorted_nums = sorted(inputs)
		num_length = len(sorted_nums)
		
		if len(sorted_nums)%2 == 0:
			median = ((sorted_nums[int(num_length/2)-1]) + (sorted_nums[int(num_length/2)]))/2
		else:
			median = sorted_nums[math.floor(num_length/2)]
		return median
	
	print("\nThe average is", mean())
	print("The modus is", modus())
	print("The median is", median())

def main():
	n = int(input("Input total number you want to input: "))
	input_list = []
	for i in range(n):
		num = int(input("Number %s> " % str(i+1)))
		input_list.append(num)
		
	calculate(input_list, n)
		
if __name__ == '__main__':
	main()