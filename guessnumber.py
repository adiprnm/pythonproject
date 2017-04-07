import random, os

def check_actual_number(guess, actual):
	if guess > actual:
		return "The number you guessed is too high!"
	elif guess < actual:
		return "The number you guessed is too low!"
	else:
		return "OK!"

os.system("cls")
os.startfile("time.m4a")
correct_answer = random.randint(0,100)
print("== GUESS THE NUMBER ==")
while True:
	guess_number = int(input("Guess the number between 0 until 100: "))
	print(check_actual_number(guess_number, correct_answer))
	if check_actual_number(guess_number, correct_answer) == "OK!":
		print("The answer is", correct_answer)
		break