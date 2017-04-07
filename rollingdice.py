import random, os

while True:
	os.system("cls")
	print("=== THE ROLLING DICE GAME ===")
	your_dice = int(input("Input your dice number: "))
	while your_dice < 0 or your_dice > 6:
		your_dice = int(input("Input your dice number between 1-6: "))
	
	real_dice = random.randint(1,6)
	print("The real dice is:", real_dice)
	if your_dice == real_dice:
		print("You win!")
	else:
		print("You lose!")
	repeat = input("Try again? (y/n): ")
	if str(repeat) == "n":
		break