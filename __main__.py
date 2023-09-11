#!/usr/bin/env python

import random

# empty prints are for blank lines in formatting output

print()

first_name: str
last_name: str

nicknames: list[str] = [
	"the Sheep",
	"the Terminator",
	"the Oracle",
	"the Cobra",
	"the Bull",
	"the Boomer",
	"the Joker",
	"the Lion",
	"the Bulldog",
	"the Beard",
]

def register_name() -> None:
	global first_name, last_name

	first_name	= input("Enter your first name: ").capitalize()
	last_name	= input("Enter your last name: " ).capitalize()

def print_nickname(nickname: str) -> None:
	global first_name, last_name

	print(f'{first_name} "{nickname}" {last_name}')

def nickname_exists(nickname: str) -> bool:
	return True if nickname in nicknames else False

register_name()
print()

while True:
	print(f"MAIN MENU ({first_name} {last_name})")
	print("1. Change name")
	print("2. Display a Random Nickname")
	print("3. Display All Nicknames")
	print("4. Add a Nickname")
	print("5. Remove a Nickname")
	print("6. Exit")

	option: str = input("Select an option (1-6): ")
	print() # blank line

	match option:
		case '1':
			print("CHANGE NAME")
			register_name()
			print(f"Name has been changed to {first_name} {last_name}.")
		case '2':
			print("RANDOM NICKNAME")
			print_nickname(random.choice(nicknames))
		case '3':
			print("ALL NICKNAMES")
			for nickname in nicknames:
				print_nickname(nickname)
		case '4':
			print("ADD A NICKNAME")
			nickname: str = input("Please enter a nickname to add: ")

			if nickname_exists(nickname):
				print(f"{nickname} is already in the list.")
			else:
				nicknames.append(nickname)
				print(f"{nickname} added to the nickname list.")
		case '5':
			print("REMOVE A NICKNAME")
			nickname: str = input("Please enter a nickname to remove: ")

			if nickname_exists(nickname):
				nicknames.remove(nickname)
				print(f"{nickname} removed from the nickname list.")
			else:
				print(f"{nickname} was not found in the nickname list.")
		case '6':
			break
		case _:
			print("Invalid option. Try again...")
	
	print() # blank line
