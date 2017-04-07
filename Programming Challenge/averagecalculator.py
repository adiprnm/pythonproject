def calculate(inputs, n):
	def mean():
		sum = 0
		for num in inputs:
			sum += num
		return sum/n
	def modus():
		inputs = sorted(inputs)
		
	def median():
	
	return mean()

def main():
	n = int(input("Input total number you want to input: "))
	input_list = []
	for i in range(n):
		num = int(input("Number %s> " % str(i+1)))
		input_list.append(num)
		
	print("The average is", calculate(input_list, n))
		
if __name__ == '__main__':
	main()