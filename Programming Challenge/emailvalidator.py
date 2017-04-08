'''
------------------------------------------
| Programming Challenge: Email Validator |
------------------------------------------

Challenge source: http://usingpython.com/python-programming-challenges/
Description:
Email valitor program will validate the email address entered by a user.
It will give a recommendation if the user's email domain is not in
allowed domain. For example:

Enter your email address: pythonproject@yaoumail.com
*Did you mean pythonproject@ymail.com? [y/n]

'''

import re

def check_email(email):
	# feel free to add another domain
	allowed_domain = ['gmail.com', 'yahoo.com', 'ymail.com', 'live.com', 'outlook.com']
	
	match = re.search('([a-z0-9_.]+)@([a-z.]+)', email)
	if match:
		if match.group(2) not in allowed_domain:
			count = []
			for domain in allowed_domain:
				new_domain = list(domain)
				for letter in match.group(2):
					if letter in new_domain:
						new_domain.remove(letter)
				count.append(len(new_domain))
			minimum = min(count)
			min_index = count.index(minimum)
			recommended_email = allowed_domain[min_index]
			print("*Did you mean %s@%s? [y/n] " % (match.group(1), recommended_email), end='')
			answer = input()
			if str(answer) == 'y' or str(answer) == 'Y':
				return "Got it! Your email is %s@%s" % (match.group(1), recommended_email)
			else:
				return False
		else:
			return "Your email is valid!"
	else:
		return "Your email is not valid!"
		
def main():
	email = input("Enter your email address: ")
	respond = check_email(email)
	while respond == False:
		email = input("Enter your email address: ")
		respond = check_email(email)
	print(respond)
	
if __name__ == '__main__':
	main()