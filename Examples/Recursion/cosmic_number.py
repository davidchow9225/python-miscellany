#cosmic_number.py
"""Proves that four is the only number whose length in word form is equal to its numerical value."""
# IMPORTS
from num2words import num2words

#* Algorithm
def cosmic_number(num):
	# Get num in word form
	num_word = num2words(int(num))
	if len(num_word) == int(num):
		print(f"\n{num} is The Cosmic Number.","\n\n")
		return
	else:
		print(f"{num_word} is {len(num_word)}.")
		cosmic_number(len(num_word))
		
def main():
	while True:
		num = input("Please Enter Any Number.\n")
		cosmic_number(num)
		_again = input("Would you like to run another proof?\n")
		if _again.lower() == "no" or _again.lower() == "n":
			break
		print("\n")

if __name__ == "__main__":
	main()
